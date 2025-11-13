#!/usr/bin/env python3
"""
Shopify Theme Analysis Tool
Extracts app inventory, analyzes code quality, and generates evaluation data
"""

import json
import os
import re
import glob
from pathlib import Path
from typing import Dict, List, Any, Tuple
import argparse

class ShopifyThemeAnalyzer:
    def __init__(self, theme_path: str):
        self.theme_path = Path(theme_path)
        self.theme_name = self.theme_path.name
        self.analysis_results = {
            'theme_name': self.theme_name,
            'apps': [],
            'scripts': [],
            'assets': {},
            'code_quality': {},
            'architecture': {},
            'performance_indicators': {}
        }
    
    def extract_apps_from_settings(self) -> List[Dict]:
        """Extract installed apps from settings_data.json"""
        apps = []
        settings_file = self.theme_path / 'config' / 'settings_data.json'
        
        if not settings_file.exists():
            return apps
        
        try:
            with open(settings_file, 'r', encoding='utf-8') as f:
                settings = json.load(f)
            
            # Look for app blocks in the settings
            if 'current' in settings and 'blocks' in settings['current']:
                for block_id, block_data in settings['current']['blocks'].items():
                    if 'type' in block_data and 'shopify://apps/' in block_data['type']:
                        app_path = block_data['type']
                        app_name = self._extract_app_name(app_path)
                        apps.append({
                            'id': block_id,
                            'name': app_name,
                            'path': app_path,
                            'enabled': not block_data.get('disabled', False),
                            'settings': block_data.get('settings', {})
                        })
        except Exception as e:
            print(f"Error reading settings file: {e}")
        
        return apps
    
    def _extract_app_name(self, app_path: str) -> str:
        """Extract app name from Shopify app path"""
        # Extract app name from path like "shopify://apps/klaviyo-email-marketing-sms/blocks/..."
        match = re.search(r'shopify://apps/([^/]+)', app_path)
        return match.group(1) if match else 'Unknown App'
    
    def analyze_layout_files(self) -> List[Dict]:
        """Analyze layout files for scripts and tracking"""
        scripts = []
        layout_files = glob.glob(str(self.theme_path / 'layout' / '*.liquid'))
        
        for layout_file in layout_files:
            try:
                with open(layout_file, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                # Find script tags
                script_matches = re.findall(r'<script[^>]*>(.*?)</script>', content, re.DOTALL)
                for script in script_matches:
                    if script.strip():
                        scripts.append({
                            'file': os.path.basename(layout_file),
                            'type': 'inline_script',
                            'content': script.strip()[:200] + '...' if len(script.strip()) > 200 else script.strip()
                        })
                
                # Find external script sources
                external_scripts = re.findall(r'<script[^>]*src=["\']([^"\']*)["\'][^>]*>', content)
                for src in external_scripts:
                    scripts.append({
                        'file': os.path.basename(layout_file),
                        'type': 'external_script',
                        'src': src
                    })
                
                # Find tracking pixels and analytics
                tracking_patterns = [
                    r'gtag\([^)]+\)',
                    r'fbq\([^)]+\)',
                    r'_gaq\.push\([^)]+\)',
                    r'dataLayer\.push\([^)]+\)'
                ]
                
                for pattern in tracking_patterns:
                    matches = re.findall(pattern, content)
                    for match in matches:
                        scripts.append({
                            'file': os.path.basename(layout_file),
                            'type': 'tracking',
                            'content': match
                        })
                        
            except Exception as e:
                print(f"Error analyzing {layout_file}: {e}")
        
        return scripts
    
    def analyze_assets(self) -> Dict[str, Any]:
        """Analyze theme assets for optimization opportunities"""
        assets = {
            'css_files': [],
            'js_files': [],
            'images': [],
            'fonts': [],
            'total_size': 0
        }
        
        assets_dir = self.theme_path / 'assets'
        if not assets_dir.exists():
            return assets
        
        for file_path in assets_dir.iterdir():
            if file_path.is_file():
                file_size = file_path.stat().st_size
                assets['total_size'] += file_size
                
                if file_path.suffix.lower() in ['.css', '.scss']:
                    assets['css_files'].append({
                        'name': file_path.name,
                        'size': file_size,
                        'size_mb': round(file_size / 1024 / 1024, 2)
                    })
                elif file_path.suffix.lower() in ['.js']:
                    assets['js_files'].append({
                        'name': file_path.name,
                        'size': file_size,
                        'size_mb': round(file_size / 1024 / 1024, 2)
                    })
                elif file_path.suffix.lower() in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']:
                    assets['images'].append({
                        'name': file_path.name,
                        'size': file_size,
                        'size_mb': round(file_size / 1024 / 1024, 2)
                    })
                elif file_path.suffix.lower() in ['.woff', '.woff2', '.ttf', '.otf']:
                    assets['fonts'].append({
                        'name': file_path.name,
                        'size': file_size,
                        'size_mb': round(file_size / 1024 / 1024, 2)
                    })
        
        assets['total_size_mb'] = round(assets['total_size'] / 1024 / 1024, 2)
        return assets
    
    def analyze_code_quality(self) -> Dict[str, Any]:
        """Analyze Liquid code quality and patterns"""
        quality_metrics = {
            'deprecated_tags': [],
            'performance_issues': [],
            'custom_sections': 0,
            'custom_snippets': 0,
            'total_lines': 0
        }
        
        # Deprecated Liquid tags to check for
        deprecated_patterns = [
            r'\{\%\s*assign\s+',
            r'\{\%\s*capture\s+',
            r'\{\%\s*comment\s+',
            r'\{\%\s*raw\s+',
            r'\{\%\s*endraw\s+'
        ]
        
        # Performance anti-patterns
        performance_patterns = [
            r'\{\%\s*for\s+.*?\s+in\s+.*?\s*\%\}',
            r'\{\%\s*if\s+.*?\s*\%\}',
            r'\.liquid\s*\.liquid',  # Double .liquid extension
            r'asset_url\s*\(\s*["\'][^"\']*\.(jpg|jpeg|png|gif)["\']\s*\)'  # Unoptimized images
        ]
        
        # Analyze all Liquid files
        liquid_files = []
        liquid_files.extend(glob.glob(str(self.theme_path / '**' / '*.liquid'), recursive=True))
        
        for file_path in liquid_files:
            try:
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                
                quality_metrics['total_lines'] += len(content.splitlines())
                
                # Check for deprecated patterns
                for pattern in deprecated_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    if matches:
                        quality_metrics['deprecated_tags'].append({
                            'file': os.path.relpath(file_path, self.theme_path),
                            'pattern': pattern,
                            'count': len(matches)
                        })
                
                # Check for performance issues
                for pattern in performance_patterns:
                    matches = re.findall(pattern, content, re.IGNORECASE)
                    if matches:
                        quality_metrics['performance_issues'].append({
                            'file': os.path.relpath(file_path, self.theme_path),
                            'pattern': pattern,
                            'count': len(matches)
                        })
                
                # Count custom sections and snippets
                if 'sections' in str(file_path):
                    quality_metrics['custom_sections'] += 1
                elif 'snippets' in str(file_path):
                    quality_metrics['custom_snippets'] += 1
                    
            except Exception as e:
                print(f"Error analyzing {file_path}: {e}")
        
        return quality_metrics
    
    def analyze_architecture(self) -> Dict[str, Any]:
        """Analyze theme architecture and structure"""
        architecture = {
            'sections_count': 0,
            'snippets_count': 0,
            'templates_count': 0,
            'layouts_count': 0,
            'locales_count': 0,
            'has_shogun': False,
            'has_custom_checkout': False,
            'complexity_score': 0
        }
        
        # Count files by type
        architecture['sections_count'] = len(glob.glob(str(self.theme_path / 'sections' / '*.liquid')))
        architecture['snippets_count'] = len(glob.glob(str(self.theme_path / 'snippets' / '*.liquid')))
        architecture['templates_count'] = len(glob.glob(str(self.theme_path / 'templates' / '*.liquid')))
        architecture['layouts_count'] = len(glob.glob(str(self.theme_path / 'layout' / '*.liquid')))
        architecture['locales_count'] = len(glob.glob(str(self.theme_path / 'locales' / '*.json')))
        
        # Check for Shogun integration
        shogun_files = glob.glob(str(self.theme_path / '**' / '*shogun*'), recursive=True)
        architecture['has_shogun'] = len(shogun_files) > 0
        
        # Check for custom checkout
        checkout_files = glob.glob(str(self.theme_path / 'layout' / '*checkout*'), recursive=True)
        architecture['has_custom_checkout'] = len(checkout_files) > 0
        
        # Calculate complexity score
        architecture['complexity_score'] = (
            architecture['sections_count'] * 2 +
            architecture['snippets_count'] * 1 +
            architecture['templates_count'] * 1 +
            architecture['layouts_count'] * 3 +
            (1 if architecture['has_shogun'] else 0) * 5 +
            (1 if architecture['has_custom_checkout'] else 0) * 3
        )
        
        return architecture
    
    def run_analysis(self) -> Dict[str, Any]:
        """Run complete theme analysis"""
        print(f"Analyzing theme: {self.theme_name}")
        
        self.analysis_results['apps'] = self.extract_apps_from_settings()
        self.analysis_results['scripts'] = self.analyze_layout_files()
        self.analysis_results['assets'] = self.analyze_assets()
        self.analysis_results['code_quality'] = self.analyze_code_quality()
        self.analysis_results['architecture'] = self.analyze_architecture()
        
        return self.analysis_results
    
    def generate_report(self) -> str:
        """Generate a formatted analysis report"""
        report = f"""
# Shopify Theme Analysis Report: {self.theme_name}

## App Ecosystem Analysis
**Total Apps Found**: {len(self.analysis_results['apps'])}

### Installed Apps:
"""
        
        for app in self.analysis_results['apps']:
            status = "✅ Enabled" if app['enabled'] else "❌ Disabled"
            report += f"- **{app['name']}**: {status}\n"
        
        report += f"""
## Technical Performance Indicators

### Asset Analysis:
- **Total Asset Size**: {self.analysis_results['assets']['total_size_mb']} MB
- **CSS Files**: {len(self.analysis_results['assets']['css_files'])} files
- **JavaScript Files**: {len(self.analysis_results['assets']['js_files'])} files
- **Images**: {len(self.analysis_results['assets']['images'])} files
- **Fonts**: {len(self.analysis_results['assets']['fonts'])} files

### Code Quality:
- **Total Lines of Code**: {self.analysis_results['code_quality']['total_lines']:,}
- **Custom Sections**: {self.analysis_results['code_quality']['custom_sections']}
- **Custom Snippets**: {self.analysis_results['code_quality']['custom_snippets']}
- **Deprecated Tags Found**: {len(self.analysis_results['code_quality']['deprecated_tags'])}
- **Performance Issues**: {len(self.analysis_results['code_quality']['performance_issues'])}

## Architecture Analysis
- **Sections**: {self.analysis_results['architecture']['sections_count']}
- **Snippets**: {self.analysis_results['architecture']['snippets_count']}
- **Templates**: {self.analysis_results['architecture']['templates_count']}
- **Layouts**: {self.analysis_results['architecture']['layouts_count']}
- **Locales**: {self.analysis_results['architecture']['locales_count']}
- **Shogun Integration**: {'Yes' if self.analysis_results['architecture']['has_shogun'] else 'No'}
- **Custom Checkout**: {'Yes' if self.analysis_results['architecture']['has_custom_checkout'] else 'No'}
- **Complexity Score**: {self.analysis_results['architecture']['complexity_score']}

## Scripts and Tracking
**Total Scripts Found**: {len(self.analysis_results['scripts'])}

### Script Types:
"""
        
        script_types = {}
        for script in self.analysis_results['scripts']:
            script_type = script['type']
            script_types[script_type] = script_types.get(script_type, 0) + 1
        
        for script_type, count in script_types.items():
            report += f"- **{script_type.replace('_', ' ').title()}**: {count}\n"
        
        return report

def main():
    parser = argparse.ArgumentParser(description='Analyze Shopify theme')
    parser.add_argument('theme_path', help='Path to theme directory')
    parser.add_argument('--output', '-o', help='Output file for analysis results')
    
    args = parser.parse_args()
    
    analyzer = ShopifyThemeAnalyzer(args.theme_path)
    results = analyzer.run_analysis()
    
    if args.output:
        with open(args.output, 'w', encoding='utf-8') as f:
            json.dump(results, f, indent=2)
        print(f"Analysis results saved to {args.output}")
    else:
        print(analyzer.generate_report())

if __name__ == '__main__':
    main()

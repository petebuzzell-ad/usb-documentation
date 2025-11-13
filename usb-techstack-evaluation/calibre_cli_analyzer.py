#!/usr/bin/env python3
"""
Calibre CLI Integration for Shopify Theme Evaluations
Uses Calibre CLI commands to get performance data
"""

import subprocess
import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
import argparse

class CalibreCLIAnalyzer:
    def __init__(self, api_key: str = None):
        self.api_key = api_key
        if api_key:
            self.set_api_key(api_key)
    
    def set_api_key(self, api_key: str):
        """Set the Calibre API key using CLI"""
        try:
            result = subprocess.run(
                ['npx', 'calibre', 'token', 'set', api_key],
                capture_output=True,
                text=True,
                check=True
            )
            print(f"✅ API key set successfully")
            return True
        except subprocess.CalledProcessError as e:
            print(f"❌ Failed to set API key: {e.stderr}")
            return False
    
    def run_calibre_command(self, command: List[str]) -> Dict:
        """Run a Calibre CLI command and return JSON output"""
        try:
            # Replace 'calibre' with 'npx calibre' in the command
            if command[0] == 'calibre':
                command[0] = 'npx'
                command.insert(1, 'calibre')
            
            # Add --json flag to get structured output
            command_with_json = command + ['--json']
            result = subprocess.run(
                command_with_json,
                capture_output=True,
                text=True,
                check=True
            )
            return json.loads(result.stdout)
        except subprocess.CalledProcessError as e:
            print(f"❌ Calibre command failed: {e.stderr}")
            return {}
        except json.JSONDecodeError as e:
            print(f"❌ Failed to parse JSON output: {e}")
            return {}
    
    def list_sites(self) -> List[Dict]:
        """List all sites using CLI"""
        print("🔍 Listing sites...")
        result = self.run_calibre_command(['calibre', 'site', 'list'])
        if result and isinstance(result, list):
            return result
        elif result and 'sites' in result:
            return result['sites']
        return []
    
    def find_site_by_url(self, target_url: str) -> Optional[Dict]:
        """Find site by URL or name"""
        sites = self.list_sites()
        
        # Extract domain from URL for matching
        domain = target_url.replace('https://', '').replace('http://', '').replace('www.', '').split('/')[0]
        
        # Map known URLs to site names
        url_to_name = {
            'cutterssports.com': 'Cutters',
            'mcdavid.com': 'McDavid', 
            'nathansports.com': 'Nathan',
            'pearlizumi.com': 'Pearl iZumi',
            'shockdoctor.com': 'Shock Doctor'
        }
        
        site_name = url_to_name.get(domain)
        if site_name:
            for site in sites:
                if site.get('name') == site_name:
                    return site
        
        # Fallback: try to match by domain
        for site in sites:
            if domain in site.get('name', '').lower() or domain.replace('.', '') in site.get('slug', ''):
                return site
        
        return None
    
    def get_latest_snapshot(self, site_slug: str) -> Optional[Dict]:
        """Get the latest snapshot for a site"""
        print(f"🔍 Getting latest snapshot for {site_slug}...")
        result = self.run_calibre_command(['calibre', 'site', 'snapshots', '--site', site_slug])
        if result and 'snapshots' in result and result['snapshots']:
            # Return the first (latest) snapshot
            snapshot = result['snapshots'][0]
            # Use iid as the ID for metrics queries
            snapshot['id'] = snapshot.get('iid')
            return snapshot
        return None
    
    def get_snapshot_metrics(self, site_slug: str, snapshot_id: str) -> Dict:
        """Get metrics for a specific snapshot"""
        print(f"📊 Getting metrics for snapshot {snapshot_id}...")
        result = self.run_calibre_command([
            'calibre', 'site', 'get-snapshot-metrics',
            '--site', site_slug,
            '--snapshot', snapshot_id
        ])
        return result
    
    def get_site_metrics(self, site_slug: str, days: int = 30) -> Dict:
        """Get time-series metrics for a site"""
        print(f"📈 Getting time-series metrics for {site_slug}...")
        result = self.run_calibre_command([
            'calibre', 'site', 'metrics',
            '--site', site_slug
        ])
        return result
    
    def run_single_page_test(self, url: str, location: str = 'us-east-1') -> Dict:
        """Run a single page test"""
        print(f"🧪 Running single page test for {url}...")
        result = self.run_calibre_command([
            'calibre', 'test', 'create', url,
            '--location', location,
            '--waitForTest'
        ])
        return result
    
    def analyze_site(self, site_url: str) -> Dict:
        """Complete analysis of a site using CLI"""
        print(f"🔍 Analyzing {site_url}...")
        
        # First, try to find the site in the list
        site = self.find_site_by_url(site_url)
        if not site:
            print(f"❌ Site not found in Calibre: {site_url}")
            print("💡 Running single page test instead...")
            return self.run_single_page_test(site_url)
        
        site_slug = site.get('slug')
        print(f"✅ Found site: {site.get('name')} (slug: {site_slug})")
        
        # Get latest snapshot
        latest_snapshot = self.get_latest_snapshot(site_slug)
        if not latest_snapshot:
            print("⚠️  No snapshots found, running single page test...")
            return self.run_single_page_test(site_url)
        
        snapshot_id = str(latest_snapshot.get('id'))
        print(f"📸 Latest snapshot: {snapshot_id}")
        
        # Get snapshot metrics
        snapshot_metrics = self.get_snapshot_metrics(site_slug, snapshot_id)
        
        # Get time-series metrics
        time_series_metrics = self.get_site_metrics(site_slug)
        
        # Calculate scores
        performance_score = self.calculate_performance_score(snapshot_metrics)
        accessibility_score = self.calculate_accessibility_score(snapshot_metrics)
        
        return {
            'site_info': site,
            'latest_snapshot': latest_snapshot,
            'snapshot_metrics': snapshot_metrics,
            'time_series_metrics': time_series_metrics,
            'scores': {
                'performance': performance_score,
                'accessibility': accessibility_score
            },
            'analysis_date': datetime.now().isoformat()
        }
    
    def calculate_performance_score(self, metrics: Dict) -> int:
        """Calculate performance score from metrics"""
        if not metrics or 'snapshot' not in metrics:
            return 0
        
        score = 100
        tests = metrics['snapshot'].get('tests', [])
        
        # Get average metrics across all tests
        lcp_values = []
        cls_values = []
        fcp_values = []
        ttfb_values = []
        
        for test in tests:
            measurements = test.get('measurements', [])
            for measurement in measurements:
                name = measurement.get('name', '')
                value = measurement.get('value', 0)
                
                if name == 'largest_contentful_paint':
                    lcp_values.append(value)
                elif name == 'cumulative-layout-shift':
                    cls_values.append(value)
                elif name == 'first-contentful-paint':
                    fcp_values.append(value)
                elif name == 'time-to-first-byte':
                    ttfb_values.append(value)
        
        # Calculate averages
        lcp = sum(lcp_values) / len(lcp_values) if lcp_values else 0
        cls = sum(cls_values) / len(cls_values) if cls_values else 0
        fcp = sum(fcp_values) / len(fcp_values) if fcp_values else 0
        ttfb = sum(ttfb_values) / len(ttfb_values) if ttfb_values else 0
        
        # LCP (Largest Contentful Paint) - values are in milliseconds
        if lcp > 4000:  # Poor
            score -= 30
        elif lcp > 2500:  # Needs improvement
            score -= 15
        
        # CLS (Cumulative Layout Shift) - values are in milliunits (divide by 1000)
        cls_decimal = cls / 1000
        if cls_decimal > 0.25:  # Poor
            score -= 25
        elif cls_decimal > 0.1:  # Needs improvement
            score -= 10
        
        # FCP (First Contentful Paint) - values are in milliseconds
        if fcp > 3000:  # Poor
            score -= 10
        elif fcp > 1800:  # Needs improvement
            score -= 5
        
        # TTFB (Time to First Byte) - values are in milliseconds
        if ttfb > 800:  # Poor
            score -= 10
        elif ttfb > 600:  # Needs improvement
            score -= 5
        
        return max(0, score)
    
    def calculate_accessibility_score(self, metrics: Dict) -> int:
        """Calculate accessibility score from metrics"""
        if not metrics or 'snapshot' not in metrics:
            return 0
        
        tests = metrics['snapshot'].get('tests', [])
        accessibility_values = []
        
        for test in tests:
            measurements = test.get('measurements', [])
            for measurement in measurements:
                name = measurement.get('name', '')
                value = measurement.get('value', 0)
                
                if name == 'lighthouse-accessibility-score':
                    accessibility_values.append(value)
        
        # Calculate average accessibility score
        accessibility_score = sum(accessibility_values) / len(accessibility_values) if accessibility_values else 0
        
        # Convert to 0-100 scale (values are already 0-100)
        return int(accessibility_score)

def main():
    parser = argparse.ArgumentParser(description='Analyze Shopify site with Calibre CLI')
    parser.add_argument('site_url', help='Site URL to analyze')
    parser.add_argument('--output', default='calibre-cli-analysis.json', help='Output file name')
    parser.add_argument('--api-key', help='Calibre API key (or set CALIBRE_API_KEY env var)')
    parser.add_argument('--location', default='us-east-1', help='Test location')
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.getenv('CALIBRE_API_KEY')
    if not api_key:
        print("❌ Calibre API key required. Set CALIBRE_API_KEY environment variable or use --api-key")
        sys.exit(1)
    
    # Check if Calibre CLI is available via npx
    try:
        subprocess.run(['npx', 'calibre', '--version'], capture_output=True, check=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("❌ Calibre CLI not found. Please install it first:")
        print("   npm install -g calibre")
        print("   or use npx calibre")
        sys.exit(1)
    
    # Run analysis
    analyzer = CalibreCLIAnalyzer(api_key)
    results = analyzer.analyze_site(args.site_url)
    
    if not results:
        print("❌ Analysis failed")
        sys.exit(1)
    
    # Save results
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 CALIBRE CLI ANALYSIS COMPLETE")
    print("=" * 50)
    
    if 'site_info' in results:
        print(f"Site: {results['site_info'].get('name', 'Unknown')}")
        print(f"URL: {results['site_info'].get('url', 'Unknown')}")
        print(f"Performance Score: {results['scores']['performance']}/100")
        print(f"Accessibility Score: {results['scores']['accessibility']}/100")
        
        # Print key metrics
        metrics = results.get('snapshot_metrics', {}).get('metrics', {})
        if metrics:
            print("\n🎯 Key Metrics:")
            for metric_name, metric_data in metrics.items():
                if isinstance(metric_data, dict) and 'value' in metric_data:
                    value = metric_data['value']
                    if 'lighthouse' in metric_name or 'largest-contentful-paint' in metric_name or 'cumulative-layout-shift' in metric_name:
                        print(f"  {metric_name}: {value:.2f}")
    else:
        print(f"Test URL: {results.get('url', 'Unknown')}")
        print(f"Test UUID: {results.get('uuid', 'Unknown')}")
    
    print(f"\n📄 Full analysis saved to: {args.output}")

if __name__ == "__main__":
    main()

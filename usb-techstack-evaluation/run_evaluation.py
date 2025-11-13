#!/usr/bin/env python3
"""
Shopify Tech Stack Evaluation Runner
Runs complete evaluation workflow for a theme
"""

import json
import os
import sys
import argparse
from pathlib import Path
from analyze_theme import ShopifyThemeAnalyzer

def run_static_analysis(theme_path: str, output_file: str):
    """Run static analysis on theme"""
    print(f"🔍 Running static analysis on {theme_path}...")
    
    analyzer = ShopifyThemeAnalyzer(theme_path)
    results = analyzer.run_analysis()
    
    # Save results
    with open(output_file, 'w') as f:
        json.dump(results, f, indent=2)
    
    print(f"✅ Static analysis complete: {output_file}")
    return results

def run_calibre_analysis(site_url: str, output_file: str):
    """Run Calibre performance analysis using CLI"""
    print(f"⚡ Running Calibre CLI analysis on {site_url}...")
    
    # Check if API key is set
    api_key = os.getenv('CALIBRE_API_KEY')
    if not api_key:
        print("❌ CALIBRE_API_KEY not set. Please set your Calibre API key:")
        print("   export CALIBRE_API_KEY='your-api-key-here'")
        return None
    
    # Import and run Calibre CLI analysis
    try:
        from calibre_cli_analyzer import CalibreCLIAnalyzer
        analyzer = CalibreCLIAnalyzer(api_key)
        results = analyzer.analyze_site(site_url)
        
        if results:
            # Save results
            with open(output_file, 'w') as f:
                json.dump(results, f, indent=2)
            print(f"✅ Calibre CLI analysis complete: {output_file}")
            return results
        else:
            print("⚠️  Calibre CLI analysis failed - site may not be added to dashboard")
            return None
            
    except ImportError:
        print("❌ Calibre CLI analysis module not found")
        return None
    except Exception as e:
        print(f"❌ Calibre CLI analysis error: {e}")
        return None

def generate_report(theme_name: str, static_data: dict, calibre_data: dict = None):
    """Generate evaluation report"""
    print(f"📊 Generating report for {theme_name}...")
    
    # Calculate scores
    app_score = calculate_app_score(static_data)
    performance_score = calculate_performance_score(static_data, calibre_data)
    accessibility_score = calculate_accessibility_score(static_data, calibre_data)
    privacy_score = calculate_privacy_score(static_data)
    architecture_score = calculate_architecture_score(static_data)
    
    # Overall score
    overall_score = (
        app_score * 0.20 +
        performance_score * 0.15 +
        accessibility_score * 0.10 +
        privacy_score * 0.05 +
        architecture_score * 0.50
    )
    
    # Generate report
    report = {
        'theme_name': theme_name,
        'overall_score': overall_score,
        'scores': {
            'app_ecosystem': app_score,
            'technical_performance': performance_score,
            'accessibility': accessibility_score,
            'consumer_privacy': privacy_score,
            'theme_architecture': architecture_score
        },
        'static_analysis': static_data,
        'calibre_data': calibre_data,
        'recommendations': generate_recommendations(static_data, overall_score)
    }
    
    return report

def calculate_app_score(data: dict) -> int:
    """Calculate app ecosystem score"""
    apps = data.get('apps', [])
    if not apps:
        return 0
    
    # Base score
    score = 60
    
    # Deduct for redundancies
    sms_apps = [app for app in apps if 'sms' in app.get('name', '').lower()]
    if len(sms_apps) > 1:
        score -= 20
    
    # Deduct for unclear apps
    unclear_apps = [app for app in apps if app.get('purpose') == 'Unknown']
    score -= len(unclear_apps) * 10
    
    # Bonus for essential apps
    essential_apps = ['klaviyo', 'consentmo', 'redirects']
    for app in apps:
        if any(essential in app.get('name', '').lower() for essential in essential_apps):
            score += 5
    
    return max(0, min(100, score))

def calculate_performance_score(data: dict, calibre_data: dict = None) -> int:
    """Calculate technical performance score"""
    # If we have live Calibre data, use it
    if calibre_data and 'scores' in calibre_data and 'performance' in calibre_data['scores']:
        return calibre_data['scores']['performance']
    
    # Fallback to static analysis
    score = 70
    
    # Asset size penalty
    total_assets = data.get('assets', {}).get('total_size_mb', 0)
    if total_assets > 3:
        score -= 20
    elif total_assets > 2:
        score -= 10
    
    # Complexity penalty
    complexity = data.get('code_quality', {}).get('complexity_score', 0)
    if complexity > 400:
        score -= 25
    elif complexity > 300:
        score -= 15
    elif complexity > 200:
        score -= 10
    
    # Deprecated patterns penalty
    deprecated = data.get('code_quality', {}).get('deprecated_patterns', 0)
    score -= min(20, deprecated // 10)
    
    return max(0, min(100, score))

def calculate_accessibility_score(data: dict, calibre_data: dict = None) -> int:
    """Calculate accessibility score"""
    # If we have live Calibre data, use it
    if calibre_data and 'scores' in calibre_data and 'accessibility' in calibre_data['scores']:
        return calibre_data['scores']['accessibility']
    
    # Fallback to static analysis
    score = 40  # Base score for basic structure
    
    # Check for accessibility widgets
    scripts = data.get('scripts', [])
    accessibility_scripts = [s for s in scripts if 'accessibility' in s.get('name', '').lower()]
    if accessibility_scripts:
        score += 30
    
    return max(0, min(100, score))

def calculate_privacy_score(data: dict) -> int:
    """Calculate privacy compliance score"""
    score = 60  # Base score
    
    # Check for GDPR compliance
    apps = data.get('apps', [])
    gdpr_apps = [app for app in apps if 'gdpr' in app.get('name', '').lower() or 'consent' in app.get('name', '').lower()]
    if gdpr_apps:
        score += 25
    
    # Check for privacy scripts
    scripts = data.get('scripts', [])
    privacy_scripts = [s for s in scripts if 'privacy' in s.get('name', '').lower() or 'consent' in s.get('name', '').lower()]
    if privacy_scripts:
        score += 15
    
    return max(0, min(100, score))

def calculate_architecture_score(data: dict) -> int:
    """Calculate theme architecture score"""
    score = 70
    
    # Complexity penalty
    complexity = data.get('code_quality', {}).get('complexity_score', 0)
    if complexity > 400:
        score -= 30
    elif complexity > 300:
        score -= 20
    elif complexity > 200:
        score -= 10
    
    # Asset organization bonus
    total_assets = data.get('assets', {}).get('total_size_mb', 0)
    if total_assets < 2:
        score += 10
    elif total_assets < 3:
        score += 5
    
    return max(0, min(100, score))

def generate_recommendations(data: dict, overall_score: int) -> list:
    """Generate recommendations based on analysis"""
    recommendations = []
    
    if overall_score < 70:
        recommendations.append("Priority: Address critical issues immediately")
    
    # App recommendations
    apps = data.get('apps', [])
    sms_apps = [app for app in apps if 'sms' in app.get('name', '').lower()]
    if len(sms_apps) > 1:
        recommendations.append("Consolidate SMS providers to reduce costs")
    
    unclear_apps = [app for app in apps if app.get('purpose') == 'Unknown']
    if unclear_apps:
        recommendations.append("Audit unclear apps for actual usage and ROI")
    
    # Performance recommendations
    total_assets = data.get('assets', {}).get('total_size_mb', 0)
    if total_assets > 2:
        recommendations.append("Optimize asset sizes for better performance")
    
    complexity = data.get('code_quality', {}).get('complexity_score', 0)
    if complexity > 300:
        recommendations.append("Simplify theme architecture to reduce maintenance complexity")
    
    # Accessibility recommendations
    scripts = data.get('scripts', [])
    accessibility_scripts = [s for s in scripts if 'accessibility' in s.get('name', '').lower()]
    if not accessibility_scripts:
        recommendations.append("Implement accessibility widget for legal compliance")
    
    return recommendations

def main():
    parser = argparse.ArgumentParser(description='Run Shopify tech stack evaluation')
    parser.add_argument('theme_path', help='Path to theme folder')
    parser.add_argument('--site-url', help='Live site URL for performance testing')
    parser.add_argument('--output', default='evaluation-report.json', help='Output file name')
    parser.add_argument('--skip-calibre', action='store_true', help='Skip Calibre analysis')
    
    args = parser.parse_args()
    
    # Validate theme path
    if not os.path.exists(args.theme_path):
        print(f"❌ Theme path not found: {args.theme_path}")
        sys.exit(1)
    
    theme_name = Path(args.theme_path).name
    
    print(f"🚀 Starting evaluation for {theme_name}")
    print("=" * 50)
    
    # Run static analysis
    static_file = f"{theme_name}-static.json"
    static_data = run_static_analysis(args.theme_path, static_file)
    
    # Run Calibre analysis (if URL provided and not skipped)
    calibre_data = None
    if args.site_url and not args.skip_calibre:
        calibre_file = f"{theme_name}-calibre.json"
        calibre_data = run_calibre_analysis(args.site_url, calibre_file)
    
    # Generate report
    report = generate_report(theme_name, static_data, calibre_data)
    
    # Save report
    with open(args.output, 'w') as f:
        json.dump(report, f, indent=2)
    
    # Print summary
    print("\n" + "=" * 50)
    print(f"📊 EVALUATION COMPLETE: {theme_name}")
    print("=" * 50)
    print(f"Overall Score: {report['overall_score']:.0f}/100")
    print(f"App Ecosystem: {report['scores']['app_ecosystem']}/100")
    print(f"Performance: {report['scores']['technical_performance']}/100")
    print(f"Accessibility: {report['scores']['accessibility']}/100")
    print(f"Privacy: {report['scores']['consumer_privacy']}/100")
    print(f"Architecture: {report['scores']['theme_architecture']}/100")
    
    print("\n🎯 Key Recommendations:")
    for i, rec in enumerate(report['recommendations'], 1):
        print(f"  {i}. {rec}")
    
    print(f"\n📄 Full report saved to: {args.output}")

if __name__ == "__main__":
    main()

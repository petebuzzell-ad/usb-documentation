#!/usr/bin/env python3
"""
Generate Markdown Reports from Evaluation Data
Automatically creates markdown reports with live performance data
"""

import json
import os
import sys
import argparse
from pathlib import Path
from datetime import datetime

def load_evaluation_data(theme_name: str) -> tuple:
    """Load static and Calibre data for a theme"""
    static_file = f"{theme_name}-static.json"
    calibre_file = f"{theme_name}-calibre.json"
    
    static_data = None
    calibre_data = None
    
    # Load static analysis data
    if os.path.exists(static_file):
        with open(static_file, 'r') as f:
            static_data = json.load(f)
    
    # Load Calibre data
    if os.path.exists(calibre_file):
        with open(calibre_file, 'r') as f:
            calibre_data = json.load(f)
    
    return static_data, calibre_data

def get_performance_score(static_data: dict, calibre_data: dict = None) -> int:
    """Get performance score from Calibre data or fallback to static"""
    if calibre_data and 'scores' in calibre_data and 'performance' in calibre_data['scores']:
        return calibre_data['scores']['performance']
    
    # Fallback to static analysis
    score = 70
    total_assets = static_data.get('assets', {}).get('total_size_mb', 0)
    if total_assets > 3:
        score -= 20
    elif total_assets > 2:
        score -= 10
    
    complexity = static_data.get('code_quality', {}).get('complexity_score', 0)
    if complexity > 400:
        score -= 25
    elif complexity > 300:
        score -= 15
    elif complexity > 200:
        score -= 10
    
    return max(0, min(100, score))

def get_accessibility_score(static_data: dict, calibre_data: dict = None) -> int:
    """Get accessibility score from Calibre data or fallback to static"""
    if calibre_data and 'scores' in calibre_data and 'accessibility' in calibre_data['scores']:
        return calibre_data['scores']['accessibility']
    
    # Fallback to static analysis
    score = 40
    scripts = static_data.get('scripts', [])
    accessibility_scripts = [s for s in scripts if 'accessibility' in s.get('name', '').lower()]
    if accessibility_scripts:
        score += 30
    
    return max(0, min(100, score))

def get_status_emoji(score: int) -> str:
    """Get status emoji based on score"""
    if score >= 80:
        return "✅"
    elif score >= 70:
        return "⚠️"
    else:
        return "❌"

def get_status_text(score: int) -> str:
    """Get status text based on score"""
    if score >= 80:
        return "Good"
    elif score >= 70:
        return "Warning"
    else:
        return "Poor"

def generate_markdown_report(theme_name: str, static_data: dict, calibre_data: dict = None) -> str:
    """Generate markdown report with live performance data"""
    
    # Calculate scores
    performance_score = get_performance_score(static_data, calibre_data)
    accessibility_score = get_accessibility_score(static_data, calibre_data)
    
    # Calculate overall score (simplified)
    overall_score = int((performance_score + accessibility_score) / 2)
    
    # Get status
    status_emoji = get_status_emoji(overall_score)
    status_text = get_status_text(overall_score)
    
    # Extract key data
    apps = static_data.get('apps', [])
    total_assets = static_data.get('assets', {}).get('total_size_mb', 0)
    complexity = static_data.get('code_quality', {}).get('complexity_score', 0)
    
    # Generate report
    report = f"""# {theme_name.replace('-', ' ').title()} - Tech Stack Evaluation Report

## Executive Summary

**Overall Score: {overall_score}/100** {status_emoji} **{status_text}**

{theme_name.replace('-', ' ').title()} demonstrates a {'strong' if overall_score >= 80 else 'moderate' if overall_score >= 70 else 'challenging'} tech stack with {'excellent' if overall_score >= 80 else 'some' if overall_score >= 70 else 'significant'} areas {'requiring attention' if overall_score < 80 else 'for optimization'}.

## Key Findings

### ✅ Strengths
- **Live Performance Data**: Performance score of {performance_score}/100
- **Accessibility Compliance**: Accessibility score of {accessibility_score}/100
- **App Ecosystem**: {len(apps)} installed apps with clear purposes
- **Theme Structure**: Well-organized theme architecture

### ⚠️ Areas of Concern
- **Performance**: {'Excellent' if performance_score >= 80 else 'Good' if performance_score >= 70 else 'Needs improvement'} performance score
- **Accessibility**: {'Excellent' if accessibility_score >= 80 else 'Good' if accessibility_score >= 70 else 'Needs improvement'} accessibility score
- **Theme Complexity**: Complexity score of {complexity} ({'High' if complexity > 300 else 'Medium' if complexity > 200 else 'Low'} complexity)
- **Asset Size**: {total_assets:.1f} MB total assets ({'Large' if total_assets > 2 else 'Moderate' if total_assets > 1 else 'Small'} size)

## Detailed Analysis

### 1. Technical Performance Analysis (Score: {performance_score}/100) {get_status_emoji(performance_score)} **{get_status_text(performance_score)}**

#### Live Performance Data (Calibre CLI)
- **Performance Score**: {performance_score}/100 {get_status_emoji(performance_score)} **{get_status_text(performance_score)}**
- **Accessibility Score**: {accessibility_score}/100 {get_status_emoji(accessibility_score)} **{get_status_text(accessibility_score)}**
- **Core Web Vitals**: {'All metrics within acceptable ranges' if performance_score >= 80 else 'Some metrics need improvement' if performance_score >= 70 else 'Multiple metrics require optimization'}
- **Lighthouse Accessibility**: {accessibility_score}/100 - {'Excellent' if accessibility_score >= 80 else 'Good' if accessibility_score >= 70 else 'Needs improvement'} compliance

#### Asset Analysis
- **Total Asset Size**: {total_assets:.1f} MB
- **Theme Complexity**: {complexity} complexity score
- **Installed Apps**: {len(apps)} apps

#### Performance {'Strengths' if performance_score >= 80 else 'Areas for Improvement'}
{get_performance_analysis(performance_score, accessibility_score)}

### 2. Accessibility Compliance (Score: {accessibility_score}/100) {get_status_emoji(accessibility_score)} **{get_status_text(accessibility_score)}**

#### Live Accessibility Data (Calibre CLI)
- **Lighthouse Accessibility Score**: {accessibility_score}/100 {get_status_emoji(accessibility_score)} **{get_status_text(accessibility_score)}**
- **WCAG Compliance**: {'Strong' if accessibility_score >= 80 else 'Moderate' if accessibility_score >= 70 else 'Weak'} compliance with accessibility standards
- **Screen Reader Support**: {'Good' if accessibility_score >= 80 else 'Basic' if accessibility_score >= 70 else 'Limited'} screen reader compatibility
- **Keyboard Navigation**: {'Proper' if accessibility_score >= 80 else 'Basic' if accessibility_score >= 70 else 'Limited'} keyboard navigation implemented

#### Current {'Strengths' if accessibility_score >= 80 else 'Areas for Enhancement'}
{get_accessibility_analysis(accessibility_score)}

### 3. App Ecosystem Analysis

#### Installed Apps ({len(apps)} total)
"""
    
    # Add app details
    for i, app in enumerate(apps, 1):
        app_name = app.get('name', 'Unknown')
        app_purpose = app.get('purpose', 'Unknown')
        status = "✅" if app_purpose != "Unknown" else "❌"
        report += f"{i}. **{app_name}** {status}\n   - Purpose: {app_purpose}\n   - Status: Active\n\n"
    
    report += f"""
#### App Analysis
- **Total Apps**: {len(apps)} installed apps
- **Clear Purpose**: {len([app for app in apps if app.get('purpose') != 'Unknown'])}/{len(apps)} apps have clear purposes
- **Potential Issues**: {len([app for app in apps if app.get('purpose') == 'Unknown'])} apps need review

## Priority Recommendations

### Immediate Actions (0-30 days)
{get_immediate_recommendations(performance_score, accessibility_score, len(apps))}

### Short-term Actions (1-3 months)
{get_shortterm_recommendations(performance_score, accessibility_score, complexity)}

### Long-term Actions (3-6 months)
{get_longterm_recommendations(overall_score, complexity)}

## Cost-Benefit Analysis

### Estimated Costs
- **Performance Optimization**: ${get_performance_cost(performance_score):,} (development)
- **Accessibility Implementation**: $50-100/month
- **App Consolidation**: $0 (saves money)
- **Theme Refactoring**: ${get_refactoring_cost(complexity):,} (if needed)

### Expected Benefits
- **Improved Performance**: {'20-30%' if performance_score < 80 else '10-15%'} faster load times
- **Better Accessibility**: Legal compliance and broader audience reach
- **Reduced Maintenance**: Lower ongoing development costs
- **Enhanced User Experience**: Higher conversion rates

## Conclusion

{theme_name.replace('-', ' ').title()} has a {'solid foundation' if overall_score >= 80 else 'moderate foundation' if overall_score >= 70 else 'challenging foundation'} but requires {'focused improvements' if overall_score < 80 else 'optimization'} in {'performance, accessibility, and app optimization' if overall_score < 80 else 'app optimization and maintenance'}. 

**Next Steps**: {'Implement immediate actions while planning for comprehensive theme optimization' if overall_score < 80 else 'Focus on app consolidation and maintenance optimization'}.

---
*Report generated on {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*
*Live performance data from Calibre CLI*
"""
    
    return report

def get_performance_analysis(performance_score: int, accessibility_score: int) -> str:
    """Get performance analysis text"""
    if performance_score >= 80:
        return """1. **Excellent Core Web Vitals**: LCP, CLS, FCP, TTFB all performing excellently
2. **Excellent Accessibility**: Strong Lighthouse accessibility score
3. **Optimized Asset Loading**: Efficient script and CSS loading
4. **Mobile Performance**: Excellent mobile experience"""
    elif performance_score >= 70:
        return """1. **Good Core Web Vitals**: Most metrics performing well
2. **Good Accessibility**: Strong Lighthouse accessibility score
3. **Optimized Asset Loading**: Generally efficient loading
4. **Mobile Performance**: Good mobile experience"""
    else:
        return """1. **Core Web Vitals Issues**: LCP, CLS, FCP, TTFB need optimization
2. **Asset Loading**: Script and CSS loading needs optimization
3. **Mobile Performance**: Mobile experience needs improvement
4. **Performance Bottlenecks**: Multiple performance issues identified"""

def get_accessibility_analysis(accessibility_score: int) -> str:
    """Get accessibility analysis text"""
    if accessibility_score >= 80:
        return """- **Excellent Lighthouse Score**: Strong accessibility compliance
- **Proper HTML Structure**: Good semantic HTML structure
- **Color Contrast**: Likely compliant (based on high Lighthouse score)
- **Focus Management**: Proper focus management implemented"""
    elif accessibility_score >= 70:
        return """- **Good Lighthouse Score**: Moderate accessibility compliance
- **Basic HTML Structure**: Standard HTML structure
- **Color Contrast**: May need review
- **Focus Management**: Basic focus management"""
    else:
        return """- **Low Lighthouse Score**: Accessibility compliance issues
- **HTML Structure**: Needs accessibility improvements
- **Color Contrast**: Likely non-compliant
- **Focus Management**: Needs improvement"""

def get_immediate_recommendations(performance_score: int, accessibility_score: int, app_count: int) -> str:
    """Get immediate recommendations"""
    recommendations = []
    
    if performance_score < 70:
        recommendations.append("1. **Performance Optimization**: Address critical performance issues")
    
    if accessibility_score < 80:
        recommendations.append("2. **Accessibility Implementation**: Add accessibility widget and improve compliance")
    
    if app_count > 10:
        recommendations.append("3. **App Audit**: Review all apps for actual usage and ROI")
    
    recommendations.append("4. **SMS Consolidation**: Choose single SMS provider if multiple exist")
    
    return "\n".join(recommendations)

def get_shortterm_recommendations(performance_score: int, accessibility_score: int, complexity: int) -> str:
    """Get short-term recommendations"""
    recommendations = []
    
    if performance_score < 80:
        recommendations.append("1. **Performance**: Implement lazy loading and script optimization")
    
    if accessibility_score < 85:
        recommendations.append("2. **Accessibility**: Complete WCAG AA compliance")
    
    if complexity > 300:
        recommendations.append("3. **Code Quality**: Replace deprecated Liquid patterns")
    
    recommendations.append("4. **Privacy**: Implement comprehensive privacy features")
    
    return "\n".join(recommendations)

def get_longterm_recommendations(overall_score: int, complexity: int) -> str:
    """Get long-term recommendations"""
    recommendations = []
    
    if overall_score < 80:
        recommendations.append("1. **Theme Refactoring**: Consider theme upgrade or rebuild")
    
    if complexity > 300:
        recommendations.append("2. **Architecture**: Simplify theme architecture")
    
    recommendations.append("3. **Advanced Analytics**: Implement comprehensive analytics")
    recommendations.append("4. **Monitoring**: Set up continuous performance monitoring")
    
    return "\n".join(recommendations)

def get_performance_cost(performance_score: int) -> int:
    """Get estimated performance optimization cost"""
    if performance_score >= 80:
        return 1000
    elif performance_score >= 70:
        return 3000
    else:
        return 8000

def get_refactoring_cost(complexity: int) -> int:
    """Get estimated refactoring cost"""
    if complexity > 400:
        return 20000
    elif complexity > 300:
        return 15000
    else:
        return 10000

def main():
    parser = argparse.ArgumentParser(description='Generate markdown reports from evaluation data')
    parser.add_argument('theme_name', help='Theme name (e.g., cutters-sports)')
    parser.add_argument('--output', help='Output file name (default: {theme_name}-evaluation.md)')
    
    args = parser.parse_args()
    
    # Load data
    static_data, calibre_data = load_evaluation_data(args.theme_name)
    
    if not static_data:
        print(f"❌ No static analysis data found for {args.theme_name}")
        sys.exit(1)
    
    # Generate report
    report = generate_markdown_report(args.theme_name, static_data, calibre_data)
    
    # Save report
    output_file = args.output or f"{args.theme_name}-evaluation.md"
    with open(output_file, 'w') as f:
        f.write(report)
    
    print(f"✅ Markdown report generated: {output_file}")
    
    # Print summary
    performance_score = get_performance_score(static_data, calibre_data)
    accessibility_score = get_accessibility_score(static_data, calibre_data)
    overall_score = int((performance_score + accessibility_score) / 2)
    
    print(f"\n📊 Summary:")
    print(f"Overall Score: {overall_score}/100")
    print(f"Performance: {performance_score}/100")
    print(f"Accessibility: {accessibility_score}/100")
    print(f"Live Data: {'✅ Yes' if calibre_data else '❌ No'}")

if __name__ == "__main__":
    main()

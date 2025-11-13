#!/usr/bin/env python3
"""
Calibre API Integration for Shopify Theme Evaluations
Pulls Core Web Vitals, CrUX data, and Lighthouse accessibility scores
"""

import requests
import json
import os
import sys
from datetime import datetime, timedelta
from typing import Dict, List, Any, Optional
import argparse

class CalibreAnalyzer:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "https://api.calibreapp.com/graphql"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def graphql_query(self, query: str, variables: Dict = None) -> Dict:
        """Execute GraphQL query"""
        payload = {"query": query}
        if variables:
            payload["variables"] = variables
        
        try:
            response = requests.post(self.base_url, headers=self.headers, json=payload)
            response.raise_for_status()
            result = response.json()
            
            # Check for authentication errors
            if 'errors' in result:
                for error in result['errors']:
                    if 'Invalid Session' in error.get('message', ''):
                        print("❌ Authentication error: Invalid session")
                        print("💡 Please check your API key and ensure it has proper permissions")
                        return {}
                    elif 'Field' in error.get('message', '') and "doesn't exist" in error.get('message', ''):
                        # This is a schema issue, not an auth issue
                        continue
                    else:
                        print(f"❌ GraphQL error: {error.get('message', 'Unknown error')}")
            
            return result
        except requests.exceptions.RequestException as e:
            print(f"❌ GraphQL query error: {e}")
            return {}
    
    def get_sites(self) -> List[Dict]:
        """Get list of sites from Calibre using GraphQL"""
        # Try different approaches to get sites
        queries = [
            # Try recent sites from current user
            """
            query {
                currentUser {
                    recentSites {
                        name
                        slug
                        canonicalUrl
                    }
                }
            }
            """,
            # Try organisation sites
            """
            query {
                organisation {
                    name
                    slug
                }
            }
            """
        ]
        
        for query in queries:
            result = self.graphql_query(query)
            if result and 'data' in result and result['data']:
                if 'currentUser' in result['data'] and result['data']['currentUser']:
                    sites = result['data']['currentUser'].get('recentSites', [])
                    if sites:
                        return sites
                elif 'organisation' in result['data'] and result['data']['organisation']:
                    # If we can access organisation, we might need to query sites differently
                    continue
        
        return []
    
    def find_site_by_url(self, target_url: str) -> Optional[Dict]:
        """Find site by URL"""
        sites = self.get_sites()
        for site in sites:
            if target_url in site.get('url', ''):
                return site
        return None
    
    def get_site_metrics(self, site_id: str, days: int = 90) -> Dict:
        """Get Core Web Vitals metrics for a site using GraphQL"""
        query = """
        query GetSiteMetrics($siteId: ID!, $startDate: Date!, $endDate: Date!) {
            site(id: $siteId) {
                id
                name
                url
                metrics(startDate: $startDate, endDate: $endDate) {
                    lcp {
                        value
                        score
                    }
                    cls {
                        value
                        score
                    }
                    inp {
                        value
                        score
                    }
                    fcp {
                        value
                        score
                    }
                    ttfb {
                        value
                        score
                    }
                }
            }
        }
        """
        
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days)
        
        variables = {
            "siteId": site_id,
            "startDate": start_date.strftime('%Y-%m-%d'),
            "endDate": end_date.strftime('%Y-%m-%d')
        }
        
        result = self.graphql_query(query, variables)
        if result and 'data' in result and result['data']['site']:
            return result['data']['site']
        return {}
    
    def get_lighthouse_scores(self, site_id: str) -> Dict:
        """Get Lighthouse scores including accessibility using GraphQL"""
        query = """
        query GetLighthouseScores($siteId: ID!) {
            site(id: $siteId) {
                id
                name
                url
                lighthouse {
                    performance {
                        score
                    }
                    accessibility {
                        score
                    }
                    bestPractices {
                        score
                    }
                    seo {
                        score
                    }
                }
            }
        }
        """
        
        variables = {"siteId": site_id}
        result = self.graphql_query(query, variables)
        if result and 'data' in result and result['data']['site']:
            return result['data']['site']
        return {}
    
    def get_crux_data(self, site_id: str) -> Dict:
        """Get CrUX data for performance trends using GraphQL"""
        query = """
        query GetCruxData($siteId: ID!) {
            site(id: $siteId) {
                id
                name
                url
                crux {
                    lcp {
                        p75
                        p90
                        p95
                    }
                    cls {
                        p75
                        p90
                        p95
                    }
                    inp {
                        p75
                        p90
                        p95
                    }
                }
            }
        }
        """
        
        variables = {"siteId": site_id}
        result = self.graphql_query(query, variables)
        if result and 'data' in result and result['data']['site']:
            return result['data']['site']
        return {}
    
    def analyze_site(self, site_url: str) -> Dict:
        """Complete analysis of a site"""
        print(f"🔍 Analyzing {site_url}...")
        
        # Check if we can access any data
        print("⚠️  Calibre API requires specific test UUIDs, not URLs")
        print("💡 To get live performance data:")
        print("   1. Go to Calibre dashboard")
        print("   2. Find the site and latest test")
        print("   3. Copy the test UUID or share token")
        print("   4. Use: python3 calibre_analysis.py --uuid <test-uuid>")
        
        return {
            'site_url': site_url,
            'status': 'requires_manual_data_collection',
            'message': 'Calibre API requires test UUIDs. Please collect data manually from dashboard.',
            'analysis_date': datetime.now().isoformat()
        }
    
    def analyze_by_uuid(self, test_uuid: str) -> Dict:
        """Analyze a specific test by UUID"""
        print(f"🔍 Analyzing test UUID: {test_uuid}...")
        
        query = """
        query GetTestData($uuid: ID!) {
            singlePageTest(uuid: $uuid) {
                url
                status
                measurements {
                    name
                    value
                }
                cruxAggregateMetrics {
                    value
                }
            }
        }
        """
        
        variables = {"uuid": test_uuid}
        result = self.graphql_query(query, variables)
        
        if result and 'data' in result and result['data']['singlePageTest']:
            test_data = result['data']['singlePageTest']
            print(f"✅ Found test for: {test_data.get('url', 'Unknown URL')}")
            
            # Calculate scores from measurements
            performance_score = self.calculate_performance_score_from_measurements(test_data.get('measurements', []))
            accessibility_score = self.calculate_accessibility_score_from_measurements(test_data.get('measurements', []))
            
            return {
                'test_data': test_data,
                'scores': {
                    'performance': performance_score,
                    'accessibility': accessibility_score
                },
                'analysis_date': datetime.now().isoformat()
            }
        else:
            print(f"❌ Test not found: {test_uuid}")
            return {}
    
    def calculate_performance_score(self, metrics: Dict) -> int:
        """Calculate performance score from Core Web Vitals"""
        if not metrics or 'metrics' not in metrics:
            return 0
        
        score = 100
        metrics_data = metrics['metrics']
        
        # LCP (Largest Contentful Paint)
        lcp = metrics_data.get('lcp', {}).get('value', 0)
        if lcp > 4000:  # Poor
            score -= 30
        elif lcp > 2500:  # Needs improvement
            score -= 15
        
        # CLS (Cumulative Layout Shift)
        cls = metrics_data.get('cls', {}).get('value', 0)
        if cls > 0.25:  # Poor
            score -= 25
        elif cls > 0.1:  # Needs improvement
            score -= 10
        
        # INP (Interaction to Next Paint)
        inp = metrics_data.get('inp', {}).get('value', 0)
        if inp > 500:  # Poor
            score -= 25
        elif inp > 200:  # Needs improvement
            score -= 10
        
        # FCP (First Contentful Paint)
        fcp = metrics_data.get('fcp', {}).get('value', 0)
        if fcp > 3000:  # Poor
            score -= 10
        elif fcp > 1800:  # Needs improvement
            score -= 5
        
        # TTFB (Time to First Byte)
        ttfb = metrics_data.get('ttfb', {}).get('value', 0)
        if ttfb > 800:  # Poor
            score -= 10
        elif ttfb > 600:  # Needs improvement
            score -= 5
        
        return max(0, score)
    
    def calculate_accessibility_score(self, lighthouse: Dict) -> int:
        """Calculate accessibility score from Lighthouse"""
        if not lighthouse or 'lighthouse' not in lighthouse:
            return 0
        
        lighthouse_data = lighthouse['lighthouse']
        accessibility_score = lighthouse_data.get('accessibility', {}).get('score', 0)
        
        # Convert to 0-100 scale
        return int(accessibility_score * 100) if accessibility_score else 0
    
    def calculate_performance_score_from_measurements(self, measurements: List[Dict]) -> int:
        """Calculate performance score from measurements array"""
        if not measurements:
            return 0
        
        score = 100
        metrics_dict = {m.get('name', ''): m.get('value', 0) for m in measurements}
        
        # LCP (Largest Contentful Paint)
        lcp = metrics_dict.get('largest-contentful-paint', 0)
        if lcp > 4000:  # Poor
            score -= 30
        elif lcp > 2500:  # Needs improvement
            score -= 15
        
        # CLS (Cumulative Layout Shift)
        cls = metrics_dict.get('cumulative-layout-shift', 0)
        if cls > 0.25:  # Poor
            score -= 25
        elif cls > 0.1:  # Needs improvement
            score -= 10
        
        # FCP (First Contentful Paint)
        fcp = metrics_dict.get('first-contentful-paint', 0)
        if fcp > 3000:  # Poor
            score -= 10
        elif fcp > 1800:  # Needs improvement
            score -= 5
        
        # TTFB (Time to First Byte)
        ttfb = metrics_dict.get('time-to-first-byte', 0)
        if ttfb > 800:  # Poor
            score -= 10
        elif ttfb > 600:  # Needs improvement
            score -= 5
        
        return max(0, score)
    
    def calculate_accessibility_score_from_measurements(self, measurements: List[Dict]) -> int:
        """Calculate accessibility score from measurements array"""
        if not measurements:
            return 0
        
        metrics_dict = {m.get('name', ''): m.get('value', 0) for m in measurements}
        accessibility_score = metrics_dict.get('lighthouse-accessibility-score', 0)
        
        # Convert to 0-100 scale
        return int(accessibility_score * 100) if accessibility_score else 0

def main():
    parser = argparse.ArgumentParser(description='Analyze Shopify site with Calibre API')
    parser.add_argument('site_url', nargs='?', help='Site URL to analyze')
    parser.add_argument('--uuid', help='Test UUID to analyze')
    parser.add_argument('--output', default='calibre-analysis.json', help='Output file name')
    parser.add_argument('--api-key', help='Calibre API key (or set CALIBRE_API_KEY env var)')
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.getenv('CALIBRE_API_KEY')
    if not api_key:
        print("❌ Calibre API key required. Set CALIBRE_API_KEY environment variable or use --api-key")
        sys.exit(1)
    
    # Run analysis
    analyzer = CalibreAnalyzer(api_key)
    
    if args.uuid:
        # Analyze by UUID
        results = analyzer.analyze_by_uuid(args.uuid)
    elif args.site_url:
        # Analyze by URL (will provide guidance)
        results = analyzer.analyze_site(args.site_url)
    else:
        print("❌ Please provide either a site URL or test UUID")
        print("Usage:")
        print("  python3 calibre_analysis.py https://example.com")
        print("  python3 calibre_analysis.py --uuid <test-uuid>")
        sys.exit(1)
    
    if not results:
        print("❌ Analysis failed")
        sys.exit(1)
    
    # Save results
    with open(args.output, 'w') as f:
        json.dump(results, f, indent=2)
    
    # Print summary
    print("\n" + "=" * 50)
    print("📊 CALIBRE ANALYSIS COMPLETE")
    print("=" * 50)
    
    if 'test_data' in results:
        print(f"Site: {results['test_data'].get('url', 'Unknown')}")
        print(f"Performance Score: {results['scores']['performance']}/100")
        print(f"Accessibility Score: {results['scores']['accessibility']}/100")
        
        # Print measurements
        measurements = results['test_data'].get('measurements', [])
        if measurements:
            print("\n🎯 Key Metrics:")
            for measurement in measurements:
                name = measurement.get('name', '')
                value = measurement.get('value', 0)
                if 'lighthouse' in name or 'largest-contentful-paint' in name or 'cumulative-layout-shift' in name:
                    print(f"  {name}: {value:.2f}")
    else:
        print(f"Status: {results.get('status', 'Unknown')}")
        print(f"Message: {results.get('message', 'No message')}")
    
    print(f"\n📄 Full analysis saved to: {args.output}")

if __name__ == "__main__":
    main()

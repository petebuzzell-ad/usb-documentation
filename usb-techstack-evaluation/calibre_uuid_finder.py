#!/usr/bin/env python3
"""
Calibre Test UUID Discovery Tool
Helps find and analyze the latest test UUIDs for sites
"""

import requests
import json
import os
import sys
from datetime import datetime
from typing import Dict, List, Any, Optional
import argparse

class CalibreUUIDFinder:
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
                    else:
                        print(f"❌ GraphQL error: {error.get('message', 'Unknown error')}")
            
            return result
        except requests.exceptions.RequestException as e:
            print(f"❌ GraphQL query error: {e}")
            return {}
    
    def test_uuid(self, uuid: str) -> Dict:
        """Test if a UUID is valid and get basic info"""
        query = """
        query GetTestInfo($uuid: ID!) {
            singlePageTest(uuid: $uuid) {
                url
                uuid
                status
                createdAt
                updatedAt
            }
        }
        """
        
        variables = {"uuid": uuid}
        result = self.graphql_query(query, variables)
        
        if result and 'data' in result and result['data']['singlePageTest']:
            return result['data']['singlePageTest']
        return {}
    
    def get_test_metrics(self, uuid: str) -> Dict:
        """Get detailed metrics for a test UUID"""
        query = """
        query GetTestMetrics($uuid: ID!) {
            singlePageTest(uuid: $uuid) {
                url
                uuid
                status
                createdAt
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
        
        variables = {"uuid": uuid}
        result = self.graphql_query(query, variables)
        
        if result and 'data' in result and result['data']['singlePageTest']:
            return result['data']['singlePageTest']
        return {}
    
    def analyze_test(self, uuid: str) -> Dict:
        """Complete analysis of a test UUID"""
        print(f"🔍 Analyzing test UUID: {uuid}...")
        
        test_data = self.get_test_metrics(uuid)
        if not test_data:
            print(f"❌ Test not found: {uuid}")
            return {}
        
        print(f"✅ Found test for: {test_data.get('url', 'Unknown URL')}")
        print(f"   Status: {test_data.get('status', 'Unknown')}")
        print(f"   Created: {test_data.get('createdAt', 'Unknown')}")
        
        # Calculate scores
        measurements = test_data.get('measurements', [])
        performance_score = self.calculate_performance_score(measurements)
        accessibility_score = self.calculate_accessibility_score(measurements)
        
        return {
            'test_data': test_data,
            'scores': {
                'performance': performance_score,
                'accessibility': accessibility_score
            },
            'analysis_date': datetime.now().isoformat()
        }
    
    def calculate_performance_score(self, measurements: List[Dict]) -> int:
        """Calculate performance score from measurements"""
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
    
    def calculate_accessibility_score(self, measurements: List[Dict]) -> int:
        """Calculate accessibility score from measurements"""
        if not measurements:
            return 0
        
        metrics_dict = {m.get('name', ''): m.get('value', 0) for m in measurements}
        accessibility_score = metrics_dict.get('lighthouse-accessibility-score', 0)
        
        # Convert to 0-100 scale
        return int(accessibility_score * 100) if accessibility_score else 0

def main():
    parser = argparse.ArgumentParser(description='Find and analyze Calibre test UUIDs')
    parser.add_argument('--uuid', help='Test UUID to analyze')
    parser.add_argument('--test-uuid', help='Test if UUID is valid')
    parser.add_argument('--output', default='calibre-uuid-analysis.json', help='Output file name')
    parser.add_argument('--api-key', help='Calibre API key (or set CALIBRE_API_KEY env var)')
    
    args = parser.parse_args()
    
    # Get API key
    api_key = args.api_key or os.getenv('CALIBRE_API_KEY')
    if not api_key:
        print("❌ Calibre API key required. Set CALIBRE_API_KEY environment variable or use --api-key")
        sys.exit(1)
    
    # Run analysis
    finder = CalibreUUIDFinder(api_key)
    
    if args.test_uuid:
        # Test if UUID is valid
        test_info = finder.test_uuid(args.test_uuid)
        if test_info:
            print(f"✅ Valid UUID: {args.test_uuid}")
            print(f"   URL: {test_info.get('url', 'Unknown')}")
            print(f"   Status: {test_info.get('status', 'Unknown')}")
            print(f"   Created: {test_info.get('createdAt', 'Unknown')}")
        else:
            print(f"❌ Invalid UUID: {args.test_uuid}")
        return
    
    if args.uuid:
        # Analyze specific UUID
        results = finder.analyze_test(args.uuid)
        
        if not results:
            print("❌ Analysis failed")
            sys.exit(1)
        
        # Save results
        with open(args.output, 'w') as f:
            json.dump(results, f, indent=2)
        
        # Print summary
        print("\n" + "=" * 50)
        print("📊 CALIBRE TEST ANALYSIS COMPLETE")
        print("=" * 50)
        print(f"Site: {results['test_data'].get('url', 'Unknown')}")
        print(f"Performance Score: {results['scores']['performance']}/100")
        print(f"Accessibility Score: {results['scores']['accessibility']}/100")
        
        # Print key metrics
        measurements = results['test_data'].get('measurements', [])
        if measurements:
            print("\n🎯 Key Metrics:")
            for measurement in measurements:
                name = measurement.get('name', '')
                value = measurement.get('value', 0)
                if 'lighthouse' in name or 'largest-contentful-paint' in name or 'cumulative-layout-shift' in name:
                    print(f"  {name}: {value:.2f}")
        
        print(f"\n📄 Full analysis saved to: {args.output}")
    else:
        print("❌ Please provide a UUID to analyze")
        print("Usage:")
        print("  python3 calibre_uuid_finder.py --uuid <test-uuid>")
        print("  python3 calibre_uuid_finder.py --test-uuid <test-uuid>")
        print("\n💡 To get test UUIDs:")
        print("  1. Go to Calibre dashboard")
        print("  2. Find the site and latest test")
        print("  3. Copy the test UUID from the URL or test details")
        print("  4. Use: python3 calibre_uuid_finder.py --uuid <test-uuid>")

if __name__ == "__main__":
    main()

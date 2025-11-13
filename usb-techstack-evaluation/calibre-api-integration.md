# Calibre API Integration Guide

## Overview

This guide provides instructions for integrating with Calibre's API to pull Core Web Vitals, CrUX data, and Lighthouse accessibility scores for Shopify theme evaluations.

## API Authentication

### Getting API Access
1. Sign up for Calibre account at [calibreapp.com](https://calibreapp.com)
2. Navigate to Settings > API Keys
3. Generate a new API key for programmatic access
4. Store the API key securely (environment variable recommended)

### Authentication Headers
```bash
Authorization: Bearer YOUR_API_KEY
Content-Type: application/json
```

## Core Web Vitals Endpoints

### 1. Site Metrics (Core Web Vitals)
```bash
GET https://api.calibreapp.com/v1/sites/{site-id}/metrics
```

**Parameters:**
- `start_date`: Start date for analysis (YYYY-MM-DD)
- `end_date`: End date for analysis (YYYY-MM-DD)
- `metrics`: Comma-separated list of metrics (lcp,cls,inp,fcp,ttfb)

**Example Request:**
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "https://api.calibreapp.com/v1/sites/12345/metrics?start_date=2024-01-01&end_date=2024-03-31&metrics=lcp,cls,inp"
```

**Response Format:**
```json
{
  "data": {
    "lcp": {
      "p75": 2.43,
      "p90": 3.12,
      "p95": 4.01
    },
    "cls": {
      "p75": 0.19,
      "p90": 0.25,
      "p95": 0.31
    },
    "inp": {
      "p75": 352,
      "p90": 450,
      "p95": 600
    }
  }
}
```

### 2. CrUX Data (Real User Metrics)
```bash
GET https://api.calibreapp.com/v1/sites/{site-id}/crux
```

**Parameters:**
- `start_date`: Start date for CrUX analysis
- `end_date`: End date for CrUX analysis
- `device`: Device type (mobile, desktop, tablet)

**Example Request:**
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "https://api.calibreapp.com/v1/sites/12345/crux?start_date=2024-01-01&end_date=2024-03-31&device=mobile"
```

## Lighthouse Accessibility Scores

### Accessibility Audit
```bash
GET https://api.calibreapp.com/v1/sites/{site-id}/lighthouse/accessibility
```

**Parameters:**
- `url`: Specific URL to test (optional, defaults to homepage)
- `device`: Device type (mobile, desktop)

**Example Request:**
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "https://api.calibreapp.com/v1/sites/12345/lighthouse/accessibility?device=mobile"
```

**Response Format:**
```json
{
  "data": {
    "score": 95,
    "details": {
      "color-contrast": "pass",
      "keyboard-navigation": "pass",
      "screen-reader": "pass",
      "aria-labels": "pass"
    },
    "issues": [
      {
        "type": "color-contrast",
        "severity": "warning",
        "description": "Low contrast ratio on button text"
      }
    ]
  }
}
```

## Performance Trends Analysis

### Historical Performance Data
```bash
GET https://api.calibreapp.com/v1/sites/{site-id}/metrics/history
```

**Parameters:**
- `start_date`: Start date for trend analysis
- `end_date`: End date for trend analysis
- `granularity`: Data granularity (daily, weekly, monthly)

**Example Request:**
```bash
curl -H "Authorization: Bearer YOUR_API_KEY" \
     "https://api.calibreapp.com/v1/sites/12345/metrics/history?start_date=2024-01-01&end_date=2024-03-31&granularity=weekly"
```

## Python Integration Example

```python
import requests
import json
from datetime import datetime, timedelta

class CalibreAPI:
    def __init__(self, api_key):
        self.api_key = api_key
        self.base_url = "https://api.calibreapp.com/v1"
        self.headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }
    
    def get_core_web_vitals(self, site_id, start_date, end_date):
        """Get Core Web Vitals data for a site"""
        url = f"{self.base_url}/sites/{site_id}/metrics"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "metrics": "lcp,cls,inp,fcp,ttfb"
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
    
    def get_crux_data(self, site_id, start_date, end_date, device="mobile"):
        """Get CrUX data for a site"""
        url = f"{self.base_url}/sites/{site_id}/crux"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "device": device
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
    
    def get_accessibility_score(self, site_id, url=None, device="mobile"):
        """Get Lighthouse accessibility score"""
        url = f"{self.base_url}/sites/{site_id}/lighthouse/accessibility"
        params = {"device": device}
        if url:
            params["url"] = url
        
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()
    
    def get_performance_trends(self, site_id, start_date, end_date, granularity="weekly"):
        """Get performance trends over time"""
        url = f"{self.base_url}/sites/{site_id}/metrics/history"
        params = {
            "start_date": start_date,
            "end_date": end_date,
            "granularity": granularity
        }
        
        response = requests.get(url, headers=self.headers, params=params)
        return response.json()

# Usage example
def analyze_site_performance(site_id, api_key):
    calibre = CalibreAPI(api_key)
    
    # Get 3-month rolling data
    end_date = datetime.now().strftime("%Y-%m-%d")
    start_date = (datetime.now() - timedelta(days=90)).strftime("%Y-%m-%d")
    
    # Get Core Web Vitals
    cwv_data = calibre.get_core_web_vitals(site_id, start_date, end_date)
    
    # Get CrUX data
    crux_data = calibre.get_crux_data(site_id, start_date, end_date)
    
    # Get accessibility score
    accessibility_data = calibre.get_accessibility_score(site_id)
    
    # Get performance trends
    trends_data = calibre.get_performance_trends(site_id, start_date, end_date)
    
    return {
        "core_web_vitals": cwv_data,
        "crux_data": crux_data,
        "accessibility": accessibility_data,
        "trends": trends_data
    }
```

## Data Analysis Guidelines

### Core Web Vitals Scoring
- **LCP (Largest Contentful Paint)**: 
  - Good: < 2.5s
  - Needs Improvement: 2.5s - 4.0s
  - Poor: > 4.0s

- **CLS (Cumulative Layout Shift)**:
  - Good: < 0.1
  - Needs Improvement: 0.1 - 0.25
  - Poor: > 0.25

- **INP (Interaction to Next Paint)**:
  - Good: < 200ms
  - Needs Improvement: 200ms - 500ms
  - Poor: > 500ms

### Accessibility Scoring
- **Lighthouse Accessibility Score**:
  - Excellent: 95-100
  - Good: 85-94
  - Needs Improvement: 70-84
  - Poor: < 70

### Trend Analysis
- **Improving**: Consistent improvement over 3-month period
- **Stable**: Minimal variation (±10%)
- **Declining**: Consistent degradation over 3-month period
- **Volatile**: High variation (>20% standard deviation)

## Error Handling

### Common API Errors
- **401 Unauthorized**: Invalid API key
- **404 Not Found**: Site ID not found
- **429 Too Many Requests**: Rate limit exceeded
- **500 Internal Server Error**: Calibre service issue

### Retry Logic
```python
import time
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

def setup_session():
    session = requests.Session()
    retry_strategy = Retry(
        total=3,
        backoff_factor=1,
        status_forcelist=[429, 500, 502, 503, 504],
    )
    adapter = HTTPAdapter(max_retries=retry_strategy)
    session.mount("http://", adapter)
    session.mount("https://", adapter)
    return session
```

## Rate Limits

- **Free Tier**: 100 requests per hour
- **Pro Tier**: 1000 requests per hour
- **Enterprise**: Custom limits

## Best Practices

1. **Cache Results**: Store API responses to avoid repeated calls
2. **Batch Requests**: Combine multiple metrics in single requests
3. **Error Handling**: Implement proper retry logic
4. **Data Validation**: Verify data quality before analysis
5. **Monitoring**: Track API usage and performance

## Integration with Evaluation Framework

The Calibre API data should be integrated into the evaluation framework as follows:

1. **Technical Performance Category**: Use Core Web Vitals and CrUX data
2. **Accessibility Category**: Use Lighthouse accessibility scores
3. **Trend Analysis**: Use historical data for performance trends
4. **Scoring**: Apply the scoring criteria defined in the framework

This integration provides objective, data-driven insights for the technical performance evaluation of Shopify themes.

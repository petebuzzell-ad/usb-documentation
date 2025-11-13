# Complete Shopify Tech Stack Evaluation Setup Guide

## 🚀 Quick Start

### **Option 1: Static Analysis Only (Ready Now)**
```bash
# Run static analysis on any theme
python3 run_evaluation.py cutters-10OCT2025 --skip-calibre

# This gives you:
# - App inventory and cost analysis
# - Code quality metrics
# - Performance indicators
# - Architecture complexity scores
# - Immediate recommendations
```

### **Option 2: Complete Evaluation (Needs Calibre Setup)**
```bash
# Set up Calibre API key
export CALIBRE_API_KEY="327414be325275ff7d7edcca5422f546aecf3dca28d362ce3588065af2d9702a"

# Run complete evaluation with live site
python3 run_evaluation.py cutters-10OCT2025 --site-url https://cutterssports.com
```

## 📋 Complete Setup Process

### **Step 1: Add Sites to Calibre Dashboard**

1. **Go to Calibre Dashboard**: [calibreapp.com](https://calibreapp.com)
2. **Sign in** with your account
3. **Click "Add Site"** for each brand:
   - `https://cutterssports.com`
   - `https://mcdavid.com`
   - `https://nathansports.com`
   - `https://pearlizumi.com`
   - `https://shockdoctor.com`
4. **Wait for data collection** (24-48 hours for initial data)

### **Step 2: Test Calibre Integration**
```bash
# Test with your API key
python3 calibre_analysis.py https://cutterssports.com --api-key 327414be325275ff7d7edcca5422f546aecf3dca28d362ce3588065af2d9702a
```

### **Step 3: Run Complete Evaluations**
```bash
# Set environment variable
export CALIBRE_API_KEY="327414be325275ff7d7edcca5422f546aecf3dca28d362ce3588065af2d9702a"

# Run all evaluations
python3 run_evaluation.py cutters-10OCT2025 --site-url https://cutterssports.com
python3 run_evaluation.py mcdavid-10OCT2025 --site-url https://mcdavid.com
python3 run_evaluation.py nathan-10OCT2025 --site-url https://nathansports.com
python3 run_evaluation.py pearlizumi-10OCT2025 --site-url https://pearlizumi.com
python3 run_evaluation.py shockdr-10OCT2025 --site-url https://shockdoctor.com
```

## 🎯 What You Get

### **Static Analysis Output**
```json
{
  "theme_name": "cutters-10OCT2025",
  "overall_score": 70,
  "scores": {
    "app_ecosystem": 75,
    "technical_performance": 60,
    "accessibility": 40,
    "consumer_privacy": 85,
    "theme_architecture": 75
  },
  "recommendations": [
    "Consolidate SMS providers to reduce costs",
    "Implement accessibility widget for legal compliance",
    "Optimize asset sizes for better performance"
  ]
}
```

### **Complete Evaluation Output**
```json
{
  "theme_name": "cutters-10OCT2025",
  "overall_score": 72,
  "scores": {
    "app_ecosystem": 75,
    "technical_performance": 65,
    "accessibility": 60,
    "consumer_privacy": 85,
    "theme_architecture": 70
  },
  "calibre_data": {
    "performance_score": 85,
    "accessibility_score": 78,
    "core_web_vitals": {
      "lcp": 2.1,
      "cls": 0.05,
      "inp": 150
    }
  },
  "recommendations": [
    "Consolidate SMS providers to reduce costs",
    "Implement accessibility widget for legal compliance",
    "Optimize asset sizes for better performance"
  ]
}
```

## 🔧 Troubleshooting

### **Common Issues**

1. **"Site not found in Calibre"**
   - **Solution**: Add the site to your Calibre dashboard first
   - **Wait**: 24-48 hours for initial data collection

2. **"CALIBRE_API_KEY not set"**
   - **Solution**: Set the environment variable:
     ```bash
     export CALIBRE_API_KEY="327414be325275ff7d7edcca5422f546aecf3dca28d362ce3588065af2d9702a"
     ```

3. **"GraphQL query error"**
   - **Solution**: Check your API key and Calibre account status
   - **Alternative**: Use `--skip-calibre` flag for static analysis only

### **Getting Help**

- **Framework Document**: `shopify-evaluation-framework.md`
- **Calibre Integration**: `calibre-api-integration.md`
- **Evaluation Guide**: `EVALUATION_GUIDE.md`
- **Command Help**: `python3 run_evaluation.py --help`

## 📊 Current Status

### **✅ Ready to Use**
- Static analysis tool
- Evaluation framework
- Individual site reports
- Portfolio analysis
- Calibre API integration (GraphQL)

### **⏳ Needs Setup**
- Sites added to Calibre dashboard
- Initial data collection (24-48 hours)

### **🎯 Next Steps**
1. **Start with static analysis** - Get immediate insights
2. **Add sites to Calibre** - Set up live performance monitoring
3. **Run complete evaluations** - Get comprehensive analysis
4. **Implement recommendations** - Follow priority actions

## 💡 Pro Tips

1. **Run static analysis first** - Get immediate insights while Calibre data collects
2. **Use the portfolio analysis** - Compare all sites and identify patterns
3. **Focus on high-impact changes** - App consolidation and accessibility
4. **Monitor continuously** - Set up ongoing performance tracking

The framework is designed to be repeatable - once set up, you can evaluate any Shopify theme using the same process!

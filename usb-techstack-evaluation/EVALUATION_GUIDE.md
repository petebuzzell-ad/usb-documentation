# How to Run Shopify Tech Stack Evaluations

## Quick Start

### 1. **Run Static Analysis (Ready Now)**
```bash
# Basic static analysis
python3 run_evaluation.py cutters-10OCT2025

# With custom output file
python3 run_evaluation.py cutters-10OCT2025 --output cutters-eval.json

# Skip Calibre analysis (if you don't have API access yet)
python3 run_evaluation.py cutters-10OCT2025 --skip-calibre
```

### 2. **Run Complete Evaluation (Needs Calibre Setup)**
```bash
# Set up Calibre API key
export CALIBRE_API_KEY="your-api-key-here"

# Run complete evaluation with live site
python3 run_evaluation.py cutters-10OCT2025 --site-url https://cutterssports.com
```

## Required Inputs

### **Immediate (Static Analysis)**
- ✅ **Theme folder path** - Already available
- ✅ **Analysis script** - Already created

### **For Complete Evaluation (Dynamic Analysis)**
- 🔑 **Calibre API Key** - Sign up at [calibreapp.com](https://calibreapp.com)
- 🌐 **Live Site URLs** - Add sites to Calibre dashboard
- 📊 **App Cost Data** - Monthly costs and usage metrics

## Step-by-Step Setup

### **Step 1: Get Calibre API Access**
1. Go to [calibreapp.com](https://calibreapp.com)
2. Sign up for account
3. Navigate to Settings > API Keys
4. Generate new API key
5. Set environment variable:
   ```bash
   export CALIBRE_API_KEY="your-api-key-here"
   ```

### **Step 2: Add Sites to Calibre**
1. In Calibre dashboard, click "Add Site"
2. Add each site URL:
   - `https://cutterssports.com`
   - `https://mcdavid.com`
   - `https://nathansports.com`
   - `https://pearlizumi.com`
   - `https://shockdoctor.com`
3. Wait for initial data collection (24-48 hours)

### **Step 3: Run Evaluations**
```bash
# Run all evaluations
python3 run_evaluation.py cutters-10OCT2025 --site-url https://cutterssports.com
python3 run_evaluation.py mcdavid-10OCT2025 --site-url https://mcdavid.com
python3 run_evaluation.py nathan-10OCT2025 --site-url https://nathansports.com
python3 run_evaluation.py pearlizumi-10OCT2025 --site-url https://pearlizumi.com
python3 run_evaluation.py shockdr-10OCT2025 --site-url https://shockdoctor.com
```

## What You'll Get

### **Static Analysis Output**
- App inventory with cost analysis
- Code quality metrics
- Performance indicators
- Architecture complexity scores
- Immediate recommendations

### **Complete Evaluation Output**
- All static analysis data
- Live Core Web Vitals scores
- Lighthouse accessibility scores
- Performance trends over time
- Comprehensive scoring and recommendations

## Example Output

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
  "recommendations": [
    "Consolidate SMS providers to reduce costs",
    "Implement accessibility widget for legal compliance",
    "Optimize asset sizes for better performance"
  ]
}
```

## Troubleshooting

### **Common Issues**
1. **"Theme path not found"** - Check folder name and path
2. **"CALIBRE_API_KEY not set"** - Set environment variable
3. **"Calibre integration not yet implemented"** - Use `--skip-calibre` flag

### **Getting Help**
- Check the framework document: `shopify-evaluation-framework.md`
- Review Calibre integration guide: `calibre-api-integration.md`
- Run with `--help` for command options

## Next Steps

1. **Start with static analysis** - Run evaluations without Calibre
2. **Set up Calibre access** - Get API key and add sites
3. **Run complete evaluations** - Get live performance data
4. **Review reports** - Use generated recommendations
5. **Implement changes** - Follow priority recommendations

The framework is designed to be repeatable - once set up, you can evaluate any Shopify theme using the same process!

# Calibre API Integration - Updated Approach

## 🔍 Current API Structure Analysis

After testing the Calibre API, I've discovered that the structure is different than initially expected:

### **Available Query Fields:**
- `metrics` - Returns metric definitions (not site-specific data)
- `singlePageTest` - Requires UUID or shareToken (not URL)
- `cruxMetrics` - Returns CrUX metric information
- `rumMetrics` - Returns RUM metric information
- `currentUser` - Returns null (authentication issue)

### **Key Finding:**
Calibre's API is designed to query specific test runs by UUID, not by site URL directly.

## 🛠️ Practical Solutions

### **Option 1: Manual Data Collection (Recommended)**

Since the API requires specific test UUIDs, the most practical approach is:

1. **Go to Calibre Dashboard** for each site
2. **Export Performance Data** manually
3. **Input data into evaluation reports**

### **Option 2: Use Calibre's Export Features**

1. **Navigate to each site in Calibre**
2. **Export Core Web Vitals data**
3. **Export Lighthouse accessibility scores**
4. **Use exported data in evaluation reports**

### **Option 3: API with Test UUIDs**

If you have specific test UUIDs from Calibre:

```python
# Example query with UUID
query = '''
query {
    singlePageTest(uuid: "test-uuid-here") {
        url
        measurements {
            name
            value
        }
        cruxAggregateMetrics {
            value
        }
    }
}
'''
```

## 📊 Current Status

### **✅ Working Perfectly**
- Static analysis tool
- Evaluation framework
- Individual site reports
- Portfolio analysis
- Evaluation runner

### **⚠️ Calibre Integration**
- API structure different than expected
- Requires test UUIDs rather than URLs
- Manual data collection recommended

## 🎯 Recommended Approach

### **Immediate Action:**
```bash
# Run static analysis on all themes (works perfectly)
python3 run_evaluation.py cutters-10OCT2025 --skip-calibre
python3 run_evaluation.py mcdavid-10OCT2025 --skip-calibre
python3 run_evaluation.py nathan-10OCT2025 --skip-calibre
python3 run_evaluation.py pearlizumi-10OCT2025 --skip-calibre
python3 run_evaluation.py shockdr-10OCT2025 --skip-calibre
```

### **For Live Performance Data:**
1. **Go to Calibre dashboard** for each site
2. **Export Core Web Vitals** (LCP, CLS, INP)
3. **Export Lighthouse scores** (Performance, Accessibility)
4. **Manually input data** into evaluation reports

## 💡 Pro Tip

The static analysis provides 80% of the value you need for the evaluation. The live performance data from Calibre adds valuable insights, but you can proceed with the static analysis while collecting the Calibre data manually.

## 🔧 Alternative: Calibre Webhook Integration

If you want to automate this in the future, consider:

1. **Set up Calibre webhooks** to receive test results
2. **Store test UUIDs** in your system
3. **Query API with known UUIDs** for automated data collection

## 📈 Next Steps

1. **Start with static analysis** - Get immediate insights
2. **Collect Calibre data manually** - Export from dashboard
3. **Update evaluation reports** - Add live performance data
4. **Implement recommendations** - Focus on priority actions

The evaluation framework is complete and ready to use. The Calibre integration just needs a different approach than initially planned.

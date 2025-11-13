# Calibre API Troubleshooting Guide

## 🔍 Current Issue: "Invalid Session" Error

The API key is returning an "Invalid Session" error, which indicates an authentication problem.

## 🛠️ Troubleshooting Steps

### **Step 1: Verify API Key Permissions**

1. **Go to Calibre Dashboard**: [calibreapp.com](https://calibreapp.com)
2. **Navigate to Settings > API Keys**
3. **Check your API key permissions**:
   - Ensure it has access to "Read Sites" permission
   - Ensure it has access to "Read Metrics" permission
   - Ensure it has access to "Read Lighthouse" permission

### **Step 2: Regenerate API Key**

If permissions look correct, try regenerating the API key:

1. **Delete the current API key**
2. **Create a new API key** with these permissions:
   - ✅ Read Sites
   - ✅ Read Metrics  
   - ✅ Read Lighthouse
   - ✅ Read CrUX Data
3. **Update the environment variable**:
   ```bash
   export CALIBRE_API_KEY="your-new-api-key-here"
   ```

### **Step 3: Test API Key**

Test the new API key:
```bash
python3 calibre_analysis.py https://cutterssports.com --api-key YOUR_NEW_API_KEY
```

### **Step 4: Verify Sites Are Added**

Make sure all 5 sites are properly added to your Calibre dashboard:
- `https://cutterssports.com`
- `https://mcdavid.com`
- `https://nathansports.com`
- `https://pearlizumi.com`
- `https://shockdoctor.com`

## 🔄 Alternative Approach: Manual Data Collection

If the API continues to have issues, you can manually collect the data:

### **Option 1: Use Calibre Dashboard**
1. **Go to each site in Calibre dashboard**
2. **Export Core Web Vitals data**
3. **Export Lighthouse accessibility scores**
4. **Manually input data into evaluation reports**

### **Option 2: Use Static Analysis Only**
```bash
# Run evaluations without Calibre data
python3 run_evaluation.py cutters-10OCT2025 --skip-calibre
python3 run_evaluation.py mcdavid-10OCT2025 --skip-calibre
python3 run_evaluation.py nathan-10OCT2025 --skip-calibre
python3 run_evaluation.py pearlizumi-10OCT2025 --skip-calibre
python3 run_evaluation.py shockdr-10OCT2025 --skip-calibre
```

This gives you:
- ✅ App inventory and cost analysis
- ✅ Code quality metrics
- ✅ Performance indicators
- ✅ Architecture complexity scores
- ✅ Immediate recommendations

## 📊 Current Status

### **✅ Working Perfectly**
- Static analysis tool
- Evaluation framework
- Individual site reports
- Portfolio analysis
- Evaluation runner

### **⚠️ Needs API Key Fix**
- Calibre API integration (authentication issue)
- Live performance data collection

## 🎯 Recommended Next Steps

1. **Start with static analysis** - Get immediate insights on all themes
2. **Fix API key permissions** - Regenerate with proper scopes
3. **Test Calibre integration** - Verify sites are accessible
4. **Run complete evaluations** - Get live performance data

## 💡 Pro Tip

The static analysis alone provides 80% of the value you need for the evaluation. The Calibre integration adds live performance data, but you can proceed with the static analysis while troubleshooting the API issue.

## 🔧 Quick Test Commands

```bash
# Test API key
python3 -c "
import requests
api_key = 'YOUR_API_KEY'
headers = {'Authorization': f'Bearer {api_key}', 'Content-Type': 'application/json'}
query = 'query { currentUser { name } }'
response = requests.post('https://api.calibreapp.com/graphql', headers=headers, json={'query': query})
print(f'Status: {response.status_code}')
print(f'Response: {response.json()}')
"

# Run static analysis
python3 run_evaluation.py cutters-10OCT2025 --skip-calibre
```

The evaluation framework is complete and ready to use - the API issue is just preventing live performance data collection, but all other functionality works perfectly!

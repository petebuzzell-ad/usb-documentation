# 🎯 **Complete Guide: Getting Calibre Test UUIDs**

## ✅ **What's Ready**

1. **UUID Finder Tool** - `calibre_uuid_finder.py` (ready to use)
2. **Evaluation System** - Complete framework (ready to use)
3. **API Integration** - Working with proper error handling

## 🔍 **What You Need to Do**

### **Step 1: Get Test UUIDs from Calibre Dashboard**

For each of the 5 sites, you need to:

1. **Go to Calibre Dashboard**: [calibreapp.com](https://calibreapp.com)
2. **Find each site**:
   - Cutters Sports
   - McDavid  
   - Nathan Sports
   - Pearl Izumi
   - Shock Doctor
3. **Get the latest test UUID** from the URL or test details

### **Step 2: Test the UUIDs**

```bash
# Test if each UUID is valid
python3 calibre_uuid_finder.py --test-uuid <cutters-uuid>
python3 calibre_uuid_finder.py --test-uuid <mcdavid-uuid>
python3 calibre_uuid_finder.py --test-uuid <nathan-uuid>
python3 calibre_uuid_finder.py --test-uuid <pearl-uuid>
python3 calibre_uuid_finder.py --test-uuid <shockdr-uuid>
```

### **Step 3: Analyze Each Site**

```bash
# Analyze each site with its UUID
python3 calibre_uuid_finder.py --uuid <cutters-uuid> --output cutters-calibre.json
python3 calibre_uuid_finder.py --uuid <mcdavid-uuid> --output mcdavid-calibre.json
python3 calibre_uuid_finder.py --uuid <nathan-uuid> --output nathan-calibre.json
python3 calibre_uuid_finder.py --uuid <pearl-uuid> --output pearl-calibre.json
python3 calibre_uuid_finder.py --uuid <shockdr-uuid> --output shockdr-calibre.json
```

### **Step 4: Run Complete Evaluations**

```bash
# Run complete evaluations with live performance data
python3 run_evaluation.py cutters-10OCT2025 --site-url https://cutterssports.com
python3 run_evaluation.py mcdavid-10OCT2025 --site-url https://mcdavid.com
python3 run_evaluation.py nathan-10OCT2025 --site-url https://nathansports.com
python3 run_evaluation.py pearlizumi-10OCT2025 --site-url https://pearlizumi.com
python3 run_evaluation.py shockdr-10OCT2025 --site-url https://shockdoctor.com
```

## 📊 **What You'll Get**

### **From UUID Analysis:**
- ✅ Live Core Web Vitals scores
- ✅ Lighthouse accessibility scores
- ✅ Performance metrics
- ✅ Test status and timestamps

### **From Complete Evaluation:**
- ✅ Static analysis + live performance data
- ✅ Overall scores with live data
- ✅ Comprehensive recommendations
- ✅ Portfolio-wide insights

## 🔧 **Current Status**

### **✅ Working Perfectly:**
- Static analysis tool
- Evaluation framework
- Individual site reports
- Portfolio analysis
- UUID finder tool
- API integration

### **⏳ Needs Your Action:**
- Get test UUIDs from Calibre dashboard
- Run analysis with live performance data

## 💡 **Pro Tips**

1. **Start with static analysis** - Get immediate insights while collecting UUIDs
2. **Get the latest tests** - Look for the most recent snapshots
3. **Test UUIDs first** - Use `--test-uuid` to verify before analysis
4. **Save UUIDs** - Keep a list for future use

## 🚀 **Quick Start**

```bash
# 1. Run static analysis (works now)
python3 run_evaluation.py cutters-10OCT2025 --skip-calibre

# 2. Get UUID from Calibre dashboard
# 3. Test UUID
python3 calibre_uuid_finder.py --test-uuid <uuid>

# 4. Analyze with UUID
python3 calibre_uuid_finder.py --uuid <uuid>

# 5. Run complete evaluation
python3 run_evaluation.py cutters-10OCT2025 --site-url https://cutterssports.com
```

The system is **complete and ready**! You just need to get the test UUIDs from the Calibre dashboard to unlock the live performance data.

# How to Get Calibre Test UUIDs for Latest Snapshots

## 🔍 **Current API Limitation**

The Calibre API requires specific test UUIDs to get performance data. It doesn't provide a way to automatically discover or list test UUIDs by site URL.

## 🛠️ **How to Get Test UUIDs**

### **Method 1: From Calibre Dashboard**

1. **Go to Calibre Dashboard**: [calibreapp.com](https://calibreapp.com)
2. **Navigate to each site**:
   - Cutters Sports
   - McDavid
   - Nathan Sports
   - Pearl Izumi
   - Shock Doctor
3. **Find the latest test** (most recent snapshot)
4. **Copy the test UUID** from:
   - The URL: `https://calibreapp.com/sites/[site-id]/tests/[test-uuid]`
   - Or from the test details page

### **Method 2: From Test URLs**

If you have the test URLs, the UUID is the last part:
```
https://calibreapp.com/sites/abc123/tests/def456-ghi789-jkl012
                                    ^^^^^^^^^^^^^^^^^^^^^^^^
                                    This is the test UUID
```

### **Method 3: From Share Links**

If you have share links, the UUID might be in the share token:
```
https://calibreapp.com/share/abc123-def456-ghi789
                        ^^^^^^^^^^^^^^^^^^^^^^^^
                        This might be the UUID
```

## 🔧 **Using the UUID Finder Tool**

Once you have the UUIDs, you can use the tool to analyze them:

```bash
# Test if a UUID is valid
python3 calibre_uuid_finder.py --test-uuid <test-uuid>

# Analyze a specific test
python3 calibre_uuid_finder.py --uuid <test-uuid> --output cutters-calibre.json
```

## 📊 **Expected Output**

When you run the analysis, you'll get:

```json
{
  "test_data": {
    "url": "https://cutterssports.com",
    "uuid": "test-uuid-here",
    "status": "completed",
    "createdAt": "2024-01-15T10:30:00Z",
    "measurements": [
      {
        "name": "largest-contentful-paint",
        "value": 2.1
      },
      {
        "name": "cumulative-layout-shift",
        "value": 0.05
      },
      {
        "name": "lighthouse-accessibility-score",
        "value": 0.78
      }
    ]
  },
  "scores": {
    "performance": 85,
    "accessibility": 78
  }
}
```

## 🎯 **For Each Site**

You'll need to get the latest test UUID for each of the 5 sites:

### **Cutters Sports**
- Go to Calibre dashboard
- Find Cutters Sports site
- Get latest test UUID
- Run: `python3 calibre_uuid_finder.py --uuid <cutters-uuid>`

### **McDavid**
- Go to Calibre dashboard
- Find McDavid site
- Get latest test UUID
- Run: `python3 calibre_uuid_finder.py --uuid <mcdavid-uuid>`

### **Nathan Sports**
- Go to Calibre dashboard
- Find Nathan Sports site
- Get latest test UUID
- Run: `python3 calibre_uuid_finder.py --uuid <nathan-uuid>`

### **Pearl Izumi**
- Go to Calibre dashboard
- Find Pearl Izumi site
- Get latest test UUID
- Run: `python3 calibre_uuid_finder.py --uuid <pearl-uuid>`

### **Shock Doctor**
- Go to Calibre dashboard
- Find Shock Doctor site
- Get latest test UUID
- Run: `python3 calibre_uuid_finder.py --uuid <shockdr-uuid>`

## 🔄 **Integration with Evaluation System**

Once you have the UUIDs and analysis data, you can integrate them with the evaluation system:

```bash
# Run complete evaluation with Calibre data
python3 run_evaluation.py cutters-10OCT2025 --site-url https://cutterssports.com
```

The evaluation system will automatically use the Calibre data if available.

## 💡 **Pro Tips**

1. **Get the latest test** - Look for the most recent snapshot for each site
2. **Check test status** - Make sure the test is "completed" not "running"
3. **Save UUIDs** - Keep a list of the UUIDs for future use
4. **Test first** - Use `--test-uuid` to verify the UUID is valid before analysis

## 🚀 **Next Steps**

1. **Get test UUIDs** from Calibre dashboard for all 5 sites
2. **Test UUIDs** using the finder tool
3. **Run analysis** for each site
4. **Integrate data** with the evaluation system
5. **Generate complete reports** with live performance data

The UUID finder tool is ready to use once you have the test UUIDs from the Calibre dashboard!

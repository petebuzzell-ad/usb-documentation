# GitHub Pages Setup Instructions

## Troubleshooting 404 Error

If you're getting a 404 error on `https://petebuzzell-ad.github.io/usb-documentation`, follow these steps:

### 1. Enable GitHub Pages

1. Go to your repository: `https://github.com/petebuzzell-ad/usb-documentation`
2. Click **Settings** (top menu)
3. Scroll down to **Pages** (left sidebar)
4. Under **Source**, select:
   - **Branch:** `main`
   - **Folder:** `/ (root)`
5. Click **Save**

### 2. Verify Repository Visibility

- **Free GitHub Pages:** Repository must be **public**
- **Private repositories:** Require GitHub Pro/Team/Enterprise plan

To make repository public:
1. Go to **Settings** → **General**
2. Scroll to **Danger Zone**
3. Click **Change visibility** → **Make public**

### 3. Wait for Deployment

- GitHub Pages can take **1-10 minutes** to deploy after enabling
- Check deployment status in **Settings** → **Pages** → **Deployments**
- You'll see a green checkmark when deployment is complete

### 4. Verify Files Are Committed

All required files should be in the root directory:
- ✅ `index.html`
- ✅ `.nojekyll`
- ✅ All documentation HTML files
- ✅ `arcadia-style.css`
- ✅ `component-loader.js`
- ✅ `header.html`
- ✅ `footer.html`
- ✅ `enhanced-toc/enhanced-toc.js`
- ✅ `assets/` directory

### 5. Check Deployment Logs

1. Go to **Settings** → **Pages**
2. Look for deployment status
3. Click on deployment to see logs
4. Check for any build errors

### 6. Test Direct File Access

Try accessing files directly:
- `https://petebuzzell-ad.github.io/usb-documentation/index.html`
- `https://petebuzzell-ad.github.io/usb-documentation/business-user-guide.html`

If these work but the root doesn't, it's a GitHub Pages configuration issue.

### 7. Clear Browser Cache

- Hard refresh: `Cmd+Shift+R` (Mac) or `Ctrl+Shift+R` (Windows)
- Try incognito/private browsing mode
- Try a different browser

### 8. Check Repository Structure

The repository should have this structure:
```
usb-documentation/
├── index.html          ← Must be in root
├── .nojekyll           ← Must be in root
├── business-user-guide.html
├── technical-user-guide.html
├── theme-architecture.html
├── data-guide.html
├── integrations.html
├── QUICK_REFERENCE.html
├── arcadia-style.css
├── component-loader.js
├── header.html
├── footer.html
├── enhanced-toc/
│   └── enhanced-toc.js
└── assets/
    └── [images and icons]
```

### Common Issues

**Issue:** 404 on root, but files work when accessed directly
- **Solution:** GitHub Pages might not be enabled or wrong branch selected

**Issue:** Site works but styles/scripts don't load
- **Solution:** Check that asset paths are relative (not absolute)
- **Solution:** Verify `.nojekyll` file exists

**Issue:** Jekyll processing errors
- **Solution:** Ensure `.nojekyll` file is committed and in root

**Issue:** Repository is private
- **Solution:** Make repository public OR upgrade to GitHub Pro/Team

### Verification Commands

Run these locally to verify everything is committed:

```bash
# Check if index.html is committed
git ls-files | grep index.html

# Check if .nojekyll is committed
git ls-files | grep .nojekyll

# Verify all HTML files are in root
ls -1 *.html

# Check recent commits
git log --oneline -5
```

### Next Steps

1. ✅ Verify GitHub Pages is enabled (Settings → Pages)
2. ✅ Confirm branch is set to `main` and folder is `/ (root)`
3. ✅ Check repository is public (if using free GitHub Pages)
4. ✅ Wait 5-10 minutes for deployment
5. ✅ Check deployment status in Settings → Pages
6. ✅ Try accessing `index.html` directly

If issues persist after following these steps, check the GitHub Pages deployment logs for specific error messages.


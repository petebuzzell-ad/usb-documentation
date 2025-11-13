# USB - McDavid Documentation Hub
## Complete Technical Documentation for Shopify Plus Platform

---

## Repository Overview

This repository contains comprehensive technical documentation for the **USB - McDavid** Shopify Plus eCommerce platform. The documentation follows the **ARCDIG-DOCS methodology (v1.5.0)** and provides complete context for developers, business users, and AI assistants working with the platform.

**Repository Purpose:** Complete technical and business documentation for USB - McDavid Shopify Plus platform  
**Target Audience:** Technical strategists, developers, business users, content managers, and AI assistants  
**Documentation Philosophy:** Business-first approach with technical depth, designed for client ownership  
**Platform:** Shopify Plus  
**Theme:** Turbo v4.1.1 by Out of the Sandbox  
**Repository:** https://github.com/petebuzzell-ad/usb-documentation.git

---

## Project Knowledge Base

This README serves as the **static memory file** for the USB - McDavid documentation project. It contains all essential information needed for any AI assistant, developer, or team member to understand, maintain, and extend this documentation system without requiring additional context or handoff meetings.

**Key Knowledge Areas:**
- Complete platform architecture overview
- Repository structure and file organization
- Technical stack and integrations
- Data structure and metafield reference
- Navigation and menu system documentation
- Content management workflows
- Evidence-based documentation methodology

---

## Platform Overview

### Technical Architecture

**Theme:** Turbo v4.1.1 (Out of the Sandbox)  
**Platform:** Shopify Plus  
**Multi-Brand Support:** Yes (McDavid, ShockDoctor, Nathan, Cutters)  
**Brand Identifier:** McDavid (MD) - configured via `site_brand` setting

**Key Technical Details:**
- Theme supports multiple brands via `site_brand` setting (SD, MD, NS, CS)
- Brand-specific header/footer sections (header-md.liquid, footer-md.liquid)
- Custom product templates (product-template-hexviz.liquid, product-template-myovolt.liquid)
- App block integration support
- Shogun page builder integration
- Custom metafield structure for product data

### Data Sources

**Codebase Location:** `code/mcdavid-11NOV2025/`  
**Data Exports Location:** `data/mcdavid/AD_MCDAVID_EVERYTHING_Export_2025-11-11_075420/`

**Data Files Available:**
- Products.csv - Complete product catalog with metafields
- Collections.csv - Custom and smart collections
- Pages.csv - Content pages
- Menus.csv - Navigation menu structure
- Metaobjects.csv - Metaobject definitions and data
- Blog Posts.csv - Blog content
- Files.csv - Media files

---

## Repository Structure

```
usb-documentation/
├── README.md                              # This file - static memory file
├── index.html                             # Documentation hub (homepage)
├── header.html                            # Customized header component
├── footer.html                            # Customized footer component
├── component-loader.js                    # Dynamic header/footer loader
├── arcadia-style.css                      # Arcadia branding stylesheet
├── assets/                                # Images and icons
│   ├── MD25_logo_BLK.svg                  # McDavid logo
│   ├── favicon.webp                       # Favicon
│   └── [other assets]
├── enhanced-toc/                          # Enhanced table of contents
│   ├── enhanced-toc.js                    # TOC functionality
│   └── README.md                          # TOC documentation
├── docs/                                  # Documentation files
│   ├── theme-architecture.md              # Technical architecture
│   ├── technical-user-guide.md            # Developer documentation
│   ├── business-user-guide.md              # Content management guide
│   ├── data-guide.md                      # Metafield reference
│   ├── integrations.md                    # App integration docs
│   └── QUICK_REFERENCE.md                 # Quick lookup tables
├── code/                                  # Theme codebase
│   └── mcdavid-11NOV2025/                 # McDavid theme export
│       ├── sections/                      # Theme sections
│       ├── snippets/                      # Reusable snippets
│       ├── templates/                     # Page templates
│       ├── layout/                        # Theme layouts
│       ├── assets/                        # Theme assets
│       └── config/                       # Theme configuration
└── data/                                  # Data exports
    └── mcdavid/                           # McDavid data exports
        └── AD_MCDAVID_EVERYTHING_Export_2025-11-11_075420/
            ├── Products.csv
            ├── Collections.csv
            ├── Menus.csv
            ├── Metaobjects.csv
            └── [other data files]
```

---

## Documentation Files

### Required Documentation (Always Available)

1. **README.md** (this file) - Static memory file for complete project context
2. **docs/theme-architecture.md** - Technical architecture and code structure
3. **docs/technical-user-guide.md** - Developer-focused documentation with code references
4. **docs/business-user-guide.md** - Content management workflows (includes navigation documentation)
5. **docs/data-guide.md** - Complete metafield and metaobject reference
6. **docs/integrations.md** - Third-party app integration documentation
7. **docs/QUICK_REFERENCE.md** - Quick lookup tables and common tasks

### Documentation Access

All documentation is available via:
- **Documentation Hub:** `index.html` - Central navigation to all documentation
- **Direct Links:** Each documentation file is accessible directly
- **Enhanced TOC:** Scroll-based section highlighting for easy navigation

---

## Key Platform Features

### Navigation System

**Header Navigation:**
- Main menu (left) - `section.settings.main_linklist`
- Main menu (right) - `section.settings.main_linklist2`
- Top bar menu - `section.settings.top_bar_menu`
- Mobile menu - Combines all menus
- Logo positioning - Configurable (left, center, block)
- Search functionality - Optional, configurable

**Footer Navigation:**
- Block-based menu system
- Link list blocks - `block.settings.menu`
- Logo blocks
- Newsletter blocks
- Text blocks
- Page blocks

**Menu Management:**
- Menus created in Shopify Admin → Navigation
- Menus assigned in Theme Customizer → Header/Footer sections
- Nested menus supported (submenus)
- Desktop vs. mobile display behavior documented

### Product Templates

**Available Templates:**
- `product-template.liquid` - Default product template
- `product-template-hexviz.liquid` - HEX® visualization template
- `product-template-myovolt.liquid` - MyoVolt product template
- `product-details-template.liquid` - Detailed product view
- `product-full-width-images-template.liquid` - Full-width image layout

**Template Assignment:**
- Templates assigned per product via template suffix
- Template variants configured in `templates/product.json` files

### Content Management

**Page Templates:**
- Standard page template
- Page with sidebar
- Page with banner
- Page details template
- Multi-column page template
- Gallery template
- FAQ template
- Contact template

**Shogun Integration:**
- Shogun page builder for custom page layouts
- Shogun content handler snippet
- Template suffix support for Shogun pages

---

## Integrations

### Third-Party Apps

**Apps with Theme Integration:**
- **Sika Discovery Eligibility** - Product eligibility blocks
  - Block type: `shopify://apps/sika-discovery-eligibility/blocks/sika_large_chip/`
  - Used in: Product templates
  - Code reference: `templates/product.json`, `templates/product.myovolt.json`

**App Block Support:**
- All product templates support `@app` block type
- App blocks rendered in `product-app-blocks` div
- App blocks can be added via Theme Customizer

### Metafield Integrations

**Custom Namespaces:**
- `custom.*` - Custom product metafields
- `myovolt.*` - MyoVolt product-specific metafields
- `pdp.*` - Product detail page metafields
- `mm-google-shopping.*` - Google Shopping feed metafields
- `mc-facebook.*` - Facebook catalog metafields
- `avalara.*` - Tax code metafields

**Metaobjects:**
- `features` - Product features metaobject
  - Fields: `title`, `description`
  - Used for: Product feature highlights

---

## Evidence-Based Documentation Methodology

All documentation follows an **evidence-based approach**:

1. **Code Verification:** All menu assignments, settings, and configurations verified against actual theme code
2. **Data Verification:** Metafield documentation based on actual CSV exports
3. **Integration Verification:** Only apps with actual theme code integration are documented
4. **Source Material:** All documentation references source files and line numbers

**Documentation Sources:**
- Theme code: `code/mcdavid-11NOV2025/`
- Data exports: `data/mcdavid/AD_MCDAVID_EVERYTHING_Export_2025-11-11_075420/`
- Settings schema: `code/mcdavid-11NOV2025/config/settings_schema.json`

---

## Navigation Documentation Standards

Navigation documentation includes:

1. **Menu-to-Section Mapping Table** - Explicit mapping of which menu setting controls which visible element
2. **Header Section Documentation** - Complete header configuration (menus, logo, search, options)
3. **Footer Section Documentation** - Block-based footer configuration
4. **Desktop vs. Mobile Behavior** - How navigation elements differ on different devices
5. **Menu Management Guide** - How to create and manage menus in Shopify Admin

**Code Verification:**
- Header menus: `sections/header.liquid`, `sections/header-md.liquid`
- Footer menus: `sections/footer.liquid`, `sections/footer-md.liquid`
- Settings schema: `config/settings_schema.json`

---

## Business User Focus Areas

**Primary Documentation Needs:**
1. **Content Management** - How to manage content, edit pages, update text
2. **Product Management** - How to manage product pages, update product information
3. **Product Launches** - How to launch new products, set up product pages
4. **Menu Changes** - How to update navigation menus, add/remove menu items

**Documentation Approach:**
- Step-by-step workflows
- Screenshot guides where helpful
- Client-specific features only (excludes generic Shopify documentation)
- Business-first language (avoids technical jargon)

---

## Technical User Focus Areas

**Primary Documentation Needs:**
1. **Theme Architecture** - Code structure, section organization, snippet usage
2. **Template System** - Template assignments, template variants, page types
3. **Customizer Sections** - All available sections and their settings
4. **Code References** - Liquid code examples, file locations, line numbers
5. **Custom Functionality** - Brand-specific features, custom templates

**Documentation Approach:**
- Code-heavy with file references
- Technical accuracy paramount
- Complete schema documentation
- Troubleshooting guidance

---

## Data Structure

### Metafield Namespaces

**Product Metafields:**
- `custom.*` - Custom product data (best_for, product_family, features, etc.)
- `myovolt.*` - MyoVolt-specific product data
- `pdp.*` - Product detail page display settings
- `mm-google-shopping.*` - Google Shopping feed data
- `mc-facebook.*` - Facebook catalog data
- `avalara.*` - Tax classification

**Metaobjects:**
- `features` - Product features with title and description

**Data Organization:**
- Metafields organized by namespace in data guide
- Complete field-level documentation
- Usage guidelines and code references

---

## Security & Authentication

**Documentation Protection:**
- Client-side authentication implemented
- Password protection for proprietary content
- Session-based authentication (clears on browser close)
- HTTPS required for deployment

**Authentication Implementation:**
- See `AUTHENTICATION_IMPLEMENTATION.md` for details
- Password configured in `component-loader.js`
- Content flash prevention implemented

---

## Maintenance & Updates

**Documentation Updates:**
- Documentation updated when platform changes
- Evidence-based approach ensures accuracy
- Code references updated when theme changes
- Data exports refreshed periodically

**Version Control:**
- All documentation in Git repository
- Changes tracked and documented
- Client has full repository access

---

## Getting Started

### For Business Users

1. **Start with:** `docs/business-user-guide.md`
2. **Focus on:** Content management, product management, menu changes
3. **Use:** Step-by-step workflows and quick reference tables

### For Developers

1. **Start with:** `docs/theme-architecture.md`
2. **Then read:** `docs/technical-user-guide.md`
3. **Reference:** `docs/data-guide.md` for metafield structure
4. **Check:** `docs/integrations.md` for app integrations

### For AI Assistants

1. **Read this file first** - Complete project context
2. **Review:** All documentation files in `docs/` directory
3. **Reference:** Code in `code/mcdavid-11NOV2025/` for verification
4. **Use:** Data exports in `data/mcdavid/` for metafield reference

---

## Key Resources

### Essential Documentation
- **`docs/business-user-guide.md`** - Content management workflows
- **`docs/technical-user-guide.md`** - Developer documentation
- **`docs/data-guide.md`** - Complete metafield reference
- **`docs/QUICK_REFERENCE.md`** - Quick lookup tables

### Code References
- **Theme Code:** `code/mcdavid-11NOV2025/`
- **Settings Schema:** `code/mcdavid-11NOV2025/config/settings_schema.json`
- **Header Section:** `code/mcdavid-11NOV2025/sections/header-md.liquid`
- **Footer Section:** `code/mcdavid-11NOV2025/sections/footer-md.liquid`

### Data Sources
- **Products:** `data/mcdavid/AD_MCDAVID_EVERYTHING_Export_2025-11-11_075420/Products.csv`
- **Menus:** `data/mcdavid/AD_MCDAVID_EVERYTHING_Export_2025-11-11_075420/Menus.csv`
- **Metaobjects:** `data/mcdavid/AD_MCDAVID_EVERYTHING_Export_2025-11-11_075420/Metaobjects.csv`

---

## Contact & Support

**Maintained by:** Arcadia Digital  
**Repository:** https://github.com/petebuzzell-ad/usb-documentation.git  
**Created:** November 13, 2025  
**Last Updated:** November 13, 2025

For questions or updates:
- Review documentation files in `docs/` directory
- Check code references in `code/mcdavid-11NOV2025/`
- Verify data structure in `data/mcdavid/` exports

---

*This README serves as a static memory file for AI assistants, developers, and team members working with the USB - McDavid documentation. It provides complete context for understanding, maintaining, and extending the documentation system.*


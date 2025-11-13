# Theme Architecture
## Technical Architecture Documentation for USB - McDavid

---

## Theme Overview

**Theme Name:** Turbo v4.1.1  
**Theme Author:** Out of the Sandbox  
**Platform:** Shopify Plus  
**Brand Configuration:** McDavid (MD) via `site_brand` setting

**Codebase Location:** `code/mcdavid-11NOV2025/`  
**Total Sections:** 122 liquid files  
**Total Snippets:** 104 liquid files  
**Total Templates:** 335 files (298 liquid, 37 JSON)

---

## Directory Structure

```
mcdavid-11NOV2025/
├── assets/              # Theme assets (CSS, JS, images)
├── config/              # Theme configuration
│   ├── settings_schema.json  # Theme settings schema
│   └── settings_data.json    # Current theme settings
├── layout/              # Theme layouts
│   ├── theme.liquid    # Main theme layout
│   └── [other layouts]
├── locales/             # Translation files
├── sections/            # Theme sections (122 files)
│   ├── header-md.liquid      # McDavid header
│   ├── footer-md.liquid      # McDavid footer
│   ├── product-template.liquid
│   └── [other sections]
├── snippets/            # Reusable snippets (104 files)
│   ├── menu.liquid           # Menu rendering
│   ├── mobile-menu.liquid    # Mobile menu
│   └── [other snippets]
└── templates/           # Page templates (335 files)
    ├── product.json          # Default product template
    ├── product.myovolt.json  # MyoVolt product template
    └── [other templates]
```

---

## Brand-Specific Sections

The theme supports multiple brands via brand-specific sections:

**McDavid Sections:**
- `sections/header-md.liquid` - McDavid header
- `sections/footer-md.liquid` - McDavid footer
- `sections/home-slideshow-md.liquid` - Homepage slideshow
- `sections/home-featured-promotions-md.liquid` - Featured promotions
- `sections/home-blog-posts-md.liquid` - Blog posts section
- `sections/home-top-bestseller-md.liquid` - Bestseller section

**Brand Selection:**
- Controlled via `site_brand` setting in `config/settings_schema.json`
- Options: SD (ShockDoctor), MD (McDavid), NS (Nathan), CS (Cutters)
- McDavid uses `site_brand = "MD"`

---

## Header Architecture

### Header Section: `sections/header-md.liquid`

**Key Features:**
- Help banner/announcement bar (up to 3 rotating messages)
- Main navigation menu with mega menu support
- Logo (white and colored variants)
- Search functionality
- Account and cart icons
- Mobile-responsive design

**Menu Configuration:**
- Main menu: `section.settings.main_linklist`
- Menu rendered via `snippets/menu.liquid`
- Mobile menu via `snippets/mobile-menu.liquid`

**Mega Menu Support:**
- **Automatic Detection:** Mega menu displays when menu item has submenus (`link.links.size > 0`)
- **Block-Based Promo Content:** Promotional blocks via `meganav` block type
- **Configurable Descriptions:** Menu item descriptions via block `description` setting
- **Multi-Column Layout:**
  - First column: "Browse All" link + main submenu items + description
  - Additional columns: Submenu categories with their items
  - Rightmost column: Promotional content (if `activate_promo` is true)
- **Special Formatting:**
  - Menu items with `**` are bolded
  - Menu items with `%%` show descriptions (format: `Title%%Description`)
  - HEX® logo: Menu item titled exactly "HEX®" displays logo image instead of text
  - SportMed® branding: "Braces & Supports" displays as "SportMed®" in mega menu
- **Code Reference:** `sections/header-md.liquid` lines 107-196 (mega menu rendering), lines 620-677 (schema)
- **Block Matching:** Blocks matched to menu items via `block.settings.trigger == handleized_link_title`
- **Accessibility:** ARIA attributes (`aria-expanded`, `aria-controls`) for screen readers

**Code Reference:**
```liquid
{% for link in linklists[section.settings.main_linklist].links %}
  <!-- Menu item rendering with mega menu support -->
{% endfor %}
```

---

## Footer Architecture

### Footer Section: `sections/footer-md.liquid`

**Structure:**
- Column 1: Logo, Newsletter (Klaviyo), Social Icons
- Columns 2-4: Menu columns with configurable titles
- Column 5: USB Logo, Payment Icons, Copyright

**Menu Configuration:**
- Column 2: `section.settings.footer_column2_menu`
- Column 3: `section.settings.footer_column3_menu`
- Column 4: `section.settings.footer_column4_menu`

**Code Reference:**
```liquid
{% for link in linklists[section.settings.footer_column2_menu].links %}
  <li><p><a href="{{ link.url }}">{{ link.title }}</a></p></li>
{% endfor %}
```

**Newsletter Integration:**
- **Klaviyo Form:** Embedded via `<div class="klaviyo-form-LWy48v"></div>`
- **Form ID:** `LWy48v`
- **Code Reference:** `sections/footer-md.liquid` line 36
- **Wrapper:** `<div class="newsletter">` container
- **Settings:** Newsletter title and text configurable via `section.settings.newsletter_title` and `section.settings.newsletter_text`

**Social Media Icons:**
- **Icons:** Instagram, TikTok, Facebook, YouTube, Twitter/X
- **Settings:** `settings.instagram_link`, `settings.tiktok_link`, `settings.facebook_link`, `settings.youtube_link`, `settings.twitter_link`
- **Code Reference:** `sections/footer-md.liquid` lines 39-54
- **Rendering:** Icons rendered via snippet includes (`icon-instagram`, `icon-tik-tok`, `icon-facebook`, `icon-youtube`)
- **Twitter/X:** Uses image asset `icon-x.png` instead of snippet

**Footer Widgets:**
- **Freshworks Widget:** Widget ID `44000003784` (lines 134-140)
- **USB Logo:** Displays in column 5 (wide column), hidden on mobile via `.mobile-hide` class
- **Brand Logos:** Block-based brand logo display in column 5

---

## Product Template System

### Available Product Templates

1. **Default Product Template**
   - File: `sections/product-template.liquid`
   - Template: `templates/product.json`
   - Standard product display

2. **HEX® Visualization Template**
   - File: `sections/product-template-hexviz.liquid`
   - Template: `templates/product.hexviz.json`
   - HEX® product visualization features

3. **MyoVolt Product Template**
   - File: `sections/product-template-myovolt.liquid`
   - Template: `templates/product.myovolt.json`
   - MyoVolt-specific product features

4. **Product Details Template**
   - File: `sections/product-details-template.liquid`
   - Detailed product view

5. **Full-Width Images Template**
   - File: `sections/product-full-width-images-template.liquid`
   - Full-width image layout

### Template Assignment

**Method:**
- Templates assigned via template suffix in Shopify Admin
- Product template selected in Shopify Admin → Product → Search engine listing → Template dropdown
- Template configuration in `templates/product.json` files
- Template suffix matches section file name (e.g., `product.myovolt` → `product-template-myovolt.liquid`)

**Available Templates:**
- `product` (default) - Uses `sections/product-template.liquid`
- `product.hexviz` - Uses `sections/product-template-hexviz.liquid`
- `product.myovolt` - Uses `sections/product-template-myovolt.liquid`
- `product.details` - Uses `sections/product-details-template.liquid`
- `product.full-width-images` - Uses `sections/product-full-width-images-template.liquid`

**App Block Support:**
All product templates support app blocks via consistent pattern:
```liquid
<div class="product-app-blocks">
  {%- for block in section.blocks -%}
    {% if block.type == '@app' %}
        {% render block %}
    {% endif %}
  {%- endfor -%}
</div>
```

**Code References:**
- `sections/product-template.liquid` lines 412-418 (exact implementation)
- `sections/product-template-hexviz.liquid` lines 387-393
- `sections/product-template-myovolt.liquid` lines 319-325
- `sections/product-details-template.liquid` lines 326-332
- `sections/product-full-width-images-template.liquid` lines 336-342

**Display Position:**
- App blocks appear above "Best For" metafield
- App blocks appear before "Add to Cart" button
- Wrapped in `product-app-blocks` div for styling

---

## Section Organization

### Section Types

**Static Sections:**
- Header, Footer (always loaded)
- No block support

**Dynamic Sections:**
- Product templates
- Collection templates
- Page sections
- Homepage sections
- Support blocks

**Block-Based Sections:**
- Footer (block-based menus)
- Page sections (multiple block types)
- Homepage sections (slideshow, featured products, etc.)

### Key Sections

**Navigation:**
- `header-md.liquid` - Main header
- `footer-md.liquid` - Footer

**Product:**
- `product-template.liquid` - Default product
- `product-template-hexviz.liquid` - HEX® products
- `product-template-myovolt.liquid` - MyoVolt products

**Homepage:**
- `home-slideshow-md.liquid` - Homepage slideshow
- `home-featured-promotions-md.liquid` - Promotions
- `home-top-bestseller-md.liquid` - Bestsellers

**Content:**
- `page-template.liquid` - Standard pages
- `page-details-template.liquid` - Detailed pages
- `blog-template.liquid` - Blog listing

---

## Snippet System

### Key Snippets

**Navigation:**
- `snippets/menu.liquid` - Desktop menu rendering
- `snippets/mobile-menu.liquid` - Mobile menu rendering
- `snippets/vertical-menu.liquid` - Vertical menu (if enabled)

**Product:**
- `snippets/product-form.liquid` - Product form (add to cart)
- `snippets/product-images.liquid` - Product image gallery
- `snippets/product-swatch.liquid` - Color swatches

**Shogun:**
- `snippets/shogun-content-handler.liquid` - Shogun page builder integration

**Usage Pattern:**
```liquid
{% include 'menu' with section.settings.main_linklist %}
{% render 'product-form' %}
```

---

## Layout System

### Main Layout: `layout/theme.liquid`

**Structure:**
- HTML document structure
- Header section inclusion
- Main content area
- Footer section inclusion
- JavaScript and CSS includes

**Key Features:**
- Responsive meta tags
- Theme settings integration
- App block support
- Shogun integration

---

## Settings Schema

### Configuration: `config/settings_schema.json`

**Key Settings Groups:**
- Theme info
- Global settings (brand selection)
- Performance settings
- Color scheme
- Typography
- Header settings
- Footer settings
- Product settings

**Brand Selection:**
```json
{
  "type": "select",
  "id": "site_brand",
  "label": "Brand",
  "options": [
    {"value": "SD", "label": "ShockDoctor"},
    {"value": "MD", "label": "McDavid"},
    {"value": "NS", "label": "Nathan"},
    {"value": "CS", "label": "Cutters"}
  ]
}
```

---

## Custom Functionality

### Multi-Brand Support

**Implementation:**
- Brand-specific sections (header-md, footer-md, etc.)
- Brand selection via `site_brand` setting
- Conditional rendering based on brand

**Code Pattern:**
```liquid
{% if settings.site_brand == "MD" %}
  {% section 'header-md' %}
{% endif %}
```

### Mega Menu System

**Features:**
- Automatic mega menu for nested menus
- Block-based promo content
- Configurable descriptions
- Multi-column layout

**Configuration:**
- Menu structure in Shopify Admin
- Promo blocks in Theme Customizer → Header → Blocks

---

## Performance Considerations

**Theme Performance:**
- Lazy loading for images
- Optimized asset loading
- Performance mode settings (Sport vs. Ludicrous)
- Image loading styles (Appear, Blur-up, Fade-in)

**Settings:**
- Performance mode: `settings.performance`
- Image loading: `settings.image_loading_style`

---

## Code Verification

All architecture documentation verified against:
- Theme code: `code/mcdavid-11NOV2025/`
- Settings schema: `config/settings_schema.json`
- Actual section files and line numbers

**Evidence-Based:**
- Menu assignments verified in header/footer sections
- Template structure verified in template files
- Settings verified in settings schema

---

*This architecture documentation is based on actual theme code analysis. All code references include file paths and line numbers for verification.*


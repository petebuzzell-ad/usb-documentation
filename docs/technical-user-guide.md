# Technical User Guide
## Developer Documentation for USB - McDavid

---

## Navigation Implementation

### Header Menu System

**Section:** `sections/header-md.liquid`  
**Menu Setting:** `section.settings.main_linklist`

**Code Reference:**
```liquid
{% for link in linklists[section.settings.main_linklist].links %}
  <li><a href="{{ link.url }}">{{ link.title }}</a></li>
{% endfor %}
```
Location: Line 106

**Menu Rendering:**
- Desktop menu: Rendered inline in header section
- Mobile menu: Uses `snippets/mobile-menu.liquid`
- Mega menu: Automatic for items with submenus (lines 108-192)

**Mega Menu Implementation:**
- **Automatic Detection:** Mega menu displays when `link.links.size > 0` (line 108)
- **Block Matching:** Menu items matched to blocks via handleized title comparison (line 114)
- **Block-Based Promo Content:** Promotional blocks appear in rightmost column when `activate_promo` is true (line 116)
- **Configurable Descriptions:** Menu item descriptions via block `description` setting (line 115)
- **Multi-Column Layout:** 
  - First column: "Browse All" link + main submenu items + description
  - Additional columns: Submenu categories with their items
  - Rightmost column: Promotional content (if enabled)
- **Special Formatting:**
  - Menu items with `**` are bolded
  - Menu items with `%%` show descriptions (format: `Title%%Description`)
  - HEX® logo: Menu item titled exactly "HEX®" displays logo image instead of text (line 107)
  - SportMed® branding: "Braces & Supports" displays as "SportMed®" in mega menu
- **Code Reference:** `sections/header-md.liquid` lines 107-196 (exact implementation)
- **Accessibility:** Mega menu includes ARIA attributes (`aria-expanded`, `aria-controls`) for screen readers

### Footer Menu System

**Section:** `sections/footer-md.liquid`  
**Menu Settings:**
- `section.settings.footer_column2_menu` (line 61)
- `section.settings.footer_column3_menu` (line 71)
- `section.settings.footer_column4_menu` (line 81)

**Code Reference:**
```liquid
{% for link in linklists[section.settings.footer_column2_menu].links %}
  <li><p><a href="{{ link.url }}">{{ link.title }}</a></p></li>
{% endfor %}
```

**Footer Structure:**
- Column-based layout
- Each column has independent menu
- Column titles configurable via section settings

---

## Template System

### Product Templates

**Default Template:**
- File: `sections/product-template.liquid`
- JSON: `templates/product.json`
- Standard product display with app block support

**HEX® Template:**
- File: `sections/product-template-hexviz.liquid`
- JSON: `templates/product.hexviz.json`
- HEX® visualization features

**MyoVolt Template:**
- File: `sections/product-template-myovolt.liquid`
- JSON: `templates/product.myovolt.json`
- MyoVolt-specific features and metafields

**Template Assignment:**
- Selected via template suffix in Shopify Admin
- Template configuration in JSON files
- Section type matches template suffix

### App Block Support

**Implementation Pattern:**
```liquid
<div class="product-app-blocks">
  {%- for block in section.blocks -%}
    {% if block.type == '@app' %}
        {% render block %}
    {% endif %}
  {%- endfor -%}
</div>
```

**Templates with App Blocks:**
- `product-template.liquid` (line 412-418)
- `product-template-hexviz.liquid` (line 387-393)
- `product-template-myovolt.liquid` (line 319-325)
- `product-details-template.liquid` (line 326-332)
- `product-full-width-images-template.liquid` (line 336-342)

---

## Customizer Sections

### Header Section

**File:** `sections/header-md.liquid`  
**Type:** Static section

**Key Settings:**
- `main_linklist` - Main navigation menu
- `logo_white` - White logo (homepage)
- `logo_colored` - Colored logo (other pages)
- `help_text`, `help_text2`, `help_text3` - Announcement bar messages
- `help_text_start_date`, `help_text_end_date` - Message date ranges
- `brace_finder` - Brace finder link toggle
- `brace_finder_url` - Brace finder URL
- `brace_finder_label` - Brace finder label

**Blocks:**
- Mega menu promo blocks
- Block type: `meganav` (defined in schema at line 623)
- Settings:
  - `trigger` (text) - Menu item handle (handleized version, e.g., 'cups-compression')
  - `description` (text) - Description text shown in first column under title
  - `activate_promo` (checkbox) - Enable promotional content
  - `image` (image_picker) - Promo image
  - `pre_header` (text) - Small text above main header
  - `header` (text) - Main promotional headline
  - `link_label` (text) - Button/link text
  - `link_url` (url) - Destination URL for promotional link
- **Code Reference:** `sections/header-md.liquid` lines 107-196 (mega menu rendering), lines 620-677 (schema definition)
- **Block Matching:** Blocks matched to menu items via `block.settings.trigger == handleized_link_title` (line 114)

### Footer Section

**File:** `sections/footer-md.liquid`  
**Type:** Static section

**Key Settings:**
- `footer_logo_image` - Footer logo
- `footer_usb_logo` - USB logo
- `newsletter_title` - Newsletter section title
- `newsletter_text` - Newsletter description
- `footer_column2_title` - Column 2 title
- `footer_column2_menu` - Column 2 menu
- `footer_column3_title` - Column 3 title
- `footer_column3_menu` - Column 3 menu
- `footer_column4_title` - Column 4 title
- `footer_column4_menu` - Column 4 menu

**Social Media:**
- Configured via global settings
- Icons: Instagram, TikTok, Facebook, YouTube, Twitter/X
- Settings: `instagram_link`, `tiktok_link`, `facebook_link`, `youtube_link`, `twitter_link`

### Product Template Sections

**Default Product Template:**
- File: `sections/product-template.liquid`
- Supports app blocks
- Custom metafield display
- Product form integration

**Settings:**
- `product_images_position` - Image gallery position
- `product_description_position` - Description position
- `review_position` - Review section position
- `gallery_arrows` - Image navigation arrows

**Blocks:**
- App blocks (`@app` type)
- Custom content blocks
- Product form blocks

---

## Code Patterns

### Menu Access

**Header Menu:**
```liquid
{% for link in linklists[section.settings.main_linklist].links %}
  <!-- Menu item -->
{% endfor %}
```

**Footer Menu:**
```liquid
{% for link in linklists[section.settings.footer_column2_menu].links %}
  <!-- Footer link -->
{% endfor %}
```

### Metafield Access

**Product Metafields:**
```liquid
{{ product.metafields.custom.best_for }}
{{ product.metafields.custom.product_family }}
{{ product.metafields.custom.features }}
{{ product.metafields.custom.details }}
{{ product.metafields.custom.care }}
{{ product.metafields.custom.description_image }}
```

**Conditional Rendering Pattern:**
```liquid
{% if product.metafields.custom.best_for != blank %}
  <div class="best-for">
    <span>Best For:</span> {{ product.metafields.custom.best_for }}
  </div>
{% endif %}
```

**MyoVolt Metafields:**
```liquid
{{ product.metafields.myovolt.hero_image_desktop.value | image_url: width: 800 | image_tag }}
{{ product.metafields.myovolt.hero_image_mobile.value | image_url: width: 800 | image_tag }}
{{ product.metafields.myovolt.hero_description }}
{{ product.metafields.myovolt.video.value | video_tag: autoplay: true, loop: true, muted: true }}
```

**File Reference Access:**
- File references require `.value` property: `product.metafields.myovolt.hero_image_desktop.value`
- Use Liquid filters for image/video rendering: `image_url`, `image_tag`, `video_tag`

**Metaobject Access:**
```liquid
{% for feature in product.metafields.custom.features.value %}
  <h5>{{ feature.title }}</h5>
  <p>{{ feature.description }}</p>
{% endfor %}
```

**List Metafield Access:**
```liquid
{% for detailsItem in product.metafields.custom.details.value %}
  <div class="product-description-item">
    <h5>{% render 'shortcode' load: detailsItem %}</h5>
  </div>
{% endfor %}
```

**Rich Text Metafield Access:**
```liquid
{{ product.metafields.myovolt.description | metafield_tag }}
{{ product.metafields.myovolt.treatment_mode_1_description | metafield_tag }}
```

**Code References:**
- `sections/product-template.liquid` lines 420-424 (best_for)
- `sections/product-template.liquid` lines 532-548 (features)
- `sections/product-template-myovolt.liquid` lines 519-536 (hero images and video)
- `sections/product-template-myovolt.liquid` lines 587-604 (treatment modes)

### App Block Rendering

**Standard Pattern:**
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

**Display Position:**
- App blocks appear in `product-app-blocks` div container
- Positioned above "Best For" metafield
- Positioned before "Add to Cart" button
- Only renders blocks with `block.type == '@app'`

**Block Configuration:**
- Blocks added via Theme Customizer → Product pages → Add block
- App blocks automatically available from installed apps
- Block settings configured in Theme Customizer or app interface

---

## Snippet Usage

### Menu Snippets

**Desktop Menu:**
```liquid
{% include 'menu' with section.settings.main_linklist %}
```

**Mobile Menu:**
```liquid
{% include 'mobile-menu' with section.settings.main_linklist %}
```

**Files:**
- `snippets/menu.liquid` - Desktop menu rendering
- `snippets/mobile-menu.liquid` - Mobile menu rendering

### Product Snippets

**Product Form:**
```liquid
{% include 'product-form' with 'product' %}
```

**Product Images:**
```liquid
{% include 'product-images' %}
```

**Files:**
- `snippets/product-form.liquid` - Add to cart form
- `snippets/product-images.liquid` - Image gallery
- `snippets/product-swatch.liquid` - Color swatches

---

## Settings Schema Reference

### Global Settings

**Brand Selection:**
```json
{
  "id": "site_brand",
  "type": "select",
  "options": [
    {"value": "SD", "label": "ShockDoctor"},
    {"value": "MD", "label": "McDavid"},
    {"value": "NS", "label": "Nathan"},
    {"value": "CS", "label": "Cutters"}
  ]
}
```

**Location:** `config/settings_schema.json`

### Header Settings

**Menu Settings:**
- `main_linklist` - Main navigation menu (link_list type)
- Menu assigned in Theme Customizer → Header section

**Logo Settings:**
- `logo_white` - White logo image
- `logo_colored` - Colored logo image

### Footer Settings

**Menu Settings:**
- `footer_column2_menu` - Column 2 menu (link_list type)
- `footer_column3_menu` - Column 3 menu (link_list type)
- `footer_column4_menu` - Column 4 menu (link_list type)

**Title Settings:**
- `footer_column2_title` - Column 2 title
- `footer_column3_title` - Column 3 title
- `footer_column4_title` - Column 4 title

---

## Template Assignments

### Product Templates

**Default:**
- Template: `product` (no suffix)
- Section: `product-template`

**HEX®:**
- Template: `product.hexviz`
- Section: `product-template-hexviz`

**MyoVolt:**
- Template: `product.myovolt`
- Section: `product-template-myovolt`

**Assignment:**
- Selected in Shopify Admin → Product → Template
- Template suffix determines section used

### Page Templates

**Available Templates:**
- `page` - Default page template
- `page.sidebar` - Page with sidebar
- `page.banner` - Page with banner
- `page.details` - Detailed page template
- `page.multi-column` - Multi-column layout
- `page.gallery` - Gallery template
- `page.faq` - FAQ template
- `page.contact` - Contact template

**Sections:**
- `sections/page-template.liquid`
- `sections/page-sidebar-template.liquid`
- `sections/page-banner-template.liquid`
- `sections/page-details-template.liquid`

---

## Custom Functionality

### Multi-Brand Support

**Implementation:**
- Brand-specific sections (header-md, footer-md)
- Brand selection via `site_brand` setting
- Conditional section rendering

**Code Pattern:**
```liquid
{% if settings.site_brand == "MD" %}
  {% section 'header-md' %}
  {% section 'footer-md' %}
{% endif %}
```

### Mega Menu System

**Features:**
- Automatic detection of nested menus
- Block-based promo content
- Configurable descriptions
- Multi-column layout

**Block Configuration:**
- Block type: `mega_menu_promo`
- Trigger: Menu item handle (case-sensitive)
- Promo content: Image, text, links

---

## Troubleshooting

### Menu Not Displaying

**Check:**
1. Menu exists in Shopify Admin → Navigation
2. Menu assigned in Theme Customizer → Header/Footer
3. Menu has items
4. Section settings saved

**Code Verification:**
- Check `section.settings.main_linklist` in header section
- Verify menu handle matches Shopify menu handle

### App Blocks Not Rendering

**Check:**
1. App block added in Theme Customizer
2. Block type is `@app`
3. App block code present in section
4. Section supports blocks

**Code Verification:**
- Check for `{% render block %}` in section
- Verify block type check: `{% if block.type == '@app' %}`

### Metafields Not Displaying

**Check:**
1. Metafield exists on product
2. Metafield namespace/key correct
3. Metafield value populated
4. Liquid syntax correct

**Code Pattern:**
```liquid
{% if product.metafields.custom.best_for != blank %}
  {{ product.metafields.custom.best_for }}
{% endif %}
```

---

## Code References Summary

**Header Menu:**
- `sections/header-md.liquid` line 106

**Footer Menus:**
- `sections/footer-md.liquid` lines 61, 71, 81

**Product Metafields:**
- `sections/product-template.liquid` line 420

**App Blocks:**
- `sections/product-template.liquid` lines 412-418
- `sections/product-template-hexviz.liquid` lines 387-393
- `sections/product-template-myovolt.liquid` lines 319-325

**Settings Schema:**
- `config/settings_schema.json`

---

*This technical guide provides code-level documentation for developers. All code references include file paths and line numbers for verification.*


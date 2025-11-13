# Data Guide
## Complete Metafield and Metaobject Reference

---

## Metafield Organization

Metafields are organized by namespace. This guide documents all metafields found in the McDavid data exports.

**Data Source:** `data/mcdavid/AD_MCDAVID_EVERYTHING_Export_2025-11-11_075420/Products.csv`

---

## Custom Namespace (`custom.*`)

### Product Metafields

**`custom.best_for`** (single_line_text_field)
- **Description:** Product use case or target audience
- **Display Location:** Product page, below app blocks and above "Add to Cart" button
- **Display Format:** "Best For: [value]" with label prefix, wrapped in `<div class="best-for">`
- **Display Position:** Appears after app blocks (`product-app-blocks` div) and before product form
- **Example:** "Moderate support for minor to moderate sprains, strains and wrist instability"
- **Code Reference:** 
  - `sections/product-template.liquid` lines 420-424 (exact implementation)
  - `sections/product-template-hexviz.liquid` lines 420-424
  - `sections/product-template-myovolt.liquid` lines 335-338
- **Usage Pattern:**
  ```liquid
  {% if product.metafields.custom.best_for != blank %}
    <div class="best-for">
      <span>Best For:</span> {{ product.metafields.custom.best_for }}
    </div>
  {% endif %}
  ```
- **Conditional Rendering:** Only displays if metafield has value (not blank)
- **Styling:** Uses `.best-for` CSS class for styling
- **When to Use:** Describe the primary use case or target audience for the product
- **Data Verification:** Verified in Products.csv export - used across product catalog

**`custom.product_family`** (list.product_reference)
- **Description:** Product family/line identifier
- **Usage:** Product grouping and relationships
- **Example:** "MDP300"

**`custom.features`** (list.metaobject_reference)
- **Description:** Product features (references Features metaobject)
- **Display Location:** Product page, in dedicated "Features" section below product description
- **Display Format:** Section with title "Features", each feature displays as:
  - Section wrapper: `<div class="product_desc product_features extended">`
  - Section title: `<h4 class="title">Features</h4>`
  - Each feature in: `<div class="product-description-item">`
  - Feature title as `<h5>` heading
  - Feature description as `<p>` paragraph text
- **Display Order:** Appears after product description section, before Details section
- **Metaobject:** References `features` metaobject (see Metaobjects section below)
- **Code Reference:** 
  - `sections/product-template.liquid` lines 532-548 (exact implementation)
  - `sections/product-template-hexviz.liquid` lines 547-563
- **Usage Pattern:**
  ```liquid
  {% if product.metafields.custom.features != blank %}
    <div class="product_desc product_features extended">
      <div class="description" itemprop="description">
        <h4 class="title">Features</h4>
        <div class="description-content">
          <div class="product-description-image">
            {% for feature in product.metafields.custom.features.value %}
              <div class="product-description-item">
                <h5>{{ feature.title }}</h5>
                <p>{{ feature.description }}</p>
              </div>
            {% endfor %}
          </div>
        </div>
      </div>
    </div>
  {% endif %}
  ```
- **Conditional Rendering:** Only displays if metafield has value (not blank)
- **Loop Structure:** Iterates through `product.metafields.custom.features.value` array
- **Metaobject Access:** Uses `.value` property to access metaobject data
- **When to Use:** Highlight key product features and benefits
- **Creating Features:** Features are created as metaobjects in Shopify Admin → Settings → Custom data → Metaobjects → Features
- **Data Verification:** 100+ feature entries available in Metaobjects.csv export

**`custom.details`** (list.single_line_text_field)
- **Description:** Product detail points displayed as list items
- **Display Location:** Product page, in "Details" section below Features section
- **Display Format:** 
  - Section wrapper: `<div class="product_desc extended">`
  - Section title: `<h4 class="title">{{ 'products.product.details' | t }}</h4>` (uses translation string)
  - Each detail in: `<div class="product-description-item"><h5>...</h5></div>`
  - Details rendered as `<h5>` headings (not bulleted list)
- **Display Order:** Appears after Features section, before Care section
- **Example:** ["FITS LEFT OR RIGHT WRIST", "UNISEX", "HSA/FSA ELIGIBLE"]
- **Code Reference:**
  - `sections/product-template.liquid` lines 550-563 (exact implementation)
  - `sections/product-template-hexviz.liquid` lines 565-578
- **Usage Pattern:**
  ```liquid
  {% if product.metafields.custom.details != blank %}
    <div class="product_desc extended">
      <div class="description" itemprop="description">
        <h4 class="title">{{ 'products.product.details' | t }}</h4>
        <div class="description-content">
          <div class="product-description-image">
            {% for detailsItem in product.metafields.custom.details.value %}
              <div class="product-description-item">
                <h5>{% render 'shortcode' load: detailsItem %}</h5>
              </div>
            {% endfor %}
          </div>
        </div>
      </div>
    </div>
  {% endif %}
  ```
- **Shortcode Processing:** Details are processed through `shortcode` snippet (`snippets/shortcode.liquid`), which may handle special formatting, links, or HTML
- **Conditional Rendering:** Only displays if metafield has value (not blank)
- **Translation Support:** Section title uses Shopify translation system (`'products.product.details' | t`)
- **When to Use:** List key product specifications, certifications, or important details
- **Data Verification:** Verified in Products.csv export - commonly used across product catalog

**`custom.care`** (list.single_line_text_field)
- **Description:** Care instructions for product maintenance
- **Display Location:** Product page, in "Care" section below Details section
- **Display Format:**
  - Section wrapper: `<div class="product_desc extended">`
  - Section title: `<h4 class="title">{{ 'products.product.care' | t }}</h4>` (uses translation string)
  - Each care instruction in: `<div class="product-description-item">` (no heading, just text)
- **Display Order:** Appears after Details section, before Shipping & Returns section
- **Example:** ["Hand wash. Air dry only."]
- **Code Reference:**
  - `sections/product-template.liquid` lines 565-578 (exact implementation)
  - `sections/product-template-hexviz.liquid` lines 580-593
- **Usage Pattern:**
  ```liquid
  {% if product.metafields.custom.care != blank %}
    <div class="product_desc extended">
      <div class="description" itemprop="description">
        <h4 class="title">{{ 'products.product.care' | t }}</h4>
        <div class="description-content">
          <div class="product-description-image">
            {% for careItem in product.metafields.custom.care.value %}
              <div class="product-description-item">{{ careItem }}</div>
            {% endfor %}
          </div>
        </div>
      </div>
    </div>
  {% endif %}
  ```
- **Conditional Rendering:** Only displays if metafield has value (not blank)
- **Translation Support:** Section title uses Shopify translation system (`'products.product.care' | t`)
- **Format Difference:** Unlike Details, Care items don't use `<h5>` headings - just plain text in div
- **When to Use:** Provide washing, care, and maintenance instructions for products
- **Data Verification:** Verified in Products.csv export - commonly used for care instructions

**`custom.description_image`** (file_reference)
- **Description:** Additional image displayed in product description area
- **Display Location:** Product page, within product description section
- **Display Conditions:**
  - Only displays when `section.settings.product_description_position == "top"`
  - Appears within description content area
  - Wrapped in `<div class="product-description-image">` container
- **Display Format:** 
  - Image wrapper: `<div class="description-image">`
  - Image rendered at 800px height
  - Displays alongside product description text
- **Image Size:** Rendered at 800px height using `image_url: height: 800` filter
- **Code Reference:** 
  - `sections/product-template.liquid` lines 520-524 (exact implementation)
  - `sections/product-template-myovolt.liquid` line 576 (also used in MyoVolt template at 1500px height)
- **Usage Pattern:**
  ```liquid
  {% if section.settings.product_description_position == "top" %}
    {% if product.description != blank %}
      <div class="description" itemprop="description">
        <h4 class="title">Description</h4>
        <div class="description-content">
          <div class="product-description-image">
            <div class="product-description">{{ product.description }}</div>
            {% if product.metafields.custom.description_image %}
              <div class="description-image">
                {{ product.metafields.custom.description_image | image_url: height: 800 | image_tag }}
              </div>
            {% endif %}
          </div>
        </div>
      </div>
    {% endif %}
  {% endif %}
  ```
- **Conditional Rendering:** Only displays if description position is "top" and image exists
- **MyoVolt Usage:** In MyoVolt template, displays at 1500px height alongside `myovolt.description`
- **When to Use:** Add supporting imagery to product description (lifestyle shots, detail images, etc.)
- **Data Verification:** Verified in Products.csv export - file reference type

**`custom.free_shipping_returns`** (rich_text_field)
- **Description:** Free shipping and returns information
- **Display Location:** Product page, in "Shipping & Returns" section (if used)
- **Note:** Currently, shipping/returns section uses theme translation strings (`products.product.shipping_returns_html`)
- **Usage:** Can be used for custom shipping/returns content if needed
- **Code Reference:** `sections/product-template.liquid` lines 581-592 (uses translation, not metafield)
- **When to Use:** Override default shipping/returns text with product-specific information

**`custom.sika_hsa_fsa`** (single_line_text_field)
- **Description:** HSA/FSA eligibility (Sika integration)
- **Usage:** Healthcare spending account eligibility

**`custom.sika_hsa_fsa_lmn_beluga`** (single_line_text_field)
- **Description:** HSA/FSA eligibility variant

**`custom.sika_hsa_fsa_subscription`** (single_line_text_field)
- **Description:** HSA/FSA eligibility for subscriptions

---

## Global Namespace (`global.*`)

### Product Metafields

**`global.brand`** (string)
- **Description:** Product brand identifier
- **Usage:** Brand classification and filtering
- **Example:** "MD" (McDavid)
- **Code Reference:** `sections/product-template-myovolt.liquid` line 8
- **Usage Pattern:**
  ```liquid
  {% assign brand = product.metafields.global.brand %}
  ```

**`global.display_sku`** (string/boolean)
- **Description:** Display SKU flag or value
- **Display Location:** Product page, in SKU container
- **Code Reference:**
  - `sections/product-template-hexviz.liquid` lines 401-404
  - `sections/product-template-myovolt.liquid` lines 316-318
- **Usage Pattern:**
  ```liquid
  {% if product.metafields.global.display_sku %}
    <p class="display-sku">
      <span>SKU: <span itemprop="sku">{{ product.selected_or_first_available_variant.sku }}</span></span>
    </p>
  {% endif %}
  ```
- **When to Use:** Control SKU display on product pages

---

## MyoVolt Namespace (`myovolt.*`)

MyoVolt-specific product metafields for MyoVolt product template.

**`myovolt.hero_image_desktop`** (file_reference)
- **Description:** Hero image for desktop view
- **Display Location:** MyoVolt product template, hero section at top of product page
- **Display Conditions:** Only displays if `myovolt.hero_image_mobile` is also present (conditional logic)
- **Image Size:** Rendered at 800px width using `image_url: width: 800` filter
- **Display Behavior:** 
  - Hidden on mobile via `.mobile-myovolt-hide` CSS class
  - Shows on desktop only
  - Wrapped in `<div class="myovolt-hero">` container
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 519-528 (exact implementation)
- **Usage Pattern:**
  ```liquid
  {% if product.metafields.myovolt.hero_image_mobile != blank %}
    <div class="myovolt-hero">
      {{ product.metafields.myovolt.hero_image_desktop.value | image_url: width: 800 | image_tag: class: 'mobile-myovolt-hide', loading: "lazy" }}
      {{ product.metafields.myovolt.hero_image_mobile.value | image_url: width: 800 | image_tag: class: 'desktop-myovolt-hide', loading: "lazy" }}
    </div>
  {% endif %}
  ```
- **Required:** Yes, for MyoVolt products (required if mobile image is present)
- **Recommended Size:** 1920px width for optimal quality on desktop displays
- **Lazy Loading:** Uses `loading: "lazy"` attribute for performance
- **Value Access:** Uses `.value` property to access file reference

**`myovolt.hero_image_mobile`** (file_reference)
- **Description:** Hero image for mobile view
- **Display Location:** MyoVolt product template, hero section
- **Image Size:** Rendered at 800px width
- **Display Behavior:** Hidden on desktop (`.desktop-myovolt-hide` class)
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 519-526
- **Required:** Optional (falls back to desktop image if not provided)
- **Recommended Size:** 768px width for mobile optimization

**`myovolt.hero_description`** (multi_line_text_field)
- **Description:** Hero section description text
- **Display Location:** MyoVolt product template, below hero image
- **Display Format:** Text block with class `myovolt-hero-description`
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 530-532
- **Required:** Optional
- **When to Use:** Provide compelling product description for hero section

**`myovolt.video`** (file_reference)
- **Description:** Product video file
- **Display Location:** MyoVolt product template, hero section below description
- **Display Format:** HTML5 video element with autoplay, loop, muted, no controls
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 534-536
- **Usage Pattern:**
  ```liquid
  {% if product.metafields.myovolt.video.value != blank %}
    <div class="myovolt-video">
      {{ product.metafields.myovolt.video.value | video_tag: autoplay: true, loop: true, muted: true, controls: false }}
    </div>
  {% endif %}
  ```
- **Required:** Optional
- **Video Format:** MP4 recommended
- **When to Use:** Add product demonstration or promotional video

**`myovolt.tech_spec_1`** through **`myovolt.tech_spec_4`** (single_line_text_field)
- **Description:** Technical specification labels/text
- **Display Location:** MyoVolt product template, technical specifications section
- **Display Format:** Each spec displays with its corresponding image
- **Example:** "Battery Life: 8 hours", "Weight: 12 oz"
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 541+ (tech specs section)
- **Required:** Optional (can use 1-4 specs)
- **When to Use:** Highlight key technical specifications with visual support

**`myovolt.tech_spec_1_image`** through **`myovolt.tech_spec_4_image`** (file_reference)
- **Description:** Technical specification images
- **Display Location:** MyoVolt product template, paired with corresponding tech spec text
- **Display Format:** Image displayed alongside or above specification text
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 541+ (tech specs section)
- **Required:** Optional (should match corresponding tech_spec field)
- **Recommended Size:** Appropriate for specification display area
- **When to Use:** Visual representation of technical specifications

**`myovolt.treatment_modes_title`** (single_line_text_field)
- **Description:** Treatment modes section title/heading
- **Display Location:** MyoVolt product template, treatment modes section
- **Display Format:** `<h3>` heading
- **Example:** "Treatment Modes"
- **Code Reference:** `sections/product-template-myovolt.liquid` line 583
- **Required:** Optional
- **When to Use:** Provide section title for treatment modes

**`myovolt.treatment_modes_subtitle`** (single_line_text_field)
- **Description:** Treatment modes section subtitle
- **Display Location:** MyoVolt product template, treatment modes section below title
- **Display Format:** `<p>` paragraph text
- **Code Reference:** `sections/product-template-myovolt.liquid` line 584
- **Required:** Optional
- **When to Use:** Provide additional context or description for treatment modes section

**`myovolt.treatment_mode_1_image`** through **`myovolt.treatment_mode_3_image`** (file_reference)
- **Description:** Treatment mode images (up to 3 modes)
- **Display Location:** MyoVolt product template, treatment modes section
- **Display Format:** Image displayed at 150x150px, paired with description
- **Image Size:** Rendered at 150px width and height
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 587-604
- **Required:** Optional (should match corresponding description)
- **When to Use:** Visual representation of each treatment mode

**`myovolt.treatment_mode_1_description`** through **`myovolt.treatment_mode_3_description`** (rich_text_field)
- **Description:** Treatment mode descriptions (up to 3 modes)
- **Display Location:** MyoVolt product template, treatment modes section below images
- **Display Format:** Rich text (supports formatting via `metafield_tag` filter)
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 587-604
- **Usage Pattern:**
  ```liquid
  {% if product.metafields.myovolt.treatment_mode_1_image and product.metafields.myovolt.treatment_mode_1_description %}
    <div>
      {{ product.metafields.myovolt.treatment_mode_1_image | image_url: width: 150, height: 150 | image_tag }}
      <div>{{ product.metafields.myovolt.treatment_mode_1_description | metafield_tag }}</div>
    </div>
  {% endif %}
  ```
- **Required:** Optional (should match corresponding image)
- **When to Use:** Describe each treatment mode functionality

**`myovolt.highlight_1_image`** and **`myovolt.highlight_2_image`** (file_reference)
- **Description:** Product highlight background images (2 highlights)
- **Display Location:** MyoVolt product template, highlights section
- **Display Format:** Background image for highlight block, rendered at 1080px height
- **Image Size:** Rendered as CSS background-image at 1080px height
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 608-617
- **Required:** Optional
- **When to Use:** Visual background for product highlight sections

**`myovolt.highlight_1_title`** and **`myovolt.highlight_2_title`** (single_line_text_field)
- **Description:** Product highlight titles (2 highlights)
- **Display Location:** MyoVolt product template, highlights section over background image
- **Display Format:** `<h3>` heading overlaid on background image
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 610, 614
- **Required:** Optional
- **When to Use:** Title for each product highlight

**`myovolt.highlight_1_description`** and **`myovolt.highlight_2_description`** (rich_text_field)
- **Description:** Product highlight descriptions (2 highlights)
- **Display Location:** MyoVolt product template, highlights section below title
- **Display Format:** Rich text (supports formatting via `metafield_tag` filter)
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 611, 615
- **Required:** Optional
- **When to Use:** Detailed description for each product highlight

**`myovolt.included_image_desktop`** and **`myovolt.included_image_mobile`** (file_reference)
- **Description:** Included items images (desktop and mobile versions)
- **Display Location:** MyoVolt product template, included items section
- **Display Format:** CSS background-image, rendered at 1300px height
- **Display Behavior:** Desktop image hidden on mobile (`.mobile-myovolt-hide`), mobile image hidden on desktop (`.desktop-myovolt-hide`)
- **Image Size:** Rendered as CSS background-image at 1300px height
- **Code Reference:** `sections/product-template-myovolt.liquid` lines 619-621
- **Required:** Optional
- **When to Use:** Visual representation of included items/accessories

**`myovolt.included_items`** (rich_text_field)
- **Description:** Included items list text
- **Display Location:** MyoVolt product template, included items section
- **Display Format:** Rich text (supports formatting via `metafield_tag` filter)
- **Code Reference:** `sections/product-template-myovolt.liquid` line 622
- **Required:** Optional
- **When to Use:** List or describe items included with product

**`myovolt.description`** (rich_text_field)
- **Description:** MyoVolt product description (full description)
- **Display Location:** MyoVolt product template, product description section
- **Display Format:** Rich text (supports formatting via `metafield_tag` filter)
- **Code Reference:** `sections/product-template-myovolt.liquid` line 575
- **Note:** Can be displayed alongside `custom.description_image` if present
- **Required:** Optional (standard product description can be used instead)
- **When to Use:** Full product description with rich formatting support

**Template:** Used exclusively in `sections/product-template-myovolt.liquid`

**MyoVolt Product Requirements:**
- Product template must be set to "MyoVolt" (`product.myovolt`)
- Hero images (desktop and/or mobile) are required
- Other metafields are optional but recommended for complete product presentation
- See Business User Guide → MyoVolt Product Setup for complete configuration workflow

---

## PDP Namespace (`pdp.*`)

Product detail page display settings.

**`pdp.swatch_color`** (single_line_text_field)
- **Description:** Color swatch value
- **Usage:** Product color swatch display
- **Example:** "#000000"

**`pdp.swatch_image`** (single_line_text_field)
- **Description:** Color swatch image
- **Usage:** Product color swatch image display

---

## Google Shopping Namespace (`mm-google-shopping.*`)

Google Shopping feed metafields.

**Product Metafields:**
- `mm-google-shopping.custom_product` (boolean/string)
- `mm-google-shopping.age_group` (string/single_line_text_field)
- `mm-google-shopping.condition` (string/single_line_text_field)
- `mm-google-shopping.gender` (string/single_line_text_field)
- `mm-google-shopping.google_product_category` (string/single_line_text_field)
- `mm-google-shopping.color` (string/single_line_text_field)

**Variant Metafields:**
- `mm-google-shopping.custom_label_0` through `custom_label_4` (single_line_text_field)
- `mm-google-shopping.size_system` (single_line_text_field)
- `mm-google-shopping.size_type` (single_line_text_field)
- `mm-google-shopping.mpn` (single_line_text_field)

**Usage:** Google Shopping feed generation

---

## Facebook Namespace (`mc-facebook.*`)

Facebook catalog metafields.

**`mc-facebook.google_product_category`** (string)
- **Description:** Facebook product category
- **Usage:** Facebook catalog feed

**`mc-facebook.condition`** (string)
- **Description:** Product condition for Facebook
- **Usage:** Facebook catalog feed

---

## Avalara Namespace (`avalara.*`)

Tax classification metafields.

**`avalara.taxcode`** (single_line_text_field)
- **Description:** Tax classification code
- **Usage:** Tax calculation
- **Example:** "P0000000"

---

## Legacy/String Metafields

**`best_for`** (string)
- **Description:** Product use case (legacy)
- **Note:** Also available as `custom.best_for`

**`best_for_title`** (string)
- **Description:** Best for section title

**`brand`** (string)
- **Description:** Product brand
- **Example:** "MD"

**`catalog_year`** (string/multi_line_text_field)
- **Description:** Catalog year reference

**`display_sku`** (string/multi_line_text_field)
- **Description:** Display SKU

**`item_style`** (string)
- **Description:** Item style classification

**`materials_used`** (string)
- **Description:** Product materials

**`product_type_level`** (string)
- **Description:** Product type classification

**`sizing_content`** (string)
- **Description:** Sizing information

**`top_seller`** (string)
- **Description:** Top seller flag

**`product_feature`** (string)
- **Description:** Product feature (legacy)

**`description_alternate`** (string)
- **Description:** Alternate description

**`protect_type`** (string)
- **Description:** Protection type

**`item_class`** (string)
- **Description:** Item classification

**`segment`** (string)
- **Description:** Product segment

**`ready_to_ship`** (string)
- **Description:** Ready to ship flag

**`stock_alternate`** (string)
- **Description:** Alternate stock information

**`youtube_id`** (string)
- **Description:** YouTube video ID

**`bundleid`** (string)
- **Description:** Bundle identifier

**`warnings`** (string)
- **Description:** Product warnings

**`mcdavid_size`** (string)
- **Description:** McDavid size classification

---

## ColorOp Namespace (`colorop.*`)

Color option management metafields.

**`colorop.ordering`** (single_line_text_field/string)
- **Description:** Color option ordering

**`colorop.canonicals`** (single_line_text_field/string)
- **Description:** Color option canonical URLs

**`colorop.handle1`** through **`colorop.handle7`** (single_line_text_field/string)
- **Description:** Color option product handles
- **Usage:** Color variant linking

---

## Microsoft Bing Ads Namespace (`msft_bingads.*`)

**Product Metafield:**
- `msft_bingads.product_status` (json_string)
- **Example:** `{"pending":4,"failed":0,"approved":0}`

**Variant Metafield:**
- `msft_bingads.import_status` (string)

---

## SEO Metafields

**`title_tag`** (string)
- **Description:** Custom page title for SEO
- **Usage:** SEO optimization

**`description_tag`** (string)
- **Description:** Custom meta description for SEO
- **Usage:** SEO optimization

**Variant:**
- `description_tag` (string) - Variant-level SEO description

---

## Metaobjects

### Features Metaobject

**Definition Handle:** `features`  
**Definition Name:** Features  
**Status:** Active

**Fields:**
- `title` (single_line_text_field) - Feature title (required)
  - Example: "BEST-SELLING PROTECTION", "ULTIMATE CONFIDENCE IN MOTION"
- `description` (multi_line_text_field) - Feature description (optional)
  - Example: "Specifically designed to anatomically wrap, flex and protect the knee by absorbing collisions, body-to-body contact and other impact."

**Usage:**
- Referenced via `custom.features` metafield (list.metaobject_reference)
- Used for product feature highlights on product pages
- Multiple features can be assigned to a single product
- Features display in dedicated "Features" section on product pages

**Example Feature Handles:**
- `features.best-selling-protection`
- `features.ultimate-confidence-in-motion`
- `features.extended-length`
- `features.superior-fit-unmatched-performance`
- `features.moisture-wicking`
- `features.unisex`
- `features.patented-hex-protection`
- `features.enhanced-fit-and-comfort`
- `features.durable`
- `features.breathable`

**Creating Features:**
1. Go to **Shopify Admin** → **Settings** → **Custom data** → **Metaobjects**
2. Find **Features** metaobject definition
3. Click **Add entry**
4. Enter feature title and description
5. Click **Save**
6. Feature can now be assigned to products via `custom.features` metafield

**Assigning Features to Products:**
1. Open product in Shopify Admin
2. Scroll to **Metafields** section
3. Find `custom.features` metafield
4. Click to add features (list field)
5. Search for and select feature entries
6. Multiple features can be selected
7. Click **Save**

**Data Source:** `data/mcdavid/AD_MCDAVID_EVERYTHING_Export_2025-11-11_075420/Metaobjects.csv`  
**Total Features in Catalog:** 100+ feature entries available

**Common Feature Categories:**
- Protection features (BEST-SELLING PROTECTION, ELITE PROTECTION)
- Technology features (PATENTED HEX® PROTECTION, MOISTURE WICKING)
- Fit and comfort (ENHANCED FIT AND COMFORT, CUSTOM-LIKE FIT)
- Durability (DURABLE, BUILT TO LAST)
- Versatility (UNISEX, FITS LEFT OR RIGHT LEG/KNEE/ANKLE)
- Care instructions (MACHINE WASHABLE / DRYABLE)

---

## Metafield Access in Liquid

### Product Metafields

```liquid
{{ product.metafields.custom.best_for }}
{{ product.metafields.custom.product_family }}
{{ product.metafields.custom.features }}
{{ product.metafields.myovolt.hero_image_desktop }}
{{ product.metafields.pdp.swatch_color }}
```

### Variant Metafields

```liquid
{{ variant.metafields.mm-google-shopping.custom_label_0 }}
{{ variant.metafields.msft_bingads.import_status }}
```

### Metaobject Access

```liquid
{% for feature in product.metafields.custom.features.value %}
  <h4>{{ feature.title }}</h4>
  <p>{{ feature.description }}</p>
{% endfor %}
```

---

## Data Relationships

**Product → Features:**
- Products reference Features metaobject via `custom.features`
- Multiple features per product (list reference)

**Product → Product Family:**
- Products reference other products via `custom.product_family`
- Used for product grouping

---

## Code References

### Product Template Metafield Usage

**Default Product Template** (`sections/product-template.liquid`):
- Line 420-423: `custom.best_for` - "Best For:" display
- Line 520-524: `custom.description_image` - Description image
- Line 532-548: `custom.features` - Features section
- Line 550-563: `custom.details` - Details section
- Line 565-578: `custom.care` - Care instructions section

**HEX® Product Template** (`sections/product-template-hexviz.liquid`):
- Line 420-423: `custom.best_for` - "Best For:" display
- Line 547-563: `custom.features` - Features section
- Line 565-578: `custom.details` - Details section
- Line 580-593: `custom.care` - Care instructions section

**MyoVolt Product Template** (`sections/product-template-myovolt.liquid`):
- Line 8: `global.brand` - Brand assignment
- Line 316-318: `global.display_sku` - SKU display
- Line 335-338: `custom.best_for` - "Best For:" display
- Line 519-526: `myovolt.hero_image_desktop` and `hero_image_mobile` - Hero images
- Line 530-532: `myovolt.hero_description` - Hero description
- Line 534-536: `myovolt.video` - Product video
- Line 541+: `myovolt.tech_spec_*` and `tech_spec_*_image` - Technical specifications
- Additional MyoVolt metafields throughout template

### Metafield Display Order on Product Pages

**Default Template Display Order:**
1. Product images and basic info
2. App blocks (Sika Discovery Eligibility, etc.)
3. **Best For** (`custom.best_for`)
4. Add to Cart button
5. Product description (with optional `custom.description_image`)
6. **Features** section (`custom.features`)
7. **Details** section (`custom.details`)
8. **Care** section (`custom.care`)
9. Shipping & Returns section

**MyoVolt Template Display Order:**
1. Hero section (images, description, video)
2. Technical specifications
3. Treatment modes
4. Product highlights
5. Included items
6. Product description
7. Best For and Add to Cart

### Metafield Verification

**Data Verification:**
- All metafields verified against actual data exports from November 11, 2025
- Field types verified from CSV column headers
- Example values verified from actual product data

**Code Verification:**
- All metafield usage verified against theme code
- Code references include exact file paths and line numbers
- Display locations and formats verified
- Conditional rendering logic documented

**Usage Patterns:**
- Metafields use conditional rendering (`{% if metafield != blank %}`)
- List metafields use `{% for item in metafield.value %}` loops
- Metaobject references access `.value` property
- File references use Liquid filters (`image_url`, `video_tag`)

---

*This data guide is based on actual data exports from November 11, 2025. All metafields documented here exist in the McDavid product catalog.*


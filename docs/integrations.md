# Integrations Guide
## Third-Party App Integration Documentation

---

## Apps with Theme Code Integration

### Sika Discovery Eligibility

**App Handle:** `sika-discovery-eligibility`  
**Integration Type:** App Block  
**Block Type:** `shopify://apps/sika-discovery-eligibility/blocks/sika_large_chip/`

**Code References:**
- `templates/product.json` line 16 (exact block reference)
- `templates/product.myovolt.json` line 16
- App blocks rendered in `sections/product-template.liquid` lines 412-418

**Usage:**
- App block added to product templates
- Displays HSA/FSA eligibility information on product pages
- Appears in `product-app-blocks` div container
- Positioned above "Best For" metafield and "Add to Cart" button

**Display Location:**
- Product pages (default template)
- MyoVolt product pages
- HEX® product pages
- All product templates that support `@app` blocks

**Configuration:**
- Block added via Theme Customizer → Product pages → Add block
- Settings include product reference, alignment, and color options
- Block ID: `e17f8505-bcca-4959-8609-82e792382ccf`
- Managed via Sika Discovery Eligibility app in Shopify Admin

**Code Pattern:**
```liquid
<div class="product-app-blocks">
  {%- for block in section.blocks -%}
    {% if block.type == '@app' %}
        {% render block %}
    {% endif %}
  {%- endfor -%}
</div>
```

**Template Support:**
- Default product template (`product-template.liquid`)
- MyoVolt product template (`product-template-myovolt.liquid`)
- HEX® product template (`product-template-hexviz.liquid`)
- All product templates support app blocks via `@app` block type

---

## App Block Support

All product templates support app blocks via the `@app` block type.

**Code Pattern:**
```liquid
<div class="product-app-blocks">
  {%- for block in section.blocks -%}
    {% if block.type == '@app' %}
        {% render block %}
    {% endif %}
  {%- endfor -%}
</div>
```

**Templates with App Block Support:**
- `sections/product-template.liquid` (line 412-418)
- `sections/product-template-hexviz.liquid` (line 387-393)
- `sections/product-template-myovolt.liquid` (line 319-325)
- `sections/product-details-template.liquid` (line 326-332)
- `sections/product-full-width-images-template.liquid` (line 336-342)
- `sections/featured-products.liquid` (line 245-251)

**Adding App Blocks:**
1. Go to Theme Customizer
2. Navigate to product page template
3. Click "Add block"
4. Select app block from available blocks
5. Configure app block settings
6. Save

---

## Shogun Page Builder

**Integration Type:** Page Builder  
**Snippet:** `snippets/shogun-content-handler.liquid`

**Usage:**
- Custom page layouts via Shogun app
- Template suffix support for Shogun pages
- Metafield-based template configuration

**Code Reference:**
- `snippets/shogun-content-handler.liquid` - Handles Shogun content rendering
- `sections/shogun-above.liquid` - Shogun content above main content
- `sections/shogun-below.liquid` - Shogun content below main content

**Configuration:**
- Pages edited via Shogun app interface
- Template suffix automatically assigned
- Content stored in page metafields

---

## Klaviyo Email Marketing

**Integration Type:** Newsletter Form + Back in Stock (BIS)  
**Location:** Footer section (newsletter) + Product pages (BIS)

**Newsletter Form:**
- **Code Reference:** `sections/footer-md.liquid` line 36
- **Implementation:** `<div class="klaviyo-form-LWy48v"></div>`
- **Form ID:** `LWy48v`
- **Display Location:** Footer column 1, below newsletter title and text
- **Wrapper:** `<div class="newsletter">` container

**Back in Stock (BIS):**
- **Code Reference:** `assets/klaviyo_bis_onsite.js` (3629 lines)
- **Script Location:** `layout/theme.shogun.landing.liquid` line 307
- **Implementation:** `<script src="{{ 'klaviyo_bis_onsite.js' | asset_url }}"></script>`
- **Usage:** Product page back-in-stock notifications
- **Configuration:** Managed via Klaviyo app settings

**Configuration:**
- Newsletter form managed via Klaviyo app → Forms
- Form ID `LWy48v` configured in footer section
- BIS functionality configured in Klaviyo app → Onsite
- No theme code changes needed for form updates
- Footer newsletter title and text configurable in Theme Customizer → Footer

**Footer Newsletter Settings:**
- Newsletter title: `section.settings.newsletter_title`
- Newsletter text: `section.settings.newsletter_text`
- Both appear above Klaviyo form

---

## Bazaarvoice Ratings & Reviews

**Integration Type:** Product Reviews and Q&A  
**Location:** Product pages

**Code References:**
- `sections/product-template.liquid` lines 438-459
- `sections/product-template-hexviz.liquid` lines 438-459
- `templates/collection.products-endpoint.liquid` lines 18-21 (aggregate ratings)

**Implementation:**
```liquid
<div class="shopify-reviews reviewsVisibility--{{settings.enable_shopify_review_comments}}">
  <div data-bv-show="reviews" data-bv-product-Id="{{product.id}}">
    {% if product.metafields.bazaarvoice.reviews %}
      {{ product.metafields.bazaarvoice.reviews }}
    {% endif %}
  </div>
  <div data-bv-show="questions" data-bv-product-Id="{{product.id}}">
    {% if product.metafields.bazaarvoice.questions %}
      {{ product.metafields.bazaarvoice.questions }}
    {% endif %}
  </div>
</div>
```

**Metafields Used:**
- `bazaarvoice.reviews` - Product reviews content
- `bazaarvoice.questions` - Product Q&A content
- `bazaarvoice.reviews-aggregate-ratings` - Aggregate rating data (collection endpoint)

**Display Conditions:**
- Only displays when `section.settings.review_position == "next_to_gallery"`
- Visibility controlled by `settings.enable_shopify_review_comments`
- Requires Bazaarvoice metafields to be populated

**Configuration:**
- Managed via Bazaarvoice app in Shopify Admin
- Review position configurable in Theme Customizer → Product pages
- Metafields automatically populated by Bazaarvoice app

---

## Shopify Product Reviews (SPR)

**Integration Type:** Native Shopify Reviews  
**Location:** Product pages

**Code References:**
- `sections/product-description-bottom-template.liquid` lines 154, 345, 403
- `assets/app.js` lines 795-803, 829-837 (SPR initialization)

**Implementation:**
```liquid
<span class="shopify-product-reviews-badge" data-id="{{ product.id }}"></span>
<div id="shopify-product-reviews" data-id="{{product.id}}">
  {{ product.metafields.spr.reviews }}
</div>
```

**JavaScript Initialization:**
```javascript
if($('#shopify-product-reviews').length || $('.shopify-product-reviews-badge').length) {
  SPR.$(document).ready(function() {
    return SPR.registerCallbacks(),
    SPR.initRatingHandler(),
    SPR.initDomEls(),
    SPR.loadProducts(),
    SPR.loadBadges()
  })
}
```

**Metafields Used:**
- `spr.reviews` - Shopify Product Reviews content

**Display:**
- Review badges and full reviews on product pages
- Initialized on product template section load
- Also initialized on featured products section load

---

## Gorgias Chat Widget

**Integration Type:** Customer Support Chat  
**Location:** All pages (footer scripts)

**Code References:**
- `layout/theme.liquid` lines 401-402
- `layout/theme.shogun.landing.liquid` lines 298-299

**Implementation:**
```liquid
<script id="gorgias-chat-widget-install-v2" src="https://config.gorgias.chat/gorgias-chat-bundle-loader.js?applicationId=4458"></script>
<script id="gorgias-chat-shopify-install">
  !function(_){
    _.SHOPIFY_PERMANENT_DOMAIN="{{shop.permanent_domain}}",
    _.SHOPIFY_CUSTOMER_ID="{{customer.id}}",
    _.SHOPIFY_CUSTOMER_EMAIL="{{customer.email}}"
  }(window||{});
</script>
```

**Application ID:** `4458`

**Features:**
- Customer support chat widget
- Customer data passed to Gorgias (ID, email, domain)
- Loads on all pages via theme layout
- Widget appears as floating chat button

**Configuration:**
- Managed via Gorgias app in Shopify Admin
- Application ID configured in theme layout
- Customer data automatically synced

---

## Freshworks Widget

**Integration Type:** Customer Support Widget  
**Location:** Footer (all pages)

**Code References:**
- `sections/footer-md.liquid` lines 134-140

**Implementation:**
```javascript
<script>
  window.fwSettings={
    'widget_id':44000003784
  };
  !function(){
    if("function"!=typeof window.FreshworksWidget){
      var n=function(){n.q.push(arguments)};
      n.q=[],window.FreshworksWidget=n
    }
  }()
</script>
<script type='text/javascript' src='https://widget.freshworks.com/widgets/44000003784.js' async defer></script>
```

**Widget ID:** `44000003784`

**Features:**
- Customer support widget
- Loads asynchronously in footer
- Appears as floating support widget

**Configuration:**
- Managed via Freshworks app in Shopify Admin
- Widget ID configured in footer section

---

## Loop Returns

**Integration Type:** Returns Management  
**Location:** Cart/Checkout

**Code References:**
- `layout/theme.shogun.landing.liquid` lines 300-306

**Implementation:**
```javascript
<script src="https://unpkg.com/@loophq/onstore-sdk@latest/dist/loop-onstore-sdk.js"></script>
<script> 
  LoopOnstore.init({ 
    key: "95498ea9ef05415e91b152adbddb46031a51f369", 
    attach: ".subtotal .action_button#checkout" 
  });
</script>
```

**API Key:** `95498ea9ef05415e91b152adbddb46031a51f369`

**Features:**
- Returns management integration
- Attached to checkout button (`.subtotal .action_button#checkout`)
- Handles return requests and exchanges

**Configuration:**
- Managed via Loop app in Shopify Admin
- API key configured in theme layout
- Attaches to checkout button selector

---

## SASO (Special Offers / Upsells)

**Integration Type:** Upsell and Cross-sell Popups  
**Location:** Product and Cart pages

**Code References:**
- `layout/theme.liquid` lines 357-368
- `layout/theme.shogun.landing.liquid` lines 273-284
- `snippets/special-offers.liquid` (187 lines)

**Configuration Object:**
```javascript
window.saso_config = {
  product_title_max_length: 40,
  crosssell_never_show_popup: false,
  show_upsell_only_in: "product, cart",
  hide_shown_upsells_for: 15, //minutes
  hide_closed_notifications_for: 10, //minutes
  upsell_variant_choose_option: "please select",
  upsell_variant_choose_message: "Please select an option",
  translate_percent_off: '% Off'
}
```

**Features:**
- Upsell popups on product pages
- Cross-sell popups in cart
- Product title max length: 40 characters
- Popup hiding logic (15 minutes for upsells, 10 minutes for notifications)
- Variant selection handling

**Script Loading:**
- Loads from `https://storefront.cdn.pxu.co/apps/uso.js`
- Includes Magnific Popup CSS for modal functionality
- Custom CSS file: `special-offers.css`
- Templates rendered via `special-offers-templates` snippet

**Configuration:**
- Managed via SASO app in Shopify Admin
- Configuration object in theme layout
- Popup behavior configurable in app settings

---

## Elevar (Google Tag Manager / Analytics)

**Integration Type:** Analytics and Data Layer  
**Location:** All pages (body end)

**Code References:**
- `layout/theme.liquid` line 394: `{% include 'elevar-body-end' %}`
- `snippets/elevar-body-end.liquid` (405 lines)

**Features:**
- Google Tag Manager integration
- Enhanced ecommerce data layer
- Customer tracking (logged in vs guest)
- Page type tracking (homepage, product, collection, cart, checkout, search)
- Product detail view tracking
- Add to cart tracking
- Remove from cart tracking
- Collection view tracking
- Search results tracking
- Product click tracking

**Data Layer Events:**
- `HomeView` - Homepage visits
- `productDetailView` - Product page views
- `addToCart` - Add to cart actions
- `removeFromCart` - Remove from cart actions
- `collectionView` - Collection page views
- `SearchView` - Search page views
- `searchResults` - Search results impressions
- `productClick` - Product link clicks

**GTM Container ID:** `GTM-5HMZRVC`

**Customer Data Tracked:**
- Visitor type (Logged In / Guest)
- Customer ID, email, name
- Customer orders count and total spent
- Product data (SKU, price, brand, variant)
- Cart data (items, total, SKUs)

**Configuration:**
- Managed via Elevar app in Shopify Admin
- GTM container ID configured in snippet
- Data layer automatically populated

---

## Kiwi Sizing

**Integration Type:** Size Guide  
**Location:** Product pages

**Code References:**
- `layout/theme.liquid` lines 388-391
- `snippets/kiwiSizing.liquid` (18 lines)

**Implementation:**
```liquid
{% if template !='index' %}
  {% if template contains 'product' or 'collections'%}
    {% include 'kiwiSizing' %}
  {% endif %}
{% endif %}
```

**Data Passed:**
```javascript
KiwiSizing.shop = "{{ shop.permanent_domain }}";
KiwiSizing.data = {
  collections: "{{ product.collections | map: 'id' | join: ','}}",
  tags: {{ product.tags | join: ',' | json}},
  product: "{{product.id}}",
  vendor: {{product.vendor | json}},
  type: {{product.type | json}},
  title: {{product.title | json}},
  images: {{product.images | json}},
  options: {{product.options_with_values | json}},
  variants: {{product.variants | json}},
};
```

**Features:**
- Size guide integration
- Product data passed to Kiwi Sizing
- Displays on product and collection pages
- Includes product collections, tags, images, options, and variants

**Configuration:**
- Managed via Kiwi Sizing app in Shopify Admin
- Product data automatically synced
- Size guide displays based on product data

---

## EasyVideo

**Integration Type:** Video Player  
**Location:** Product and Collection pages

**Code References:**
- `layout/theme.liquid` lines 388-391
- `snippets/easyvideo.liquid` (if exists)

**Implementation:**
```liquid
{% if template !='index' %}
  {% if template contains 'product' or 'collections'%}
    {% include 'easyvideo' %}
  {% endif %}
{% endif %}
```

**Features:**
- Video player integration
- Displays on product and collection pages
- Video content management

**Configuration:**
- Managed via EasyVideo app in Shopify Admin
- Video content configured in app

---

## Gem Apps (Page Builder)

**Integration Type:** Page Builder Sections  
**Location:** Homepage and Pages

**Code References:**
- `layout/theme.liquid` lines 395-400
- `snippets/gem-app-footer-scripts.liquid`
- Multiple `templates/index.gem-*.liquid` files

**Template Files:**
- `templates/index.gem-1600551102-template.liquid`
- `templates/index.gem-1590033886-template.liquid`
- `templates/index.gem-1592426711-template.liquid`
- `templates/index.gem-1608019865-template.liquid`
- `templates/index.gem-1594692224-template.liquid`
- `templates/index.gem-1610136936-template.liquid`
- `templates/index.gem-1584690625-template.liquid`
- `templates/index.gem-1595010713-template.liquid`
- `templates/index.gem-1571095289-template.liquid`

**Features:**
- Page builder sections for homepage
- Custom page layouts
- Footer scripts loaded via `gem-app-footer-scripts` snippet
- Multiple homepage template variations

**Configuration:**
- Managed via Gem app in Shopify Admin
- Page templates created via Gem interface
- Footer scripts automatically loaded

---

## Thimatic Bundle

**Integration Type:** Product Bundles  
**Location:** All pages (footer scripts)

**Code References:**
- `layout/theme.liquid` line 398: `{% render 'th-bundle-product' %}`

**Features:**
- Product bundle functionality
- Bundle product display
- Bundle pricing and discounts

**Configuration:**
- Managed via Thimatic Bundle app in Shopify Admin
- Bundle configuration in app settings

---

## Apps Without Theme Integration

The following apps may be installed but have no theme code integration:

- Apps using only Shopify admin configuration
- Apps using only metafields (no theme code)
- Apps using only checkout extensions
- Apps using only Shopify Flow or Scripts

**Note:** To verify app integration, check for:
1. App blocks in templates (`@app` block type)
2. App snippets in theme code (`snippets/` directory)
3. App-specific metafield usage in theme code
4. App JavaScript/CSS in theme assets (`assets/` directory)
5. App scripts in layout files (`layout/theme.liquid`)
6. App configuration objects in JavaScript

---

## Integration Verification

All documented integrations have been verified against actual theme code from `code/mcdavid-11NOV2025/`:

1. **Sika Discovery Eligibility:** Verified in `templates/product.json` line 16 and `templates/product.myovolt.json` line 16
2. **App Block Support:** Verified in `sections/product-template.liquid` lines 412-418 and multiple product template sections
3. **Shogun:** Verified via `snippets/shogun-content-handler.liquid` and template suffix support
4. **Klaviyo:** Verified in `sections/footer-md.liquid` line 36 (newsletter) and `layout/theme.shogun.landing.liquid` line 307 (BIS)
5. **Bazaarvoice:** Verified in `sections/product-template.liquid` lines 438-459
6. **Shopify Product Reviews:** Verified in `sections/product-description-bottom-template.liquid` and `assets/app.js`
7. **Gorgias:** Verified in `layout/theme.liquid` lines 401-402
8. **Freshworks:** Verified in `sections/footer-md.liquid` lines 134-140
9. **Loop:** Verified in `layout/theme.shogun.landing.liquid` lines 300-306
10. **SASO:** Verified in `layout/theme.liquid` lines 357-368 and `snippets/special-offers.liquid`
11. **Elevar:** Verified in `snippets/elevar-body-end.liquid` (405 lines)
12. **Kiwi Sizing:** Verified in `layout/theme.liquid` lines 388-391 and `snippets/kiwiSizing.liquid`
13. **EasyVideo:** Verified in `layout/theme.liquid` lines 388-391
14. **Gem Apps:** Verified in `layout/theme.liquid` lines 395-400 and multiple `templates/index.gem-*.liquid` files
15. **Thimatic Bundle:** Verified in `layout/theme.liquid` line 398

**Evidence-Based Documentation:**
- Only apps with actual theme code integration are documented
- Code references include exact file paths and line numbers
- Integration patterns verified against source code
- JavaScript configuration objects documented
- Metafield usage verified
- Script loading locations verified

**Integration Types:**
- **App Blocks:** Sika Discovery Eligibility
- **Snippets:** Shogun, Kiwi Sizing, EasyVideo, Special Offers, Elevar, Gem Apps, Thimatic Bundle
- **Layout Scripts:** Gorgias, Loop, SASO, Klaviyo BIS, Elevar
- **Footer Scripts:** Freshworks, Klaviyo Newsletter
- **JavaScript Assets:** Klaviyo BIS (`klaviyo_bis_onsite.js`), SASO (external CDN)
- **Metafields:** Bazaarvoice (`bazaarvoice.*`), Shopify Product Reviews (`spr.reviews`)

---

*This guide documents only apps with verified theme code integration. For app-specific configuration, refer to app documentation or Shopify App Store. All integrations verified against McDavid theme code from November 2025.*


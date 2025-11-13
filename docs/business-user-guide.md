# Business User Guide
## Content Management Workflows for USB - McDavid

---

## Table of Contents

1. [Navigation & Menu Management](#navigation--menu-management)
2. [Content Management](#content-management)
3. [Product Management](#product-management)
4. [Launching New Products](#launching-new-products)
5. [Common Tasks](#common-tasks)
6. [Troubleshooting](#troubleshooting)

---

## Navigation & Menu Management

### Menu-to-Section Mapping Table

This table shows exactly which menu setting in Theme Customizer controls which visible navigation element on your site.

| **Menu Setting**      | **Theme Customizer Location**  | **Visible Element**                       | **Desktop Behavior**                                 | **Mobile Behavior**            |
| --------------------- | ------------------------------ | ----------------------------------------- | ---------------------------------------------------- | ------------------------------ |
| `main_linklist`       | Header section → Main menu     | Main desktop navigation menu (horizontal) | Displays as horizontal menu with mega menu dropdowns | Included in mobile menu drawer |
| `footer_column2_menu` | Footer section → Column 2 menu | Footer column 2 links                     | Displays in footer column 2                          | Same as desktop                |
| `footer_column3_menu` | Footer section → Column 3 menu | Footer column 3 links                     | Displays in footer column 3                          | Same as desktop                |
| `footer_column4_menu` | Footer section → Column 4 menu | Footer column 4 links                     | Displays in footer column 4                          | Same as desktop                |

**Code Verification:**
- Header menu: `sections/header-md.liquid` line 106: `linklists[section.settings.main_linklist]`
- Footer menus: `sections/footer-md.liquid` lines 61, 71, 81: `linklists[section.settings.footer_column2_menu]`, etc.

### Header Navigation

The header contains the main site navigation and several configurable elements.

#### Main Menu

**Location:** Theme Customizer → Header section → Main menu setting

**How to Update:**
1. Go to **Shopify Admin** → **Online Store** → **Navigation**
2. Find or create the menu you want to use (e.g., "Main menu")
3. Add/edit menu items (collections, pages, products, or custom links)
4. Go to **Theme Customizer** → **Header** section
5. Select your menu from the **Main menu** dropdown
6. Click **Save**

**Menu Features:**
- **Nested menus (submenus)** - Create parent items with child items in Shopify Admin
- **Mega menu support** - Automatically displays when menu items have submenus
  - Multi-column layout based on number of submenu items
  - First column shows "Browse All" and main submenu items
  - Additional columns show submenu categories with their items
  - Special formatting: Menu items with `**` are bolded, items with `%%` show descriptions
- **Mega menu descriptions** - Add descriptions to menu items via Theme Customizer blocks
- **Mega menu promo blocks** - Add promotional content to mega menus
  - Configure in Theme Customizer → Header section → Blocks
  - Add "Mega menu promo" block
  - Match trigger to menu item handle (case-sensitive)
  - Include image, pre-header, header, and link
- **HEX® logo support** - Menu item titled exactly "HEX®" automatically displays the HEX logo image instead of text
- **SportMed® branding** - Menu items titled "Braces & Supports" automatically display as "SportMed®" in mega menu
- **Custom link support** - Can link to external URLs, internal pages, or anchor links

**Desktop Display:**
- Horizontal menu bar at top of page
- Mega menu dropdowns appear on hover for items with submenus
- Search icon, account icon, and cart icon on the right

**Mobile Display:**
- Hamburger menu icon opens mobile menu drawer
- All menu items appear in vertical list
- Search icon accessible from mobile header

#### Header Elements (Non-Menu)

**Logo:**
- Location: Theme Customizer → Header section → Logo settings
- Two logo options: 
  - **White logo** - Displays on homepage (when header is over banner content)
  - **Colored logo** - Displays on all other pages
- Recommended size: 40px height
- Logo automatically links to homepage
- Logo switches automatically based on page type

**Help Banner/Announcement Bar:**
- Location: Theme Customizer → Header section → Help text settings
- **Up to 3 rotating messages** - Messages automatically rotate if multiple are active
- **Date-based scheduling:**
  - Each message can have a start date and end date
  - Format: `yyyy-mm-dd hh:mm:ss` (e.g., `2025-11-13 00:00:00`)
  - Messages only display during their scheduled date range
  - Leave dates blank for messages that should always show
- **Customization options:**
  - Text color (`help_text_color`)
  - Background color (`help_text_bg_color`)
  - Link color (`help_text_link_color`)
- **Character limit:** Maximum 170 characters per message
- **Brace Finder Link:**
  - Optional link that appears on the right side of help banner
  - Enable via "SHOW Brace Finder" checkbox
  - Configure label text and URL
  - Customize background and text colors
  - Only displays on desktop (hidden on mobile/tablet)
  - Location: Theme Customizer → Header section → Brace Finder link settings

**Search:**
- Always enabled in McDavid header
- Search icon appears in header icons area (desktop) and mobile header
- Search functionality configured via global theme settings

**Account & Cart:**
- Account icon appears if customer accounts are enabled
- Cart icon with live item count
- Both appear in header icons area (right side)
- Cart opens as slide-out drawer

### Footer Navigation

The footer uses a block-based system with multiple columns.

#### Footer Structure

**Column 1 (Left):**
- Footer logo image
- Newsletter signup (Klaviyo form)
- Social media icons (Instagram, TikTok, Facebook, YouTube, Twitter/X)

**Columns 2, 3, 4:**
- Each column has a title and menu
- Menus assigned via Theme Customizer → Footer section
- Each column menu is independent

**Column 5 (Right - Wide Column):**
- USB logo image (desktop only)
- Payment icons
- Copyright text

#### How to Update Footer Menus

1. Go to **Shopify Admin** → **Online Store** → **Navigation**
2. Create or edit the menu you want to use (e.g., "Footer Column 2")
3. Add menu items (pages, collections, or custom links)
4. Go to **Theme Customizer** → **Footer** section
5. Find the column you want to update (Column 2, 3, or 4)
6. Enter the column title in the **Column X title** field
7. Select your menu from the **Column X menu** dropdown
8. Click **Save**

**Footer Menu Features:**
- Simple link lists (no nested menus in footer)
- Each column is independent
- Column titles are configurable
- Menus can be left empty (column won't display)

### Creating Menus in Shopify Admin

**Step-by-Step:**

1. **Navigate to Navigation:**
   - Go to **Shopify Admin** → **Online Store** → **Navigation**

2. **Create New Menu:**
   - Click **Add menu**
   - Enter menu name (e.g., "Main menu", "Footer Column 2")
   - Click **Add menu**

3. **Add Menu Items:**
   - Click **Add menu item**
   - Choose item type:
     - **Collection** - Links to a product collection
     - **Page** - Links to a content page
     - **Product** - Links to a product page
     - **HTTP** - Custom URL (internal or external)
   - Enter the item details
   - Click **Add**

4. **Create Nested Menus (Submenus):**
   - Add a parent menu item first
   - Click **Add menu item** again
   - Choose your item type
   - **Important:** Before clicking Add, look for the **Parent item** dropdown
   - Select the parent item from the dropdown
   - Click **Add**
   - The submenu item will appear indented under the parent

5. **Reorder Menu Items:**
   - Drag and drop menu items to reorder
   - Drag submenu items to change their parent
   - Changes save automatically

**Menu Item Types:**
- **Collection:** Links to a product collection page
- **Page:** Links to a content page
- **Product:** Links to a specific product page
- **HTTP:** Custom URL - can be:
  - Internal page: `/pages/about-us`
  - External site: `https://example.com`
  - Anchor link: `#section-name`
  - Placeholder: `#` (for parent items that only have submenus)

### Desktop vs. Mobile Behavior

**Desktop Navigation:**
- Main menu displays horizontally across header
- Mega menus appear on hover
- Footer menus display in columns
- All menus always visible

**Mobile Navigation:**
- Main menu hidden behind hamburger icon
- Tapping hamburger opens full-screen menu drawer
- Footer menus stack vertically
- Mobile menu includes all header menu items

---

## Content Management

### Editing Pages

**Step-by-Step:**

1. Go to **Shopify Admin** → **Online Store** → **Pages**
2. Find the page you want to edit
3. Click the page title to open it
4. Edit the page content in the content editor
5. Update page title, SEO settings, or template if needed
6. Click **Save**

**Page Templates Available:**
- Default page template
- Page with sidebar
- Page with banner
- Page details template
- Multi-column page template
- Gallery template
- FAQ template
- Contact template

**To Change Page Template:**
1. Open the page in Shopify Admin
2. Scroll to **Search engine listing** section
3. Find **Template** dropdown
4. Select the template you want
5. Click **Save**

### Creating New Pages

1. Go to **Shopify Admin** → **Online Store** → **Pages**
2. Click **Add page**
3. Enter page title
4. Add page content
5. Set visibility (visible/hidden)
6. Configure SEO settings
7. Select template (if different from default)
8. Click **Save**

**Page Visibility:**
- **Visible:** Page is live and accessible via URL
- **Hidden:** Page exists but is not listed in navigation (can still be accessed via direct URL)

### Shogun Page Builder

Some pages use Shogun page builder for custom layouts and advanced design options.

**Identifying Shogun Pages:**
- Pages with template suffix like `shogun-68f1425c049b6e3f42882321`
- Pages edited via Shogun app interface (not standard Shopify page editor)
- Homepage can use Shogun (template: `index.shogun-68f1425c049b6e3f42882321`)

**Editing Shogun Pages:**
1. Go to **Shogun** app in Shopify Admin
2. Find your page in the Shogun page list
3. Click to edit
4. Use Shogun's visual drag-and-drop editor to make changes
5. Add sections, images, text, buttons, and custom HTML
6. Preview changes before publishing
7. Click **Publish** when done

**Shogun Features:**
- Visual page builder with drag-and-drop interface
- Pre-built sections and components
- Custom HTML/CSS support
- Mobile-responsive editing
- A/B testing capabilities
- Advanced styling options

**Important Notes:**
- Shogun pages are separate from standard Shopify pages
- Changes made in Shogun override standard page content
- Shogun pages require Shogun app subscription
- Contact technical team if you need to convert a Shogun page to standard page

---

## Product Management

### Editing Product Information

**Step-by-Step:**

1. Go to **Shopify Admin** → **Products**
2. Find the product you want to edit
3. Click the product title to open it
4. Edit product details:
   - Title, description, vendor
   - Product images
   - Variants (sizes, colors, etc.)
   - Pricing
   - Inventory
   - SEO settings
5. Click **Save**

### Product Images

**Image Requirements:**
- Recommended size: 1000x1000px minimum
- Square format preferred
- High quality, well-lit product photos
- Multiple angles recommended

**Adding Product Images:**
1. Open product in Shopify Admin
2. Scroll to **Media** section
3. Click **Add files** or drag images
4. Reorder images by dragging (first image is featured)
5. Add alt text for accessibility
6. Click **Save**

### Product Variants

**Creating Variants:**
1. Open product in Shopify Admin
2. Scroll to **Variants** section
3. Click **Add variant**
4. Select option names (Size, Color, etc.)
5. Enter option values
6. Set price, SKU, inventory for each variant
7. Click **Save**

**Variant Options:**
- Common options: Size, Color, Style
- Can have up to 3 option types per product
- Each combination creates a separate variant

### Product Metafields

Products use metafields for additional information that displays on product pages and in search results.

**Common Product Metafields:**

**`custom.best_for`** - Product use case description
- Displays on product pages as "Best For:" section
- Example: "Moderate support for minor to moderate sprains, strains and wrist instability"
- Single line text field

**`custom.product_family`** - Product line identifier
- Links products in the same product family
- Used for product recommendations and grouping
- Example: "MDP300"
- List of product references

**`custom.features`** - Product feature highlights
- References Features metaobject
- Displays as feature list on product pages
- Each feature has a title and description
- List of metaobject references

**`custom.details`** - Product detail points
- Displays as bulleted list on product pages
- Example: ["FITS LEFT OR RIGHT WRIST", "UNISEX", "HSA/FSA ELIGIBLE"]
- List of single line text fields

**`custom.care`** - Care instructions
- Displays care and maintenance information
- Example: ["Hand wash. Air dry only."]
- List of single line text fields

**`custom.description_image`** - Additional description image
- Image displayed in product description area
- File reference

**`custom.free_shipping_returns`** - Free shipping and returns information
- Rich text field for shipping/returns policy
- Displays on product pages

**`pdp.swatch_color`** - Color swatch value
- Used for color variant display
- Example: "#000000"
- Single line text field

**`pdp.swatch_image`** - Color swatch image
- Image used for color variant swatch
- Single line text field

**Editing Metafields:**
1. Open product in Shopify Admin
2. Scroll to **Metafields** section (may need to enable in settings)
3. Find the metafield you want to edit
4. Update the value
5. Click **Save**

**Important Notes:**
- Some metafields are managed via apps (Sika Discovery Eligibility, Google Shopping, etc.)
- Bulk metafield updates require technical assistance
- Features metafield requires creating/editing Features metaobjects first
- Contact technical team for bulk updates or complex metafield configurations

---

## Launching New Products

### Pre-Launch Checklist

- [ ] Product information complete (title, description, vendor)
- [ ] Product images uploaded (minimum 1, recommended 3-5)
- [ ] Variants created (sizes, colors, etc.)
- [ ] Pricing set for all variants
- [ ] Inventory quantities set
- [ ] Product tags added
- [ ] Product added to collections
- [ ] SEO title and description set
- [ ] Product template selected (if using custom template)
- [ ] Metafields populated (best_for, features, etc.)
- [ ] Product visibility set to "Visible"

### Step-by-Step Product Launch

1. **Create Product:**
   - Go to **Shopify Admin** → **Products** → **Add product**
   - Enter product title, description, vendor
   - Add product images
   - Set product type and tags

2. **Set Up Variants:**
   - Add variant options (Size, Color, etc.)
   - Set price for each variant
   - Enter SKU for each variant
   - Set inventory quantities

3. **Add to Collections:**
   - Scroll to **Collections** section
   - Select collections this product belongs to
   - Or add product to collections later

4. **Configure SEO:**
   - Scroll to **Search engine listing** section
   - Edit page title (if different from product title)
   - Add meta description
   - Preview how it will appear in search results

5. **Select Template (if needed):**
   - Most products use default template
   - **Special templates available:**
     - **HEX® visualization template** (`product.hexviz`)
       - For HEX® products with visualization features
       - Includes HEX®-specific product display
       - Contact technical team to determine if product should use this template
     - **MyoVolt product template** (`product.myovolt`)
       - For MyoVolt products with advanced features
       - Requires MyoVolt-specific metafields:
         - Hero images (desktop and mobile)
         - Hero description
         - Video
         - Technical specifications (4 specs with images)
         - Treatment modes (3 modes with images and descriptions)
         - Product highlights (2 highlights with images and descriptions)
         - Included items (images and text)
         - Product description
       - See "MyoVolt Product Setup" section below for details
   - **To assign template:**
     1. Open product in Shopify Admin
     2. Scroll to **Search engine listing** section
     3. Find **Template** dropdown
     4. Select template (default, hexviz, or myovolt)
     5. Click **Save**

6. **Set Visibility:**
   - Scroll to top of product page
   - Ensure **Product status** is set to **Active**
   - Click **Save**

7. **Verify Product:**
   - View product on live site
   - Check all images display correctly
   - Verify pricing and variants
   - Test add to cart functionality
   - Check mobile view

### Adding Products to Navigation

**Option 1: Add to Collection Menu**
- If product is in a collection that's in the menu, it's automatically accessible
- No additional steps needed

**Option 2: Add Product Directly to Menu**
1. Go to **Shopify Admin** → **Online Store** → **Navigation**
2. Find the menu you want to add product to
3. Click **Add menu item**
4. Select **Product** as item type
5. Search for and select your product
6. Click **Add**

**Option 3: Create Featured Products Section**
- Use homepage sections to feature new products
- Go to **Theme Customizer** → **Homepage**
- Add **Featured Products** section
- Select products to feature

---

## MyoVolt Product Setup

MyoVolt products use a special template with extensive metafield configuration. Follow these steps to set up a MyoVolt product.

### Prerequisites

- Product created in Shopify Admin
- Product template set to "MyoVolt" (`product.myovolt`)
- MyoVolt metafields available (namespace: `myovolt.*`)

### Step-by-Step MyoVolt Setup

1. **Set Product Template:**
   - Open product in Shopify Admin
   - Scroll to **Search engine listing** section
   - Select **MyoVolt** from Template dropdown
   - Click **Save**

2. **Configure Hero Section:**
   - **Hero Image (Desktop):** `myovolt.hero_image_desktop`
     - Upload high-quality product hero image for desktop view
     - Recommended: 1920px width
   - **Hero Image (Mobile):** `myovolt.hero_image_mobile`
     - Upload optimized hero image for mobile view
     - Recommended: 768px width
   - **Hero Description:** `myovolt.hero_description`
     - Enter product description for hero section
     - Multi-line text field

3. **Add Product Video (Optional):**
   - **Video:** `myovolt.video`
     - Upload product video file
     - File reference

4. **Configure Technical Specifications:**
   - **Tech Spec 1-4:** `myovolt.tech_spec_1` through `tech_spec_4`
     - Enter specification label (e.g., "Battery Life: 8 hours")
     - Single line text field
   - **Tech Spec Images:** `myovolt.tech_spec_1_image` through `tech_spec_4_image`
     - Upload image for each specification
     - File reference

5. **Set Up Treatment Modes:**
   - **Title:** `myovolt.treatment_modes_title`
     - Section title (e.g., "Treatment Modes")
   - **Subtitle:** `myovolt.treatment_modes_subtitle`
     - Section subtitle
   - **Mode 1-3 Images:** `myovolt.treatment_mode_1_image` through `treatment_mode_3_image`
     - Upload image for each treatment mode
   - **Mode 1-3 Descriptions:** `myovolt.treatment_mode_1_description` through `treatment_mode_3_description`
     - Enter description for each treatment mode
     - Rich text field (supports formatting)

6. **Configure Product Highlights:**
   - **Highlight 1-2 Images:** `myovolt.highlight_1_image`, `highlight_2_image`
     - Upload images for product highlights
   - **Highlight 1-2 Titles:** `myovolt.highlight_1_title`, `highlight_2_title`
     - Enter highlight titles
   - **Highlight 1-2 Descriptions:** `myovolt.highlight_1_description`, `highlight_2_description`
     - Enter highlight descriptions
     - Rich text field

7. **Set Up Included Items:**
   - **Included Image (Desktop):** `myovolt.included_image_desktop`
     - Upload image showing included items (desktop)
   - **Included Image (Mobile):** `myovolt.included_image_mobile`
     - Upload image showing included items (mobile)
   - **Included Items Text:** `myovolt.included_items`
     - Enter list of included items
     - Rich text field

8. **Add Product Description:**
   - **Description:** `myovolt.description`
     - Enter full product description
     - Rich text field (supports formatting, links, etc.)

### MyoVolt Metafield Checklist

- [ ] Hero image (desktop) uploaded
- [ ] Hero image (mobile) uploaded
- [ ] Hero description entered
- [ ] Video uploaded (if applicable)
- [ ] Technical specifications (1-4) configured with images
- [ ] Treatment modes title and subtitle entered
- [ ] Treatment modes (1-3) configured with images and descriptions
- [ ] Product highlights (1-2) configured with images, titles, and descriptions
- [ ] Included items images (desktop and mobile) uploaded
- [ ] Included items text entered
- [ ] Product description entered

---

## Mega Menu Configuration

The McDavid header supports advanced mega menu features including descriptions and promotional content.

### Adding Menu Item Descriptions

Menu item descriptions appear in the mega menu to provide additional context.

**Step-by-Step:**
1. Go to **Theme Customizer** → **Header** section
2. Scroll to **Blocks** section
3. Click **Add block**
4. Select **Mega menu description** block type
5. Configure settings:
   - **Trigger:** Enter the menu item handle (case-sensitive)
     - To find handle: Menu item title converted to lowercase with hyphens
     - Example: "Braces & Supports" → `braces-supports`
   - **Description:** Enter description text
6. Click **Save**

**Tips:**
- Descriptions appear below the menu item title in mega menu
- Use descriptions to explain what's in each menu section
- Keep descriptions concise (1-2 sentences)

### Adding Mega Menu Promotional Content

Promotional blocks appear in mega menus to highlight special offers or featured content.

**Step-by-Step:**
1. Go to **Theme Customizer** → **Header** section
2. Scroll to **Blocks** section
3. Click **Add block**
4. Select **Mega menu promo** block type
5. Configure settings:
   - **Trigger:** Enter the menu item handle (must match exactly, case-sensitive)
   - **Activate promo:** Check to enable promotional content
   - **Image:** Upload promotional image (recommended: 300px width)
   - **Pre-header:** Small text above main header (optional)
   - **Header:** Main promotional headline
   - **Link label:** Button/link text
   - **Link URL:** Destination URL for promotional link
6. Click **Save**

**Promo Block Features:**
- Appears as rightmost column in mega menu
- Image displays at top
- Pre-header, header, and link text below image
- Entire block can be clickable if link URL is provided
- Only displays for menu items with submenus

### Menu Item Formatting

Mega menu items support special formatting via menu item titles:

**Bold Text:**
- Add `**` around text in menu item title
- Example: `**New Arrivals**` displays as **New Arrivals**
- Use for emphasis on important menu items

**Menu Item Descriptions:**
- Add `%%` separator in menu item title
- Format: `Menu Item Title%%Description text`
- Example: `Knee Sleeves%%Premium protection for active athletes`
- Description appears below menu item title in mega menu

**Combining Formats:**
- Can combine bold and description: `**New**%%Just arrived!`
- Bold applies to title portion only

---

## Footer Configuration

### Newsletter Signup (Klaviyo)

The footer includes a Klaviyo newsletter signup form.

**Configuration:**
- Form is pre-configured with Klaviyo form ID: `LWy48v`
- Form managed via Klaviyo app
- To update form:
  1. Go to **Klaviyo** app in Shopify Admin
  2. Find form with ID `LWy48v`
  3. Edit form design and fields
  4. Changes reflect automatically on site

**Footer Newsletter Settings:**
- **Newsletter Title:** Theme Customizer → Footer → Newsletter title
- **Newsletter Text:** Theme Customizer → Footer → Newsletter text
- Both appear above the Klaviyo form

### Social Media Icons

Social media icons appear in footer column 1.

**Configured Icons:**
- Instagram
- TikTok
- Facebook
- YouTube
- Twitter/X

**Configuration:**
- Go to **Theme Customizer** → **Theme settings** → **Social media**
- Enter URLs for each platform:
  - `instagram_link`
  - `tiktok_link`
  - `facebook_link`
  - `youtube_link`
  - `twitter_link`
- Icons automatically appear in footer when URLs are provided
- Icons open in new tab

### Footer Logo and USB Logo

**Footer Logo:**
- Location: Theme Customizer → Footer section → Footer logo image
- Displays in footer column 1 (left)
- Recommended size: Appropriate for footer space

**USB Logo:**
- Location: Theme Customizer → Footer section → Footer USB logo
- Displays in footer column 5 (right, wide column)
- Only displays on desktop (hidden on mobile)
- Recommended size: Appropriate for footer space

---

## Common Tasks

### Updating Product Prices

1. Go to **Shopify Admin** → **Products**
2. Open the product
3. Scroll to **Variants** section
4. Click the price field for the variant
5. Enter new price
6. Click **Save**

**Bulk Price Updates:**
- Use Shopify's bulk editor or import/export
- Contact technical team for assistance with bulk updates

### Changing Product Images

1. Open product in Shopify Admin
2. Scroll to **Media** section
3. To replace an image: Click the image → **Replace**
4. To add images: Click **Add files**
5. To reorder: Drag images to desired order
6. Click **Save**

### Updating Menu Items

1. Go to **Shopify Admin** → **Online Store** → **Navigation**
2. Find the menu containing the item
3. Click the menu item to edit
4. Update title, URL, or item type
5. Click **Save**

**To Remove Menu Item:**
- Click the menu item
- Click **Delete** or remove the item
- Changes save automatically

### Adding New Collection to Menu

1. **Create Collection (if needed):**
   - Go to **Shopify Admin** → **Products** → **Collections**
   - Click **Create collection**
   - Set up collection details
   - Add products to collection

2. **Add Collection to Menu:**
   - Go to **Shopify Admin** → **Online Store** → **Navigation**
   - Find the menu (Main menu, Footer menu, etc.)
   - Click **Add menu item**
   - Select **Collection**
   - Search for and select your collection
   - Click **Add**

3. **Assign Menu in Theme Customizer:**
   - Go to **Theme Customizer** → **Header** (or **Footer**)
   - Select your menu from the appropriate dropdown
   - Click **Save**

---

## Troubleshooting

### Menu Not Appearing on Site

**Checklist:**
- [ ] Menu created in Shopify Admin → Navigation
- [ ] Menu assigned in Theme Customizer → Header/Footer section
- [ ] Menu has at least one menu item
- [ ] Menu items are set to visible
- [ ] Changes saved in Theme Customizer

**Solution:**
1. Verify menu exists in Shopify Admin → Navigation
2. Go to Theme Customizer → Header section
3. Check that correct menu is selected in "Main menu" dropdown
4. Click **Save** in Theme Customizer
5. Refresh site to see changes

### Product Not Showing in Collection

**Checklist:**
- [ ] Product is active (not draft or archived)
- [ ] Product is added to the collection
- [ ] Collection is published
- [ ] Product has inventory (if inventory tracking enabled)

**Solution:**
1. Open product in Shopify Admin
2. Check product status (should be "Active")
3. Scroll to **Collections** section
4. Verify product is in the correct collection
5. If using smart collection, check collection conditions match product

### Images Not Displaying

**Checklist:**
- [ ] Image file uploaded successfully
- [ ] Image file format supported (JPG, PNG, GIF, WebP)
- [ ] Image file size not too large
- [ ] Product saved after adding image

**Solution:**
1. Try re-uploading the image
2. Check image file size (recommended under 2MB)
3. Ensure image is in supported format
4. Clear browser cache and refresh

### Footer Menu Not Updating

**Checklist:**
- [ ] Menu updated in Shopify Admin → Navigation
- [ ] Correct menu selected in Theme Customizer → Footer
- [ ] Column title and menu both configured
- [ ] Changes saved in Theme Customizer

**Solution:**
1. Verify menu changes in Shopify Admin → Navigation
2. Go to Theme Customizer → Footer section
3. Check that correct menu is selected for the column
4. Ensure column title is entered
5. Click **Save**
6. Refresh site

### Help Banner Not Displaying

**Checklist:**
- [ ] Help text entered in Theme Customizer → Header
- [ ] Start/end dates are correct (if using date ranges)
- [ ] Date format is correct: `yyyy-mm-dd hh:mm:ss`
- [ ] Current date is within start/end date range (if dates set)
- [ ] Changes saved in Theme Customizer

**Solution:**
1. Go to Theme Customizer → Header section
2. Check Help text fields (Help text, Help text 2, Help text 3)
3. Verify date ranges if using scheduled messages
4. Ensure at least one help text field has content
5. Check date format matches: `2025-11-13 00:00:00`
6. Click **Save**
7. Refresh site

### Mega Menu Not Showing Promo Content

**Checklist:**
- [ ] Mega menu promo block added in Theme Customizer → Header → Blocks
- [ ] Trigger matches menu item handle exactly (case-sensitive)
- [ ] "Activate promo" checkbox is checked
- [ ] Menu item has submenus (promo only shows for items with submenus)
- [ ] Changes saved in Theme Customizer

**Solution:**
1. Verify menu item has submenus in Shopify Admin → Navigation
2. Find the menu item handle (title converted to lowercase with hyphens)
3. Go to Theme Customizer → Header → Blocks
4. Check that trigger in promo block matches handle exactly
5. Ensure "Activate promo" is checked
6. Click **Save**

### MyoVolt Product Not Displaying Correctly

**Checklist:**
- [ ] Product template set to "MyoVolt"
- [ ] Required MyoVolt metafields populated
- [ ] Images uploaded for hero, tech specs, treatment modes, highlights
- [ ] Text fields filled in
- [ ] Product saved after metafield updates

**Solution:**
1. Verify product template is "MyoVolt" in Shopify Admin
2. Check that all required MyoVolt metafields have values
3. Ensure images are uploaded and not broken
4. Verify text fields are not empty
5. Save product and refresh product page

### Need More Help?

- Review this guide for step-by-step instructions
- Check **Quick Reference** guide for common tasks
- Review **Data Guide** for complete metafield reference
- Contact technical team for advanced configuration
- Refer to Shopify Help Center for general Shopify questions

---

*This guide focuses on client-specific features and workflows. For general Shopify documentation, refer to Shopify's official help center.*


document.addEventListener('buybox:variantChanged', function (event) {
    const variant = event.detail.data;

    const skuEl = document.querySelectorAll('[data-sku]');
    if (skuEl) {
        if (variant && variant.sku) {
            skuEl.forEach((el) => {

                el.textContent = variant.sku;
            })
        }
    }

});

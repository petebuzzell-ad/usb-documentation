/*********************** Custom JS for Boost AI Search & Discovery  ************************/
window.__BoostCustomization__ = (window.__BoostCustomization__ ?? []).concat([
    (componentRegistry) => {
        componentRegistry.useComponentPlugin('SearchInput', {
            name: 'Customized Search Input',
            apply: () => ({
                afterRender: (element) => {
                    try {
                        const searchElms = document.querySelectorAll('.boost-sd__search-widget-init-input');
                        if (searchElms) {
                            searchElms.forEach(function(el) {
                                el.setAttribute('spellcheck', 'false');
                            });
                        }
                    } catch (e) {
                        console.warn(e);
                    }
                },
            }),
        });
    }
]);
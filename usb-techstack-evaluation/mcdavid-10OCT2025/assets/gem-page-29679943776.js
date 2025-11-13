

        jQuery(function() {
            var $hero = jQuery('#m-1560381291082');
            var $module = jQuery('#m-1560381291082').children('.module');

            var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
            if(mode == 'dev') {
                $hero.children('.hero-link').hide();
            }

            var height = jQuery.trim($module.attr('data-height'));
            if(height == undefined || height == '') {
                $hero.attr('style', 'height: auto!important');
                jQuery(window).resize(function(){
                    $hero.attr('style', 'height: auto!important');
                });
            } else {
                $hero.removeAttr('style');
            }

            var effect = $module.attr('data-effect');
            var transition = $module.attr('data-transition');

            if(effect == 'effect-zoom') {   
                $module.parent().addClass(effect);  

                setTimeout(function() {
                    var backgroundImage = $module.parent().css('background-image');
                    var backgroundSize = $module.parent().css('background-size');
                    var backgroundPosition = $module.parent().css('background-position');
                    $module.siblings('.gf_hero-bg-wrap').css({
                        'background-image'      : 'inherit',
                        'background-size'       : 'inherit',
                        'background-position'   : 'inherit',
                        '-webkit-transition'    : 'transform ' + transition + 's ease-in-out',
                        '-moz-transition'       : 'transform ' + transition + 's ease-in-out',
                        '-ms-transition'        : 'transform ' + transition + 's ease-in-out',
                        '-o-transition'         : 'transform ' + transition + 's ease-in-out',
                        'transition'            : 'transform ' + transition + 's ease-in-out'
                    })
                    $module.siblings('.gf_hero-bg-wrap').children('.gf_hero-bg').css({
                        'background-image'      : 'inherit',
                        'background-size'       : 'inherit',
                        'background-position'   : 'inherit',
                        '-webkit-transition'    : 'transform ' + transition + 's ease-in-out',
                        '-moz-transition'       : 'transform ' + transition + 's ease-in-out',
                        '-ms-transition'        : 'transform ' + transition + 's ease-in-out',
                        '-o-transition'         : 'transform ' + transition + 's ease-in-out',
                        'transition'            : 'transform ' + transition + 's ease-in-out'
                    });
                }, 300);
            }

            if($module.attr('data-fixedMode') == '1'){
                $module.parent().attr('style', 'padding-top: 0px!important; padding-bottom: 0px!important; height: auto!important; background-image: none!important;max-width: 100%!important;');

                jQuery(window).resize(function(){
                    var backgroundImage =  $module.parent().css('background-image');
                    $module.parent().attr('style', 'padding-top: 0px!important; padding-bottom: 0px!important; height: auto!important; background-image: none!important;max-width: 100%!important;');
                });
            } else {
                $module.parent().removeAttr('style');
            }
        });
    
        jQuery(function() {
            var $module = jQuery('#m-1560381291027').children('.module');   
            var navspeed = $module.data('navspeed'),
                autoplaytimeout = $module.data('autoplaytimeout'),
                autoplayhoverpause = $module.data('autoplayhoverpause'),
                navlg = $module.data('navlg'),
                navmd = $module.data('navmd'),
                navsm = $module.data('navsm'),
                navxs = $module.data('navxs'),
                collg = $module.data('collg'),
                colmd = $module.data('colmd'),
                colsm = $module.data('colsm'),
                colxs = $module.data('colxs'),
                dotslg = $module.data('dotslg'),
                dotsmd = $module.data('dotsmd'),
                dotssm = $module.data('dotssm'),
                dotsxs = $module.data('dotsxs'),
                marginlg = parseInt($module.data('marginlg')),
                marginmd = parseInt($module.data('marginmd')),
                marginsm = parseInt($module.data('marginsm')),
                marginxs = parseInt($module.data('marginxs'));

            var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
            if(mode == 'production') {
                var autoplay = $module.data('autoplay'), 
                    loop = $module.data('loop');
            } else {
                var autoplay = 0, 
                    loop = 0;
            }
        
            $module.owlCarousel({
                mouseDrag: false,
                autoplayHoverPause: autoplayhoverpause,
                autoplay: autoplay,
                autoplayTimeout: autoplaytimeout,
                loop: loop,
                navSpeed: navspeed,
                autoWidth: !1,
                responsiveClass:true,
                responsive:{
                    0:{
                        items:colxs,
                        nav: navxs,
                        dots:dotsxs,
                        margin: marginxs
                    },
                    768:{
                        items:colsm,
                        nav: navsm,
                        dots:dotssm,
                        margin: marginsm
                    },
                    992:{
                        items:colmd,
                        nav: navmd,
                        dots:dotsmd,
                        margin: marginmd
                    },
                    1200:{
                        items:collg,
                        nav: navlg,
                        dots:dotslg,
                        margin: marginlg
                    }
                }
            }); 
        }); 
    
    jQuery(function() {
        var $hero = jQuery('#m-1564010663967');
        var $module = jQuery('#m-1564010663967').children('.module');

        var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
        var $heroLink = $hero.children('.hero-link');
        if(mode == 'dev' && $heroLink.length > 0) {
             $hero.children('.hero-link').hide();
        }
        if (mode == 'production' && $heroLink.length > 0) {
            $module.off('click.openLink').on('click.openLink', function(e) {
                var $target = jQuery(e.target);
                if ($target.length > 0){
                    var linkTarget = typeof $target.attr('href') !== "undefined" ? $target.attr('href') : "";
                    if (linkTarget == "") {
                        var link = typeof $heroLink.attr('href') !== "undefined" ? $heroLink.attr('href') : "";
                        var newTab = typeof $heroLink.attr('target') !== "undefined" ? $heroLink.attr('target') : "";
                        if (link != "") {
                            if (newTab == "") {
                                window.location.href = link;
                            } else {
                                window.open(link, newTab);
                            }
                        }
                    }
                };
            })
        }

        var height = jQuery.trim($module.attr('data-height'));
        if(height == undefined || height == '') {
            $hero.attr('style', 'height: auto!important');
            jQuery(window).resize(function(){
                $hero.attr('style', 'height: auto!important');
            });
        } else {
            $hero.removeAttr('style');
        }

        var effect = $module.attr('data-effect');
        var transition = $module.attr('data-transition');

        if(effect == 'effect-zoom') {
            $module.parent().addClass(effect);

            setTimeout(function() {
                var backgroundImage = $module.parent().css('background-image');
                var backgroundSize = $module.parent().css('background-size');
                var backgroundPosition = $module.parent().css('background-position');
                $module.siblings('.gf_hero-bg-wrap').css({
                    'background-image'      : 'inherit',
                    'background-size'       : 'inherit',
                    'background-position'   : 'inherit',
                    '-webkit-transition'    : 'transform ' + transition + 's ease-in-out',
                    '-moz-transition'       : 'transform ' + transition + 's ease-in-out',
                    '-ms-transition'        : 'transform ' + transition + 's ease-in-out',
                    '-o-transition'         : 'transform ' + transition + 's ease-in-out',
                    'transition'            : 'transform ' + transition + 's ease-in-out'
                })
                $module.siblings('.gf_hero-bg-wrap').children('.gf_hero-bg').css({
                    'background-image'      : 'inherit',
                    'background-size'       : 'inherit',
                    'background-position'   : 'inherit',
                    '-webkit-transition'    : 'transform ' + transition + 's ease-in-out',
                    '-moz-transition'       : 'transform ' + transition + 's ease-in-out',
                    '-ms-transition'        : 'transform ' + transition + 's ease-in-out',
                    '-o-transition'         : 'transform ' + transition + 's ease-in-out',
                    'transition'            : 'transform ' + transition + 's ease-in-out'
                });
            }, 300);
        }

        if($module.attr('data-fixedMode') == '1'){
            $module.parent().attr('style', 'padding-top: 0px!important; padding-bottom: 0px!important; height: auto!important; background-image: none!important;max-width: 100%!important;');

            jQuery(window).resize(function(){
                var backgroundImage =  $module.parent().css('background-image');
                $module.parent().attr('style', 'padding-top: 0px!important; padding-bottom: 0px!important; height: auto!important; background-image: none!important;max-width: 100%!important;');
            });
        } else {
            $module.parent().removeAttr('style');
        }
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564445163817').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564445163817-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564445163817-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564445163817-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1564009706892').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564440870519').children('.module');
        $module.find('.video-popup').magnificPopup({
            type: 'iframe',
            iframe: {
                patterns: {
                    youtube: {
                        index: 'youtube.com/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    youtu: {
                        index: 'youtu.be/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    vimeo: {
                        index: 'vimeo.com/',
                        id: function(url) {
                            var m = url.match(/(https?:\/\/)?(www.)?(player.)?vimeo.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*/);
                            if ( !m || !m[5] ) return null;
                            return m[5];
                        },
                        src: '//player.vimeo.com/video/%id%?autoplay=1'
                    }
                }
            }
        });
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564445117531').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564445117531-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564445117531-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564445117531-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1564441051363').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564441051324').children('.module');
        $module.find('.video-popup').magnificPopup({
            type: 'iframe',
            iframe: {
                patterns: {
                    youtube: {
                        index: 'youtube.com/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    youtu: {
                        index: 'youtu.be/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    vimeo: {
                        index: 'vimeo.com/',
                        id: function(url) {
                            var m = url.match(/(https?:\/\/)?(www.)?(player.)?vimeo.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*/);
                            if ( !m || !m[5] ) return null;
                            return m[5];
                        },
                        src: '//player.vimeo.com/video/%id%?autoplay=1'
                    }
                }
            }
        });
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564446045097').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564446045097-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564446045097-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564446045097-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1564441201245').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564441201270').children('.module');
        $module.find('.video-popup').magnificPopup({
            type: 'iframe',
            iframe: {
                patterns: {
                    youtube: {
                        index: 'youtube.com/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    youtu: {
                        index: 'youtu.be/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    vimeo: {
                        index: 'vimeo.com/',
                        id: function(url) {
                            var m = url.match(/(https?:\/\/)?(www.)?(player.)?vimeo.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*/);
                            if ( !m || !m[5] ) return null;
                            return m[5];
                        },
                        src: '//player.vimeo.com/video/%id%?autoplay=1'
                    }
                }
            }
        });
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447198715').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447198715-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447198715-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447198715-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1564441340867').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564441340863').children('.module');
        $module.find('.video-popup').magnificPopup({
            type: 'iframe',
            iframe: {
                patterns: {
                    youtube: {
                        index: 'youtube.com/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    youtu: {
                        index: 'youtu.be/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    vimeo: {
                        index: 'vimeo.com/',
                        id: function(url) {
                            var m = url.match(/(https?:\/\/)?(www.)?(player.)?vimeo.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*/);
                            if ( !m || !m[5] ) return null;
                            return m[5];
                        },
                        src: '//player.vimeo.com/video/%id%?autoplay=1'
                    }
                }
            }
        });
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1564441646414').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564441646409').children('.module');
        $module.find('.video-popup').magnificPopup({
            type: 'iframe',
            iframe: {
                patterns: {
                    youtube: {
                        index: 'youtube.com/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    youtu: {
                        index: 'youtu.be/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    vimeo: {
                        index: 'vimeo.com/',
                        id: function(url) {
                            var m = url.match(/(https?:\/\/)?(www.)?(player.)?vimeo.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*/);
                            if ( !m || !m[5] ) return null;
                            return m[5];
                        },
                        src: '//player.vimeo.com/video/%id%?autoplay=1'
                    }
                }
            }
        });
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564448249178').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564448249178-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564448249178-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564448249178-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1564441560354').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564441560362').children('.module');
        $module.find('.video-popup').magnificPopup({
            type: 'iframe',
            iframe: {
                patterns: {
                    youtube: {
                        index: 'youtube.com/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    youtu: {
                        index: 'youtu.be/',
                        id: function(url) {
                            var id;
                            if (url.indexOf('youtu.be/') != -1) {
                                id = url.split('youtu.be/');
                            } else {
                                id = url.split(/watch\?v=/);
                            }
                            if (id && id[1] != undefined) {
                                id = id[1].split(/&/)[0];
                            }
                            return id;
                        },
                        src: '//www.youtube.com/embed/%id%?autoplay=1'
                    },
                    vimeo: {
                        index: 'vimeo.com/',
                        id: function(url) {
                            var m = url.match(/(https?:\/\/)?(www.)?(player.)?vimeo.com\/([a-z]*\/)*([0-9]{6,11})[?]?.*/);
                            if ( !m || !m[5] ) return null;
                            return m[5];
                        },
                        src: '//player.vimeo.com/video/%id%?autoplay=1'
                    }
                }
            }
        });
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564448039713').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564448039713-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564448039713-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564448039713-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564444935535').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564444935535-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564444935535-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564444935535-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1560807617647').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564620777008').children('.module');
        var videoUrl = jQuery.trim($module.attr('data-url'));
        var autoPause = $module.attr('data-autopause');
        var autoPlay = $module.attr('data-autoplay');
        var videoloop = $module.attr('data-videoloop');
        var videoMute = $module.attr('data-videomute');
        var byline = $module.attr('data-byline');
        var showtitle = $module.attr('data-showtitle');
        var showportrait = $module.attr('data-showportrait');

        setTimeout(function() {
            var videoWrapper = $module.children('.vimeo_video');
            videoWrapper.empty().append('<div id="vimeo-wrapper-1564620777008"></div>');

            var options = {
                url: videoUrl,
                loop: videoloop,
                autoplay: autoPlay,
                autopause: autoPause,
                byline: byline,
                title: showtitle,
                muted: videoMute,
                portrait: showportrait
            };
            var player = new Vimeo.Player("vimeo-wrapper-1564620777008", options);

        }, 100);
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1565137969868').children('.module');
        var videoUrl = jQuery.trim($module.attr('data-url'));
        var autoPause = $module.attr('data-autopause');
        var autoPlay = $module.attr('data-autoplay');
        var videoloop = $module.attr('data-videoloop');
        var videoMute = $module.attr('data-videomute');
        var byline = $module.attr('data-byline');
        var showtitle = $module.attr('data-showtitle');
        var showportrait = $module.attr('data-showportrait');

        setTimeout(function() {
            var videoWrapper = $module.children('.vimeo_video');
            videoWrapper.empty().append('<div id="vimeo-wrapper-1565137969868"></div>');

            var options = {
                url: videoUrl,
                loop: videoloop,
                autoplay: autoPlay,
                autopause: autoPause,
                byline: byline,
                title: showtitle,
                muted: videoMute,
                portrait: showportrait
            };
            var player = new Vimeo.Player("vimeo-wrapper-1565137969868", options);

        }, 100);
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564444982185').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564444982185-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564444982185-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564444982185-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1560808828103').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564449284286').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564449284286-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564449284286-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564449284286-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1564013972893').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564702811037').children('.module');
        var videoUrl = jQuery.trim($module.attr('data-url'));
        var autoPause = $module.attr('data-autopause');
        var autoPlay = $module.attr('data-autoplay');
        var videoloop = $module.attr('data-videoloop');
        var videoMute = $module.attr('data-videomute');
        var byline = $module.attr('data-byline');
        var showtitle = $module.attr('data-showtitle');
        var showportrait = $module.attr('data-showportrait');

        setTimeout(function() {
            var videoWrapper = $module.children('.vimeo_video');
            videoWrapper.empty().append('<div id="vimeo-wrapper-1564702811037"></div>');

            var options = {
                url: videoUrl,
                loop: videoloop,
                autoplay: autoPlay,
                autopause: autoPause,
                byline: byline,
                title: showtitle,
                muted: videoMute,
                portrait: showportrait
            };
            var player = new Vimeo.Player("vimeo-wrapper-1564702811037", options);

        }, 100);
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1565138494737').children('.module');
        var videoUrl = jQuery.trim($module.attr('data-url'));
        var autoPause = $module.attr('data-autopause');
        var autoPlay = $module.attr('data-autoplay');
        var videoloop = $module.attr('data-videoloop');
        var videoMute = $module.attr('data-videomute');
        var byline = $module.attr('data-byline');
        var showtitle = $module.attr('data-showtitle');
        var showportrait = $module.attr('data-showportrait');

        setTimeout(function() {
            var videoWrapper = $module.children('.vimeo_video');
            videoWrapper.empty().append('<div id="vimeo-wrapper-1565138494737"></div>');

            var options = {
                url: videoUrl,
                loop: videoloop,
                autoplay: autoPlay,
                autopause: autoPause,
                byline: byline,
                title: showtitle,
                muted: videoMute,
                portrait: showportrait
            };
            var player = new Vimeo.Player("vimeo-wrapper-1565138494737", options);

        }, 100);
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447402451').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447402451-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447402451-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447402451-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1564014293066').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564447782563').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447782563-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447782563-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447782563-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1564015110487').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
    jQuery(function() {
        var $module = jQuery('#m-1564626288027').children('.module');
        var videoUrl = jQuery.trim($module.attr('data-url'));
        var autoPause = $module.attr('data-autopause');
        var autoPlay = $module.attr('data-autoplay');
        var videoloop = $module.attr('data-videoloop');
        var videoMute = $module.attr('data-videomute');
        var byline = $module.attr('data-byline');
        var showtitle = $module.attr('data-showtitle');
        var showportrait = $module.attr('data-showportrait');

        setTimeout(function() {
            var videoWrapper = $module.children('.vimeo_video');
            videoWrapper.empty().append('<div id="vimeo-wrapper-1564626288027"></div>');

            var options = {
                url: videoUrl,
                loop: videoloop,
                autoplay: autoPlay,
                autopause: autoPause,
                byline: byline,
                title: showtitle,
                muted: videoMute,
                portrait: showportrait
            };
            var player = new Vimeo.Player("vimeo-wrapper-1564626288027", options);

        }, 100);
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447873618').children('.module');
        $module.gfV3Product();
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447873618-0').children('.module');
        var effect = $module.attr('data-effect');
        $module.gfV3ProductImage({
            'effect': effect
        })
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447873618-1').children('.module');
    });
  
    jQuery(function() {
        var $module = jQuery('#m-1564447873618-2').children('.module');
        $module.gfV3ProductPrice();
    });
  
        jQuery(function() {
            try {
                var $module = jQuery('#m-1564015862887').children('.module');   
                var navspeed = $module.data('navspeed'),
                    autoplaytimeout = $module.data('autoplaytimeout'),
                    autoplayhoverpause = $module.data('autoplayhoverpause'),
                    navlg = $module.data('navlg'),
                    navmd = $module.data('navmd'),
                    navsm = $module.data('navsm'),
                    navxs = $module.data('navxs'),
                    collg = $module.data('collg'),
                    colmd = $module.data('colmd'),
                    colsm = $module.data('colsm'),
                    colxs = $module.data('colxs'),
                    dotslg = $module.data('dotslg'),
                    dotsmd = $module.data('dotsmd'),
                    dotssm = $module.data('dotssm'),
                    dotsxs = $module.data('dotsxs'),
                    marginlg = parseInt($module.data('marginlg')),
                    marginmd = parseInt($module.data('marginmd')),
                    marginsm = parseInt($module.data('marginsm')),
                    marginxs = parseInt($module.data('marginxs'));
    
                var mode = jQuery('.gryffeditor').hasClass('editing') ? 'dev' : 'production';
                if(mode == 'production') {
                    var autoplay = $module.data('autoplay'), 
                        loop = $module.data('loop');
                } else {
                    var autoplay = 0, 
                        loop = 0;
                }
            
                $module.owlCarousel({
                    mouseDrag: false,
                    autoplayHoverPause: autoplayhoverpause,
                    autoplay: autoplay,
                    autoplayTimeout: autoplaytimeout,
                    loop: loop,
                    navSpeed: navspeed,
                    autoWidth: !1,
                    responsiveClass:true,
                    responsive:{
                        0:{
                            items:colxs,
                            nav: navxs,
                            dots:dotsxs,
                            margin: marginxs
                        },
                        768:{
                            items:colsm,
                            nav: navsm,
                            dots:dotssm,
                            margin: marginsm
                        },
                        992:{
                            items:colmd,
                            nav: navmd,
                            dots:dotsmd,
                            margin: marginmd
                        },
                        1200:{
                            items:collg,
                            nav: navlg,
                            dots:dotslg,
                            margin: marginlg
                        }
                    }
                }); 
            } catch(err) {}

        }); 
    
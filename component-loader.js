/**
 * Component Loader for ARCDIG-DOCS Templates
 * 
 * Dynamically loads header and footer components using fetch(),
 * then initializes header menu functionality.
 * 
 * This script replaces inline header/footer loading code in HTML pages.
 * Simply include this script and add <div id="header-container"></div>
 * and <div id="footer-container"></div> to your HTML.
 * 
 * @author Arcadia Digital
 * @version 1.0.0
 */

(function() {
    'use strict';

    // ============================================
    // CLIENT-SIDE AUTHENTICATION
    // ============================================
    
    const PASSWORD = 'arcadia'; // REPLACE WITH ACTUAL PASSWORD
    const AUTH_KEY = 'docs_authenticated'; // Change this if you want a unique key per project
    
    /**
     * Check if user is authenticated
     */
    function isAuthenticated() {
        return sessionStorage.getItem(AUTH_KEY) === 'true';
    }
    
    /**
     * Set authentication state
     */
    function setAuthenticated() {
        sessionStorage.setItem(AUTH_KEY, 'true');
    }
    
    /**
     * Hide content to prevent flash before authentication
     * Hides main content containers, not the entire body (so overlay is visible)
     */
    function hideContent() {
        const containers = [
            document.getElementById('header-container'),
            document.getElementById('footer-container'),
            document.querySelector('.container')
        ].filter(Boolean);
        
        containers.forEach(container => {
            container.style.visibility = 'hidden';
        });
        
        // Also hide body content but keep it in layout so overlay can be positioned
        if (document.body) {
            document.body.style.overflow = 'hidden';
        }
    }
    
    /**
     * Show content after authentication
     */
    function showContent() {
        const containers = [
            document.getElementById('header-container'),
            document.getElementById('footer-container'),
            document.querySelector('.container')
        ].filter(Boolean);
        
        containers.forEach(container => {
            container.style.visibility = 'visible';
        });
        
        if (document.body) {
            document.body.style.overflow = '';
        }
    }
    
    /**
     * Show password prompt overlay
     */
    function showPasswordPrompt() {
        // Create overlay
        const overlay = document.createElement('div');
        overlay.id = 'auth-overlay';
        overlay.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100%;
            background: #1a1a1a;
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 10000;
        `;
        
        // Create container
        const container = document.createElement('div');
        container.style.cssText = `
            background: #2a2a2a;
            padding: 2rem;
            border-radius: 8px;
            text-align: center;
            min-width: 300px;
            max-width: 400px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.3);
        `;
        
        // Create form
        const form = document.createElement('form');
        form.setAttribute('role', 'form');
        form.setAttribute('aria-label', 'Authentication form');
        
        // Hidden username field (required for browser password managers)
        const usernameInput = document.createElement('input');
        usernameInput.type = 'text';
        usernameInput.name = 'username';
        usernameInput.autocomplete = 'username';
        usernameInput.setAttribute('aria-hidden', 'true');
        usernameInput.style.cssText = 'position: absolute; left: -9999px;';
        form.appendChild(usernameInput);
        
        // Title
        const title = document.createElement('h2');
        title.textContent = 'Protected Documentation';
        title.style.cssText = `
            color: #fff;
            margin: 0 0 1rem 0;
            font-size: 1.5rem;
            font-weight: 700;
        `;
        form.appendChild(title);
        
        // Description
        const description = document.createElement('p');
        description.textContent = 'Please enter the password to access this documentation.';
        description.style.cssText = `
            color: #ccc;
            margin: 0 0 1.5rem 0;
            font-size: 0.9rem;
        `;
        form.appendChild(description);
        
        // Password input
        const passwordInput = document.createElement('input');
        passwordInput.type = 'password';
        passwordInput.name = 'password';
        passwordInput.id = 'auth-password';
        passwordInput.autocomplete = 'current-password';
        passwordInput.placeholder = 'Password';
        passwordInput.setAttribute('aria-label', 'Password');
        passwordInput.setAttribute('aria-required', 'true');
        passwordInput.required = true;
        passwordInput.style.cssText = `
            width: 100%;
            padding: 0.75rem;
            margin-bottom: 1rem;
            border: 1px solid #444;
            border-radius: 4px;
            background: #1a1a1a;
            color: #fff;
            font-size: 1rem;
            box-sizing: border-box;
        `;
        form.appendChild(passwordInput);
        
        // Error message
        const errorMsg = document.createElement('div');
        errorMsg.id = 'auth-error';
        errorMsg.setAttribute('role', 'alert');
        errorMsg.setAttribute('aria-live', 'polite');
        errorMsg.style.cssText = `
            color: #ff6b6b;
            margin-bottom: 1rem;
            font-size: 0.9rem;
            min-height: 1.5rem;
            display: none;
        `;
        form.appendChild(errorMsg);
        
        // Submit button
        const submitButton = document.createElement('button');
        submitButton.type = 'submit';
        submitButton.textContent = 'Access Documentation';
        submitButton.style.cssText = `
            width: 100%;
            padding: 0.75rem;
            background: #2d5016;
            color: #fff;
            border: none;
            border-radius: 4px;
            font-size: 1rem;
            font-weight: 700;
            cursor: pointer;
            transition: background-color 0.2s;
        `;
        
        // Button hover effect
        submitButton.addEventListener('mouseenter', function() {
            this.style.backgroundColor = '#3a6a1e';
        });
        submitButton.addEventListener('mouseleave', function() {
            this.style.backgroundColor = '#2d5016';
        });
        
        form.appendChild(submitButton);
        
        // Form submission handler
        form.addEventListener('submit', function(e) {
            e.preventDefault();
            checkPassword();
        });
        
        // Enter key handler
        passwordInput.addEventListener('keypress', function(e) {
            if (e.key === 'Enter') {
                e.preventDefault();
                checkPassword();
            }
        });
        
        /**
         * Check password and authenticate
         */
        function checkPassword() {
            const password = passwordInput.value.trim();
            const error = document.getElementById('auth-error');
            
            if (password === PASSWORD) {
                // Success - authenticate and show content
                setAuthenticated();
                overlay.remove();
                // Show content and load components
                showContent();
                loadComponents();
            } else {
                // Error - show message and refocus
                error.textContent = 'Incorrect password. Please try again.';
                error.style.display = 'block';
                passwordInput.value = '';
                passwordInput.focus();
            }
        }
        
        container.appendChild(form);
        overlay.appendChild(container);
        document.body.appendChild(overlay);
        
        // Auto-focus password input
        setTimeout(function() {
            passwordInput.focus();
        }, 100);
    }
    
    // ============================================
    // END AUTHENTICATION CODE
    // ============================================

    /**
     * Header menu initialization
     * Handles mobile menu toggle functionality
     */
    function initializeHeaderMenu() {
        const menuToggle = document.getElementById('menu-toggle');
        const headerMenu = document.getElementById('header-menu');
        
        if (!menuToggle || !headerMenu) {
            return; // Header components not found
        }
        
        // Toggle menu on button click
        menuToggle.addEventListener('click', function(e) {
            e.preventDefault();
            e.stopPropagation();
            
            const isOpen = headerMenu.classList.contains('show');
            
            if (isOpen) {
                closeMenu();
            } else {
                openMenu();
            }
        });
        
        // Close menu when clicking outside
        document.addEventListener('click', function(e) {
            if (!headerMenu.contains(e.target) && !menuToggle.contains(e.target)) {
                closeMenu();
            }
        });
        
        // Close menu on escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                closeMenu();
            }
        });
        
        function openMenu() {
            headerMenu.classList.add('show');
            menuToggle.classList.add('active');
            menuToggle.setAttribute('aria-expanded', 'true');
        }
        
        function closeMenu() {
            headerMenu.classList.remove('show');
            menuToggle.classList.remove('active');
            menuToggle.setAttribute('aria-expanded', 'false');
        }
    }

    /**
     * Load header component
     */
    function loadHeader() {
        const headerContainer = document.getElementById('header-container');
        
        if (!headerContainer) {
            console.warn('Component Loader: header-container not found');
            return;
        }
        
        fetch('header.html')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text();
            })
            .then(data => {
                headerContainer.innerHTML = data;
                // Initialize menu after header loads
                initializeHeaderMenu();
            })
            .catch(error => {
                console.error('Component Loader: Error loading header:', error);
                // Fallback: minimal header if component fails to load
                headerContainer.innerHTML = `
                    <header class="arcadia-header">
                        <div class="header-content">
                            <div class="header-brand">
                                <h1 class="header-main-title">Documentation</h1>
                            </div>
                        </div>
                    </header>
                `;
            });
    }

    /**
     * Load footer component
     */
    function loadFooter() {
        const footerContainer = document.getElementById('footer-container');
        
        if (!footerContainer) {
            console.warn('Component Loader: footer-container not found');
            return;
        }
        
        fetch('footer.html')
            .then(response => {
                if (!response.ok) {
                    throw new Error(`HTTP error! status: ${response.status}`);
                }
                return response.text();
            })
            .then(data => {
                footerContainer.innerHTML = data;
            })
            .catch(error => {
                console.error('Component Loader: Error loading footer:', error);
                // Fallback: minimal footer if component fails to load
                footerContainer.innerHTML = `
                    <footer class="arcadia-footer">
                        <div class="footer-content">
                            <div class="footer-legal">
                                <p class="footer-disclaimer">
                                    This documentation is proprietary and confidential. Unauthorized distribution is prohibited.
                                </p>
                                <p><a href="https://arcadiadigital.com" target="_blank">Arcadia Digital</a></p>
                            </div>
                        </div>
                    </footer>
                `;
            });
    }

    /**
     * Load all components
     */
    function loadComponents() {
        loadHeader();
        loadFooter();
    }

    /**
     * Initialize: Check authentication first, then load components
     */
    function init() {
        if (document.body) {
            if (!isAuthenticated()) {
                // Not authenticated - show password prompt first, then hide content
                // Show overlay first so it's visible, then hide main content
                showPasswordPrompt();
                // Small delay to ensure overlay is rendered before hiding content
                setTimeout(function() {
                    hideContent();
                }, 10);
            } else {
                // Already authenticated - hide content briefly, then show and load
                hideContent();
                showContent();
                if (document.readyState === 'loading') {
                    document.addEventListener('DOMContentLoaded', loadComponents);
                } else {
                    loadComponents();
                }
            }
        }
    }

    // Auto-initialize
    init();

})();


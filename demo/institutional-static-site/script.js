document.addEventListener('DOMContentLoaded', function() {
    'use strict';

    var mainNav = document.querySelector('nav[role="navigation"]');
    var currentPage = window.location.pathname.split('/').pop() || 'index.html';

    if (mainNav) {
        var links = mainNav.querySelectorAll('a');
        links.forEach(function(link) {
            var href = link.getAttribute('href');
            if (href === currentPage) {
                link.setAttribute('aria-current', 'page');
            }
        });
    }

    var allLinks = document.querySelectorAll('a');
    allLinks.forEach(function(link) {
        link.addEventListener('focus', function() {
            this.scrollIntoView({
                behavior: 'smooth',
                block: 'nearest'
            });
        });
    });

    document.addEventListener('keydown', function(e) {
        if (e.key === 'Tab') {
            document.body.classList.add('keyboard-navigation');
        }
    });

    document.addEventListener('mousedown', function() {
        document.body.classList.remove('keyboard-navigation');
    });
});
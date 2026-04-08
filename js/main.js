/* ============================================
   EA Bogotá — Main JavaScript
   ============================================ */

(function () {
  'use strict';

  // --- Language Switcher ---
  var LANG_KEY = 'ea-bogota-lang';
  var defaultLang = localStorage.getItem(LANG_KEY) || 'es';

  function setLanguage(lang) {
    document.documentElement.lang = lang;
    localStorage.setItem(LANG_KEY, lang);
    document.querySelectorAll('.lang-toggle button').forEach(function (btn) {
      btn.classList.toggle('active', btn.dataset.lang === lang);
    });
  }

  setLanguage(defaultLang);

  document.addEventListener('click', function (e) {
    if (e.target.matches('.lang-toggle button')) {
      setLanguage(e.target.dataset.lang);
    }
  });

  // --- Mobile Navigation ---
  document.addEventListener('click', function (e) {
    var hamburger = e.target.closest('.hamburger');
    if (hamburger) {
      hamburger.classList.toggle('open');
      var mobileNav = document.querySelector('.mobile-nav');
      if (mobileNav) mobileNav.classList.toggle('open');
      document.body.style.overflow = mobileNav && mobileNav.classList.contains('open') ? 'hidden' : '';
    }
  });

  document.addEventListener('click', function (e) {
    if (e.target.matches('.mobile-nav a')) {
      var hamburger = document.querySelector('.hamburger');
      var mobileNav = document.querySelector('.mobile-nav');
      if (hamburger) hamburger.classList.remove('open');
      if (mobileNav) mobileNav.classList.remove('open');
      document.body.style.overflow = '';
    }
  });

  // --- Scroll Fade-In (IntersectionObserver) ---
  if ('IntersectionObserver' in window) {
    var fadeObserver = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          fadeObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.05, rootMargin: '0px 0px -40px 0px' });

    document.querySelectorAll('.fade-in').forEach(function (el) {
      var rect = el.getBoundingClientRect();
      if (rect.top < window.innerHeight) {
        // Already in viewport — show immediately
        el.classList.add('visible');
      } else {
        // Below viewport — animate on scroll
        el.classList.add('animate');
        fadeObserver.observe(el);
      }
    });
  } else {
    // Fallback: no IntersectionObserver — show everything
    document.querySelectorAll('.fade-in').forEach(function (el) {
      el.classList.add('visible');
    });
  }

  // Safety net: reveal all after 2s in case observer never fires
  setTimeout(function () {
    document.querySelectorAll('.fade-in.animate:not(.visible)').forEach(function (el) {
      el.classList.add('visible');
    });
  }, 2000);

  // --- Active Nav Link ---
  var path = window.location.pathname;
  var filename = path.substring(path.lastIndexOf('/') + 1) || 'index.html';

  document.querySelectorAll('.nav-links a, .mobile-nav a').forEach(function (link) {
    var href = link.getAttribute('href');
    if (href === filename || (filename === '' && href === 'index.html')) {
      link.classList.add('active');
    }
  });

  // --- FAQ Accordion ---
  document.addEventListener('click', function (e) {
    var question = e.target.closest('.faq-question');
    if (question) {
      var item = question.closest('.faq-item');
      if (item) {
        item.classList.toggle('open');
      }
    }
  });

  // --- Smooth anchor scroll offset for fixed nav ---
  document.addEventListener('click', function (e) {
    var anchor = e.target.closest('a[href^="#"]');
    if (anchor) {
      var id = anchor.getAttribute('href').slice(1);
      var target = document.getElementById(id);
      if (target) {
        e.preventDefault();
        var offset = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-height')) || 64;
        var top = target.getBoundingClientRect().top + window.scrollY - offset - 20;
        window.scrollTo({ top: top, behavior: 'smooth' });
      }
    }
  });
})();

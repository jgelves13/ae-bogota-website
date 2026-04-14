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

  // Mark dropdown toggle as active if the current page is one of its child links
  document.querySelectorAll('.nav-dropdown').forEach(function (dd) {
    var toggle = dd.querySelector('.nav-dropdown-toggle');
    if (!toggle) return;
    var childLinks = dd.querySelectorAll('.nav-dropdown-menu a');
    for (var i = 0; i < childLinks.length; i++) {
      var href = childLinks[i].getAttribute('href');
      if (!href || href.indexOf('http') === 0) continue; // skip external + anchors
      // strip hash fragment for match (so foo.html#bar also counts as foo.html)
      var hrefBase = href.split('#')[0];
      if (hrefBase === filename) {
        toggle.classList.add('active');
        break;
      }
    }
  });

  // --- Nav Dropdown toggle (click to open on desktop, tap to expand on mobile) ---
  document.addEventListener('click', function (e) {
    var toggle = e.target.closest('.nav-dropdown-toggle');
    if (toggle) {
      e.preventDefault();
      e.stopPropagation();
      var dd = toggle.closest('.nav-dropdown');
      var isOpen = dd.getAttribute('data-open') === 'true';
      // Close any other open dropdowns
      document.querySelectorAll('.nav-dropdown[data-open="true"]').forEach(function (other) {
        if (other !== dd) {
          other.setAttribute('data-open', 'false');
          var otherToggle = other.querySelector('.nav-dropdown-toggle');
          if (otherToggle) otherToggle.setAttribute('aria-expanded', 'false');
        }
      });
      dd.setAttribute('data-open', isOpen ? 'false' : 'true');
      toggle.setAttribute('aria-expanded', isOpen ? 'false' : 'true');
      return;
    }
    // Click outside any dropdown closes all
    if (!e.target.closest('.nav-dropdown')) {
      document.querySelectorAll('.nav-dropdown[data-open="true"]').forEach(function (dd) {
        dd.setAttribute('data-open', 'false');
        var t = dd.querySelector('.nav-dropdown-toggle');
        if (t) t.setAttribute('aria-expanded', 'false');
      });
    }
  });

  // Escape key closes open dropdowns
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape') {
      document.querySelectorAll('.nav-dropdown[data-open="true"]').forEach(function (dd) {
        dd.setAttribute('data-open', 'false');
        var t = dd.querySelector('.nav-dropdown-toggle');
        if (t) {
          t.setAttribute('aria-expanded', 'false');
          t.focus();
        }
      });
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

  // --- Essay Sidebar TOC: Scroll Spy ---
  var tocLinks = document.querySelectorAll('.toc-link');
  if (tocLinks.length > 0) {
    var sectionIds = [];
    tocLinks.forEach(function (link) {
      var id = link.getAttribute('href').slice(1);
      if (id) sectionIds.push(id);
    });

    var navH = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-height')) || 76;

    function updateActiveToc() {
      var lang = document.documentElement.lang || 'es';
      var prefix = lang === 'en' ? 'en-' : 'es-';
      var scrollY = window.scrollY + navH + 60;
      var activeId = null;

      sectionIds.forEach(function (id) {
        if (!id.startsWith(prefix)) return;
        var el = document.getElementById(id);
        if (el && el.getBoundingClientRect().top + window.scrollY <= scrollY) {
          activeId = id;
        }
      });

      tocLinks.forEach(function (link) {
        var href = link.getAttribute('href').slice(1);
        link.classList.toggle('active', href === activeId);
      });
    }

    var tocRaf;
    window.addEventListener('scroll', function () {
      if (tocRaf) cancelAnimationFrame(tocRaf);
      tocRaf = requestAnimationFrame(updateActiveToc);
    }, { passive: true });
    updateActiveToc();
  }

  // --- Audio Player Widget ---
  var audioPlayer = document.getElementById('audio-player');
  var btnPlay = document.getElementById('audio-play');
  var btnBack = document.getElementById('audio-back');
  var btnFwd = document.getElementById('audio-fwd');
  var btnSpeed = document.getElementById('audio-speed');
  var progressBar = document.getElementById('audio-progress');
  var timeCurrent = document.getElementById('audio-current');
  var timeDuration = document.getElementById('audio-duration');
  var btnListen = document.getElementById('btn-listen');

  if (btnPlay && audioPlayer) {
    var audio = null;
    var speeds = [0.75, 1, 1.25, 1.5, 1.75, 2];
    var speedIdx = 1;

    function fmtTime(s) {
      if (!s || isNaN(s)) return '00:00';
      var m = Math.floor(s / 60);
      var sec = Math.floor(s % 60);
      return (m < 10 ? '0' : '') + m + ':' + (sec < 10 ? '0' : '') + sec;
    }

    function initAudio() {
      var lang = document.documentElement.lang || 'es';
      var src = 'audio/essay-' + lang + '.mp3';
      if (audio && audio.dataset.lang === lang) return audio;
      if (audio) { audio.pause(); }
      audio = new Audio(src);
      audio.dataset.lang = lang;
      audio.preload = 'metadata';

      audio.addEventListener('loadedmetadata', function () {
        timeDuration.textContent = fmtTime(audio.duration);
        progressBar.max = audio.duration || 100;
      });
      audio.addEventListener('timeupdate', function () {
        timeCurrent.textContent = fmtTime(audio.currentTime);
        progressBar.value = audio.currentTime;
      });
      audio.addEventListener('ended', function () {
        btnPlay.querySelector('.icon-play').style.display = '';
        btnPlay.querySelector('.icon-pause').style.display = 'none';
        if (btnListen) btnListen.classList.remove('active');
      });
      return audio;
    }

    function showPlayer() {
      audioPlayer.classList.add('visible');
    }

    function setPlayIcon(playing) {
      btnPlay.querySelector('.icon-play').style.display = playing ? 'none' : '';
      btnPlay.querySelector('.icon-pause').style.display = playing ? '' : 'none';
      if (btnListen) btnListen.classList.toggle('active', playing);
    }

    function togglePlay() {
      var a = initAudio();
      showPlayer();
      if (a.paused) {
        a.play();
        setPlayIcon(true);
      } else {
        a.pause();
        setPlayIcon(false);
      }
    }

    btnPlay.addEventListener('click', togglePlay);

    // Sidebar "Escuchar" button opens player and starts playback
    if (btnListen) {
      btnListen.addEventListener('click', function () {
        var a = initAudio();
        showPlayer();
        if (a.paused) {
          a.play();
          setPlayIcon(true);
        } else {
          a.pause();
          setPlayIcon(false);
        }
      });
    }

    btnBack.addEventListener('click', function () {
      if (audio) audio.currentTime = Math.max(0, audio.currentTime - 10);
    });
    btnFwd.addEventListener('click', function () {
      if (audio) audio.currentTime = Math.min(audio.duration || 0, audio.currentTime + 10);
    });

    progressBar.addEventListener('input', function () {
      if (audio) audio.currentTime = parseFloat(progressBar.value);
    });

    btnSpeed.addEventListener('click', function () {
      speedIdx = (speedIdx + 1) % speeds.length;
      var s = speeds[speedIdx];
      if (audio) audio.playbackRate = s;
      btnSpeed.textContent = 'Speed ' + (s === 1 ? '1' : s) + 'x';
    });

    // Re-init audio when language changes
    document.querySelectorAll('.lang-toggle button').forEach(function (b) {
      b.addEventListener('click', function () {
        var wasPlaying = audio && !audio.paused;
        if (audio) { audio.pause(); audio = null; }
        btnPlay.querySelector('.icon-play').style.display = '';
        btnPlay.querySelector('.icon-pause').style.display = 'none';
        timeCurrent.textContent = '00:00';
        timeDuration.textContent = '00:00';
        progressBar.value = 0;
        if (btnListen) btnListen.classList.remove('active');
        audioPlayer.classList.remove('visible');
      });
    });
  }

  // --- Share Button (always copies URL to clipboard) ---
  var btnShare = document.getElementById('btn-share');
  if (btnShare) {
    btnShare.addEventListener('click', function () {
      var url = window.location.href;
      function showToast() {
        var toast = document.getElementById('share-toast');
        if (toast) {
          toast.classList.add('visible');
          setTimeout(function () { toast.classList.remove('visible'); }, 2000);
        }
      }
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(showToast).catch(function () {
          // Fallback for browsers without clipboard API permission
          var ta = document.createElement('textarea');
          ta.value = url;
          ta.style.position = 'fixed';
          ta.style.opacity = '0';
          document.body.appendChild(ta);
          ta.select();
          try { document.execCommand('copy'); showToast(); } catch (e) {}
          document.body.removeChild(ta);
        });
      } else {
        var ta = document.createElement('textarea');
        ta.value = url;
        ta.style.position = 'fixed';
        ta.style.opacity = '0';
        document.body.appendChild(ta);
        ta.select();
        try { document.execCommand('copy'); showToast(); } catch (e) {}
        document.body.removeChild(ta);
      }
    });
  }

  // --- Footnote Popups ---
  document.addEventListener('click', function (e) {
    var ref = e.target.closest('.fn-ref');
    if (ref) {
      e.preventDefault();
      e.stopPropagation();
      var fn = ref.closest('.fn');
      var wasOpen = fn.classList.contains('open');
      // Close all open footnotes
      document.querySelectorAll('.fn.open').forEach(function (f) { f.classList.remove('open'); });
      if (!wasOpen) fn.classList.add('open');
      return;
    }
    // Click outside closes all
    if (!e.target.closest('.fn-popup')) {
      document.querySelectorAll('.fn.open').forEach(function (f) { f.classList.remove('open'); });
    }
  });

  // --- Smooth anchor scroll offset for fixed nav ---
  function scrollToHash(hash) {
    if (!hash) return;
    var id = hash.slice(1);
    var target = document.getElementById(id);
    if (target) {
      var offset = parseInt(getComputedStyle(document.documentElement).getPropertyValue('--nav-height')) || 64;
      var top = target.getBoundingClientRect().top + window.scrollY - offset - 20;
      window.scrollTo({ top: top, behavior: 'smooth' });
    }
  }

  document.addEventListener('click', function (e) {
    var anchor = e.target.closest('a[href^="#"]');
    if (anchor) {
      e.preventDefault();
      scrollToHash(anchor.getAttribute('href'));
    }
  });

  // Handle hash on page load
  if (window.location.hash) {
    requestAnimationFrame(function () {
      scrollToHash(window.location.hash);
    });
  }
})();

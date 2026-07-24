/* ==========================================================================
   G3FSP — Accueil : moteur d'animation scroll-driven
   Modèle repris de la V2 (validé en production) :
     · le canvas est visible et réagit dès le PREMIER pixel de scroll
     · aucun épinglage du hero, aucun loader bloquant
     · révélations de section en CSS + IntersectionObserver (fluide sur mobile)
   ========================================================================== */

(function () {
  "use strict";

  /* ----------------------------------------------------------------------
     Configuration
     ---------------------------------------------------------------------- */
  var FRAME_COUNT = 192;
  var FRAME_SPEED = 1.30;   // recalculé dynamiquement plus bas
  // « cover » strict : toute valeur < 1 laisserait des bandes noires en haut
  // et en bas, visibles sur les frames dont le bas est rocheux (fin de séquence).
  // Sur un cadre de 2/3 de large, le cover conserve la machine entière.
  var IMAGE_SCALE = 1.0;
  var HERO_FADE_PX = 900;   // distance sur laquelle le hero s'efface

  var pad = function (n) { return String(n).padStart(4, "0"); };

  var reduceMotion = window.matchMedia("(prefers-reduced-motion: reduce)").matches;

  /* ----------------------------------------------------------------------
     Références DOM
     ---------------------------------------------------------------------- */
  var canvas       = document.getElementById("canvas");
  var canvasWrap   = document.querySelector(".canvas-wrap");
  var heroSection  = document.querySelector(".hero-standalone");
  var heroInner    = document.querySelector(".hero-inner");
  var progressBar  = document.getElementById("global-progress-bar");
  var loadingBadge = document.getElementById("frame-loading");
  var loadingCount = document.getElementById("frame-loading-count");
  var ctx          = canvas.getContext("2d", { alpha: false });

  var frames  = new Array(FRAME_COUNT);
  var loaded  = 0;
  var current = -1;

  /* ----------------------------------------------------------------------
     Rendu canvas
     ---------------------------------------------------------------------- */

  function resizeCanvas() {
    var rect = canvasWrap.getBoundingClientRect();
    var dpr = Math.min(window.devicePixelRatio || 1, 2);
    canvas.width  = Math.max(1, Math.round(rect.width * dpr));
    canvas.height = Math.max(1, Math.round(rect.height * dpr));
    if (current >= 0) drawFrame(current);
  }

  // Renvoie la frame demandée, ou la plus proche déjà chargée.
  function nearestLoaded(index) {
    if (frames[index]) return frames[index];
    for (var d = 1; d < FRAME_COUNT; d++) {
      if (frames[index - d]) return frames[index - d];
      if (frames[index + d]) return frames[index + d];
    }
    return null;
  }

  function drawFrame(index) {
    var img = nearestLoaded(index);
    if (!img) return;

    var cw = canvas.width, ch = canvas.height;
    var iw = img.naturalWidth, ih = img.naturalHeight;
    var scale = Math.max(cw / iw, ch / ih) * IMAGE_SCALE;
    var dw = iw * scale, dh = ih * scale;

    ctx.fillStyle = "#000";
    ctx.fillRect(0, 0, cw, ch);
    ctx.drawImage(img, (cw - dw) / 2, (ch - dh) / 2, dw, dh);
  }

  /* ----------------------------------------------------------------------
     Chargement des frames — non bloquant
     La première frame est dessinée dès son arrivée ; les suivantes
     s'ajoutent en arrière-plan pendant que l'utilisateur lit le hero.
     ---------------------------------------------------------------------- */

  function updateBadge() {
    if (!loadingBadge) return;
    if (loaded >= FRAME_COUNT) {
      loadingBadge.setAttribute("data-visible", "false");
      return;
    }
    loadingBadge.setAttribute("data-visible", "true");
    if (loadingCount) {
      loadingCount.textContent = Math.round((loaded / FRAME_COUNT) * 100) + " %";
    }
  }

  function loadFrame(i, onDone) {
    var img = new Image();
    img.decoding = "async";
    img.onload = function () {
      frames[i] = img;
      loaded++;
      updateBadge();
      // Dessine immédiatement si c'est la frame attendue à l'écran
      if (i === current || (current < 0 && i === 0)) {
        if (current < 0) current = 0;
        drawFrame(current);
      }
      if (onDone) onDone();
    };
    img.onerror = function () { loaded++; updateBadge(); if (onDone) onDone(); };
    img.src = "frames/frame_" + pad(i + 1) + ".webp";
  }

  // Frame 1 en priorité absolue, puis le reste par lots parallèles.
  loadFrame(0, function () {
    var next = 1;
    var CONCURRENCY = 6;
    function pump() {
      if (next >= FRAME_COUNT) return;
      var i = next++;
      loadFrame(i, pump);
    }
    for (var c = 0; c < CONCURRENCY; c++) pump();
  });

  resizeCanvas();
  updateBadge();

  var resizeTimer;
  window.addEventListener("resize", function () {
    window.clearTimeout(resizeTimer);
    resizeTimer = window.setTimeout(resizeCanvas, 150);
  });

  /* ----------------------------------------------------------------------
     Positionnement des sections (en vh, comme en V2)
     ---------------------------------------------------------------------- */

  var sections = Array.prototype.slice.call(
    document.querySelectorAll("#scroll-container .scroll-section")
  );

  // Positions en % du conteneur : s'adaptent automatiquement aux
  // hauteurs différentes définies par breakpoint (620 / 480 / 430 vh).
  sections.forEach(function (s) {
    var enter = parseFloat(s.dataset.enter);
    var leave = parseFloat(s.dataset.leave);
    s.style.top = (enter + (leave - enter) / 2) + "%";
  });

  /* ----------------------------------------------------------------------
     Révélations de section — CSS + IntersectionObserver
     ---------------------------------------------------------------------- */

  function setupReveal(section) {
    var type = section.dataset.animation || "fade-up";
    var persist = section.dataset.persist === "true";
    var children = section.querySelectorAll(
      ".section-label, .section-heading, .section-body, .section-note," +
      " .section-link, .cta-actions, .stat"
    );

    section.classList.add("anim-parent");
    Array.prototype.forEach.call(children, function (child, i) {
      child.classList.add("anim-child", "a-" + type);
      child.style.transitionDelay = (i * 0.11) + "s";
    });

    if (!("IntersectionObserver" in window)) {
      section.classList.add("is-visible");
      return;
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (entry.isIntersecting) {
          section.classList.add("is-visible");
          if (persist) io.unobserve(section);
        } else if (!persist) {
          section.classList.remove("is-visible");
        }
      });
    }, { threshold: 0.15, rootMargin: "0px 0px -10% 0px" });

    io.observe(section);
  }

  sections.forEach(setupReveal);

  /* ----------------------------------------------------------------------
     Compteurs
     ---------------------------------------------------------------------- */

  document.querySelectorAll(".stat-number").forEach(function (el) {
    var target = parseFloat(el.dataset.value);
    var section = el.closest(".scroll-section");
    if (!section) return;

    var fired = false;
    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting || fired) return;
        fired = true;
        if (reduceMotion) { el.textContent = target; return; }
        var start = null, dur = 1400;
        function step(ts) {
          if (start === null) start = ts;
          var p = Math.min((ts - start) / dur, 1);
          el.textContent = Math.round(target * (1 - Math.pow(1 - p, 3)));
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.4 });

    io.observe(section);
  });

  /* ----------------------------------------------------------------------
     Repli sans GSAP : on affiche tout proprement
     ---------------------------------------------------------------------- */

  if (typeof gsap === "undefined" || typeof ScrollTrigger === "undefined") {
    sections.forEach(function (s) { s.classList.add("is-visible"); });
    window.addEventListener("scroll", function () {
      var max = document.documentElement.scrollHeight - window.innerHeight;
      var p = max > 0 ? window.scrollY / max : 0;
      var idx = Math.min(Math.floor(Math.min(p * FRAME_SPEED, 1) * FRAME_COUNT),
                         FRAME_COUNT - 1);
      if (idx !== current) { current = idx; drawFrame(idx); }
      if (progressBar) progressBar.style.width = (p * 100) + "%";
    }, { passive: true });
    return;
  }

  gsap.registerPlugin(ScrollTrigger);

  /* ----------------------------------------------------------------------
     Lenis — scroll fluide (désactivé si mouvement réduit)
     ---------------------------------------------------------------------- */

  var lenis = null;
  if (typeof Lenis !== "undefined" && !reduceMotion) {
    lenis = new Lenis({
      duration: 1.2,
      easing: function (t) { return Math.min(1, 1.001 - Math.pow(2, -10 * t)); },
      smoothWheel: true
    });
    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add(function (time) { lenis.raf(time * 1000); });
    gsap.ticker.lagSmoothing(0);
    window.g3Lenis = lenis; // pour la coupure du scroll par le menu mobile
  }

  document.querySelectorAll('a[href^="#"]').forEach(function (a) {
    a.addEventListener("click", function (e) {
      var t = document.querySelector(a.getAttribute("href"));
      if (!t) return;
      e.preventDefault();
      if (lenis) lenis.scrollTo(t, { offset: -70 });
      else t.scrollIntoView({ behavior: "smooth" });
    });
  });

  /* ----------------------------------------------------------------------
     Liaison frames ↔ scroll — sur TOUT le document.
     C'est ce qui fait que la machine bouge dès le premier pixel.
     ---------------------------------------------------------------------- */

  // La séquence doit s'achever exactement quand la zone statique commence :
  // on calcule le facteur d'accélération à partir de la hauteur réelle de la
  // page, ce qui reste juste quel que soit le breakpoint ou la longueur du
  // contenu éditorial ajouté plus bas.
  var staticRegionEl = document.querySelector(".static-region");

  function computeFrameSpeed() {
    var maxScroll = document.documentElement.scrollHeight - window.innerHeight;
    if (maxScroll <= 0) return 1;
    var animEnd = staticRegionEl
      ? staticRegionEl.offsetTop - window.innerHeight * 0.5
      : maxScroll;
    animEnd = Math.max(window.innerHeight, Math.min(animEnd, maxScroll));
    return maxScroll / animEnd;
  }

  FRAME_SPEED = computeFrameSpeed();
  ScrollTrigger.addEventListener("refresh", function () {
    FRAME_SPEED = computeFrameSpeed();
  });

  ScrollTrigger.create({
    trigger: document.documentElement,
    start: "top top",
    end: "bottom bottom",
    scrub: true,
    onUpdate: function (self) {
      var accelerated = Math.min(self.progress * FRAME_SPEED, 1);
      var index = Math.min(Math.floor(accelerated * FRAME_COUNT), FRAME_COUNT - 1);
      if (index !== current) {
        current = index;
        requestAnimationFrame(function () { drawFrame(current); });
      }
      if (progressBar) progressBar.style.width = (self.progress * 100) + "%";
    }
  });

  /* ----------------------------------------------------------------------
     Hero — fondu + parallaxe (pas d'épinglage)
     ---------------------------------------------------------------------- */

  gsap.from(".hero-heading .word > span", {
    yPercent: 110, opacity: 0, duration: 1, stagger: 0.08,
    ease: "power4.out", delay: 0.15
  });
  gsap.from(".hero-tagline, .hero-sub, .hero-meta > *, .hero-scroll", {
    y: 22, opacity: 0, duration: 0.8, stagger: 0.08,
    ease: "power3.out", delay: 0.4
  });

  ScrollTrigger.create({
    trigger: document.documentElement,
    start: "top top",
    end: "+=" + HERO_FADE_PX,
    scrub: true,
    onUpdate: function (self) {
      var p = self.progress;
      heroSection.style.opacity = Math.max(0, 1 - p * 1.45);
      if (heroInner) heroInner.style.transform = "translateY(" + (p * 140) + "px)";
    }
  });

  /* ----------------------------------------------------------------------
     Marquee horizontal
     ---------------------------------------------------------------------- */

  // Le marquee se cale sur la progression du conteneur de scroll (et non de
  // la page entière), pour rester aligné avec les sections quelle que soit
  // la longueur du contenu éditorial en dessous.
  var scrollContainer = document.getElementById("scroll-container");

  document.querySelectorAll(".marquee-wrap").forEach(function (el) {
    var speed  = parseFloat(el.dataset.scrollSpeed) || -28;
    var mEnter = parseFloat(el.dataset.enter) / 100;
    var mLeave = parseFloat(el.dataset.leave) / 100;

    gsap.to(el.querySelector(".marquee-text"), {
      xPercent: speed,
      ease: "none",
      scrollTrigger: {
        trigger: scrollContainer,
        start: "top top", end: "bottom bottom", scrub: true
      }
    });

    ScrollTrigger.create({
      trigger: scrollContainer,
      start: "top top", end: "bottom bottom", scrub: true,
      onUpdate: function (self) {
        var p = self.progress;
        el.style.opacity = (p >= mEnter && p <= mLeave) ? 1 : 0;
      }
    });
  });

  /* ----------------------------------------------------------------------
     En-tête transparent au-dessus du hero, opaque ensuite
     ---------------------------------------------------------------------- */

  var header = document.querySelector(".site-header");
  header.classList.add("site-header--transparent");
  ScrollTrigger.create({
    start: "top -60",
    onEnter:     function () { header.classList.remove("site-header--transparent"); },
    onLeaveBack: function () { header.classList.add("site-header--transparent"); }
  });

  /* ----------------------------------------------------------------------
     Masquer canvas / voiles une fois la zone statique atteinte
     ---------------------------------------------------------------------- */

  var staticRegion = document.querySelector(".static-region");
  if (staticRegion) {
    var fixedLayers = [canvasWrap,
                       document.getElementById("dark-overlay"),
                       document.getElementById("grid-overlay")];
    ScrollTrigger.create({
      trigger: staticRegion,
      start: "top bottom",
      onEnter: function () {
        fixedLayers.forEach(function (n) { if (n) n.style.visibility = "hidden"; });
      },
      onLeaveBack: function () {
        fixedLayers.forEach(function (n) { if (n) n.style.visibility = "visible"; });
      }
    });
  }

  ScrollTrigger.refresh();
})();

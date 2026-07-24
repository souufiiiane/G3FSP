/* ==========================================================================
   G3FSP — Comportements partagés (toutes pages)
   ========================================================================== */

(function () {
  "use strict";

  /* --- Menu mobile --- */
  var burger = document.querySelector(".burger");
  var menu = document.getElementById("mobile-menu");

  // Coupe le scroll fluide Lenis pendant l'ouverture du menu (sinon le fond
  // continue de défiler sous l'overlay).
  function setMenu(open) {
    if (!burger || !menu) return;
    burger.setAttribute("aria-expanded", String(open));
    menu.setAttribute("data-open", String(open));
    document.body.style.overflow = open ? "hidden" : "";
    if (window.g3Lenis) {
      if (open) window.g3Lenis.stop();
      else window.g3Lenis.start();
    }
  }

  if (burger && menu) {
    burger.addEventListener("click", function () {
      setMenu(burger.getAttribute("aria-expanded") !== "true");
    });

    menu.addEventListener("click", function (e) {
      if (e.target.closest("a")) setMenu(false);
    });

    document.addEventListener("keydown", function (e) {
      if (e.key === "Escape" && menu.getAttribute("data-open") === "true") {
        setMenu(false);
        burger.focus();
      }
    });
  }

  /* --- Révélations au scroll --- */
  var revealables = document.querySelectorAll("[data-reveal]");

  if (revealables.length) {
    if (!("IntersectionObserver" in window)) {
      revealables.forEach(function (el) { el.classList.add("is-in"); });
    } else {
      var io = new IntersectionObserver(function (entries) {
        entries.forEach(function (entry) {
          if (entry.isIntersecting) {
            entry.target.classList.add("is-in");
            io.unobserve(entry.target);
          }
        });
      }, { rootMargin: "0px 0px -12% 0px", threshold: 0.12 });

      revealables.forEach(function (el, i) {
        // Décalage en cascade au sein d'un même parent
        var siblings = Array.prototype.filter.call(
          el.parentElement ? el.parentElement.children : [],
          function (n) { return n.hasAttribute && n.hasAttribute("data-reveal"); }
        );
        var idx = siblings.indexOf(el);
        el.style.setProperty("--d", (idx > 0 ? idx * 90 : 0) + "ms");
        io.observe(el);
      });
    }
  }

  /* --- Compteurs (pages intérieures, sans GSAP) --- */
  var counters = document.querySelectorAll("[data-count]");

  if (counters.length && "IntersectionObserver" in window) {
    var cio = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        if (!entry.isIntersecting) return;
        var el = entry.target;
        cio.unobserve(el);

        if (window.matchMedia("(prefers-reduced-motion: reduce)").matches) {
          el.textContent = el.dataset.count;
          return;
        }

        var target = parseFloat(el.dataset.count);
        var suffix = el.dataset.suffix || "";
        var start = null;
        var dur = 1500;

        function step(ts) {
          if (start === null) start = ts;
          var p = Math.min((ts - start) / dur, 1);
          var eased = 1 - Math.pow(1 - p, 3);
          el.textContent = Math.round(target * eased) + suffix;
          if (p < 1) requestAnimationFrame(step);
        }
        requestAnimationFrame(step);
      });
    }, { threshold: 0.5 });

    counters.forEach(function (el) { cio.observe(el); });
  }

  /* --- Année courante dans le pied de page --- */
  document.querySelectorAll("[data-year]").forEach(function (el) {
    el.textContent = String(new Date().getFullYear());
  });
})();

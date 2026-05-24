document.addEventListener("DOMContentLoaded", () => {
    // ----------------------------------------------------------------
    // 1. Lenis Smooth Scroll Setup
    // ----------------------------------------------------------------
    const lenis = new Lenis({
        duration: 1.2,
        easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
        smoothWheel: true
    });

    lenis.on("scroll", ScrollTrigger.update);
    gsap.ticker.add((time) => lenis.raf(time * 1000));
    gsap.ticker.lagSmoothing(0);


    // ----------------------------------------------------------------
    // 1b. Mobile Menu Logic
    // ----------------------------------------------------------------
    const mobileToggle = document.querySelector('.mobile-toggle');
    const mobileOverlay = document.querySelector('.mobile-nav-overlay');
    const mobileLinks = document.querySelectorAll('.mobile-link');

    if (mobileToggle && mobileOverlay) {
        mobileToggle.addEventListener('click', () => {
            mobileToggle.classList.toggle('active');
            mobileOverlay.classList.toggle('active');

            // Stop lenis scroll when menu is open
            if (mobileOverlay.classList.contains('active')) {
                lenis.stop();
            } else {
                lenis.start();
            }
        });

        // Close menu when a link is clicked
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                mobileToggle.classList.remove('active');
                mobileOverlay.classList.remove('active');
                lenis.start();
            });
        });
    }


    // ----------------------------------------------------------------
    // 2. Preloader & Frame Setup
    // ----------------------------------------------------------------
    const TOTAL_FRAMES = 192; // Ensure this matches ffmpeg extract
    const frames = [];
    let loadedCount = 0;
    let currentFrame = 0;

    // Pad number to 4 digits
    const pad = (num) => String(num).padStart(4, '0');

    function loadFrames() {
        // Initialize animations instantly
        initAnimations();

        for (let i = 1; i <= TOTAL_FRAMES; i++) {
            const img = new Image();
            img.src = `frames/frame_${pad(i)}.webp`;
            img.onload = () => {
                frames[i - 1] = img;
                loadedCount++;

                // If first frame loaded, draw it
                if (loadedCount === 1 && canvas) {
                    resizeCanvas();
                }
                
                // If it's the current frame we need, draw it
                if (i - 1 === currentFrame && canvas) {
                    drawFrame(currentFrame);
                }
            };
            img.onerror = () => {
                loadedCount++;
            }
        }
    }


    // ----------------------------------------------------------------
    // 3. Canvas Renderer
    // ----------------------------------------------------------------
    const canvasWrap = document.querySelector(".canvas-wrap");
    const canvas = document.getElementById("canvas");
    const ctx = canvas.getContext("2d", { alpha: false });

    // Resize canvas
    function resizeCanvas() {
        // We set to fixed right column sizing (or full width on mobile)
        const isMobile = window.innerWidth <= 1024;
        const width = isMobile ? window.innerWidth : window.innerWidth * 0.6666;
        const height = window.innerHeight;

        // Handle High DPI displays
        const dpr = window.devicePixelRatio || 1;
        canvas.width = width * dpr;
        canvas.height = height * dpr;
        ctx.scale(dpr, dpr);

        if (currentFrame >= 0) {
            drawFrame(currentFrame);
        }
    }

    const IMAGE_SCALE = 0.85;

    function drawFrame(index) {
        const img = frames[index];
        if (!img) return;

        const cw = canvas.width / (window.devicePixelRatio || 1);
        const ch = canvas.height / (window.devicePixelRatio || 1);

        const iw = img.naturalWidth;
        const ih = img.naturalHeight;

        const scale = Math.max(cw / iw, ch / ih) * IMAGE_SCALE;
        const dw = iw * scale;
        const dh = ih * scale;
        const dx = (cw - dw) / 2;
        const dy = (ch - dh) / 2;

        // Fill background with black to blend
        ctx.fillStyle = "#000000";
        ctx.fillRect(0, 0, cw, ch);

        ctx.drawImage(img, dx, dy, dw, dh);
    }

    window.addEventListener("resize", resizeCanvas);


    // ----------------------------------------------------------------
    // 4. Initializing Animations
    // ----------------------------------------------------------------
    function initAnimations() {
        resizeCanvas();

        const scrollContainer = document.getElementById("scroll-container");

        // 4a. Frame to Scroll Binding
        const FRAME_SPEED = 1.3;
        ScrollTrigger.create({
            trigger: document.documentElement,
            start: "top top",
            end: "bottom bottom",
            scrub: true,
            onUpdate: (self) => {
                const accelerated = Math.min(self.progress * FRAME_SPEED, 1);
                const index = Math.min(Math.floor(accelerated * TOTAL_FRAMES), TOTAL_FRAMES - 1);

                if (index !== currentFrame) {
                    currentFrame = index;
                    requestAnimationFrame(() => drawFrame(currentFrame));
                }
            }
        });

        // 4b. Hero Parallax and Fade Out
        const heroSection = document.querySelector(".hero-standalone");
        const heroContent = document.querySelector(".hero-content");
        ScrollTrigger.create({
            trigger: document.documentElement,
            start: "top top",
            end: "+=1500", // Tweak end distance to personal taste
            scrub: true,
            onUpdate: (self) => {
                const p = self.progress;
                // Fade out hero content
                heroSection.style.opacity = Math.max(0, 1 - p * 5);
                if (heroContent) {
                    // Parallax effect: moves down as user scrolls down
                    heroContent.style.transform = `translateY(${p * 250}px)`;
                }
            }
        });

        // 4X. Global Progress Bar
        const progressBar = document.getElementById("global-progress-bar");
        ScrollTrigger.create({
            trigger: document.documentElement,
            start: "top top",
            end: "bottom bottom",
            scrub: true,
            onUpdate: (self) => {
                if (progressBar) {
                    progressBar.style.width = `${self.progress * 100}%`;
                }
            }
        });

        // 4c. Footer Sections Native Reveal
        const normalSections = document.querySelectorAll(".normal-section");
        normalSections.forEach(setupSectionAnimation);

        // 4d. Setup Section Animations
        document.querySelectorAll(".scroll-section").forEach(setupSectionAnimation);
    }


    // ----------------------------------------------------------------
    // 5. Section Animation System
    // ----------------------------------------------------------------
    function setupSectionAnimation(section) {
        const type = section.dataset.animation || "fade-up";
        const persist = section.dataset.persist === "true";

        if (section.classList.contains('scroll-section')) {
            const enterValue = parseFloat(section.dataset.enter) || 0;
            const leaveValue = parseFloat(section.dataset.leave) || 100;
            const midpoint = enterValue + ((leaveValue - enterValue) / 2);
            section.style.top = `${midpoint}vh`;
        }

        const children = section.querySelectorAll(
            ".section-label, .section-heading, .section-body, .feature-item, .project-item, .project-card, a.btn-primary, .contact-form, .footer-info"
        );

        // Prepare CSS-first animations
        section.classList.add("css-animate-parent");
        children.forEach((child, index) => {
            child.classList.add("css-animate-child");
            child.classList.add(`anim-type-${type}`);
            child.style.transitionDelay = `${index * 0.15}s`;
        });

        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    section.classList.add('is-visible');
                } else if (!persist) {
                    section.classList.remove('is-visible');
                }
            });
        }, { threshold: 0.15, rootMargin: "0px 0px -10% 0px" });

        observer.observe(section);
    }

    // Start loading frames right away
    loadFrames();
});

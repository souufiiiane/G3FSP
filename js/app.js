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

    const loaderPercent = document.getElementById("loader-percent");
    const loaderBar = document.getElementById("loader-bar");
    const loader = document.getElementById("loader");

    // Pad number to 4 digits
    const pad = (num) => String(num).padStart(4, '0');

    // First load 10 frames fast, then load the rest
    const loadPhase1 = 10;

    function loadFrames() {
        for (let i = 1; i <= TOTAL_FRAMES; i++) {
            const img = new Image();
            img.src = `frames/frame_${pad(i)}.webp`;
            img.onload = () => {
                frames[i - 1] = img;
                loadedCount++;

                // Update loader UI
                const p = Math.floor((loadedCount / TOTAL_FRAMES) * 100);
                loaderPercent.innerText = `${p}%`;
                loaderBar.style.width = `${p}%`;

                // If first frame loaded, draw it
                if (loadedCount === 1 && canvas) {
                    resizeCanvas();
                }

                // Hydrate page when fully loaded
                if (loadedCount === TOTAL_FRAMES) {
                    setTimeout(() => {
                        loader.style.opacity = "0";
                        setTimeout(() => loader.style.display = "none", 800);
                        initAnimations();
                    }, 500);
                }
            };
            img.onerror = () => {
                // Ignore missing frames slightly 
                loadedCount++;
                if (loadedCount === TOTAL_FRAMES) {
                    loader.style.opacity = "0";
                    setTimeout(() => loader.style.display = "none", 800);
                    initAnimations();
                }
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
        normalSections.forEach((sec) => {
            const children = sec.querySelectorAll(
                ".section-label, .section-heading, .section-body, .feature-item, .project-item, .project-card, .btn-primary, .contact-form, .footer-info"
            );
            gsap.from(children, {
                scrollTrigger: {
                    trigger: sec,
                    start: "top 85%", // trigger when top of section hits 85% down viewport
                },
                y: 60,
                opacity: 0,
                stagger: 0.15,
                duration: 1.2,
                ease: "power4.out"
            });
        });

        // 4d. Setup Section Animations
        document.querySelectorAll(".scroll-section").forEach(setupSectionAnimation);
    }


    // ----------------------------------------------------------------
    // 5. Section Animation System
    // ----------------------------------------------------------------
    function setupSectionAnimation(section) {
        const type = section.dataset.animation;
        const persist = section.dataset.persist === "true";

        // Enter / Leave percentages (0-1)
        const enterValue = parseFloat(section.dataset.enter) || 0;
        const leaveValue = parseFloat(section.dataset.leave) || 100;
        const enter = enterValue / 100;
        const leave = leaveValue / 100;

        const children = section.querySelectorAll(
            ".section-label, .section-heading, .section-body, .feature-item, .project-item, .project-card, .btn-primary, .contact-form, .footer-info"
        );

        // Position it at the center of our scroll area where it will be visible
        // We translate it absolutely based on percentage
        const midpoint = enter + ((leave - enter) / 2);
        section.style.top = `${midpoint * 100}%`;

        const tl = gsap.timeline({ paused: true });

        // Add standard stagger animations Based on `type`
        switch (type) {
            case "fade-up":
                tl.from(children, { y: 60, opacity: 0, stagger: 0.15, duration: 1.2, ease: "power4.out" });
                break;
            case "slide-left":
                tl.from(children, { x: -80, opacity: 0, stagger: 0.15, duration: 1.2, ease: "power4.out" });
                break;
            case "slide-right":
                tl.from(children, { x: 80, opacity: 0, stagger: 0.15, duration: 1.2, ease: "power4.out" });
                break;
            case "scale-up":
                tl.from(children, { scale: 0.9, y: 40, opacity: 0, stagger: 0.15, duration: 1.2, ease: "power3.out" });
                break;
            case "clip-reveal":
                tl.from(children, { clipPath: "inset(100% 0 0 0)", y: 40, opacity: 0, stagger: 0.15, duration: 1.2, ease: "power4.inOut" });
                break;
            default:
                tl.from(children, { y: 60, opacity: 0, stagger: 0.15, duration: 1.2, ease: "power4.out" });
        }

        // Trigger Play/Reverse based on global scroll position
        const scrollContainer = document.getElementById("scroll-container");
        let played = false;

        ScrollTrigger.create({
            trigger: scrollContainer,
            start: "top top",
            end: "bottom bottom",
            scrub: true,
            onUpdate: (self) => {
                const p = self.progress;

                // Inside the active viewing window
                if (p >= enter && p <= leave) {
                    if (!played) {
                        tl.play();
                        played = true;
                    }
                }
                // Scrolled past it (reverse it, unless persist is true)
                else if (p > leave) {
                    if (played && !persist) {
                        tl.reverse();
                        played = false;
                    }
                }
                // Scrolled above it (reverse to hide)
                else if (p < enter) {
                    if (played) {
                        tl.reverse();
                        played = false;
                    }
                }
            }
        });
    }

    // Start loading frames right away
    loadFrames();
});

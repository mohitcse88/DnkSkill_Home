// Tailwind Configuration
tailwind.config = {
    theme: {
        extend: {
            colors: {
                border: "hsl(210 20% 90%)",
                input: "hsl(210 20% 90%)",
                ring: "hsl(163 88% 20%)",
                background: "hsl(0 0% 100%)",
                foreground: "hsl(220 20% 15%)",
                primary: {
                    DEFAULT: "#059669",
                    foreground: "hsl(0 0% 100%)",
                },
                secondary: {
                    DEFAULT: "hsl(163 30% 95%)",
                    foreground: "#065f46",
                },
                muted: {
                    DEFAULT: "hsl(210 20% 96%)",
                    foreground: "hsl(220 10% 46%)",
                },
                card: {
                    DEFAULT: "hsl(0 0% 100%)",
                    foreground: "hsl(220 20% 15%)",
                },
                hero: "#f3fbf8",
            },
            borderRadius: {
                lg: "0.5rem",
                md: "calc(0.5rem - 2px)",
                sm: "calc(0.5rem - 4px)",
            }
        }
    }
};

document.addEventListener('DOMContentLoaded', () => {
    // Initialize Lucide icons
    if (typeof lucide !== 'undefined') {
        lucide.createIcons();
    }

    // Mobile menu toggle
    const menuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    const menuIcon = document.getElementById('menu-icon');
    const closeIcon = document.getElementById('close-icon');
    const mobileLinks = document.querySelectorAll('.mobile-link');

    let isMenuOpen = false;

    function toggleMenu() {
        isMenuOpen = !isMenuOpen;
        if (isMenuOpen) {
            if (mobileMenu) mobileMenu.classList.remove('hidden');
            if (mobileMenu) mobileMenu.classList.add('flex');
            if (menuIcon) menuIcon.classList.add('hidden');
            if (closeIcon) closeIcon.classList.remove('hidden');
        } else {
            if (mobileMenu) mobileMenu.classList.add('hidden');
            if (mobileMenu) mobileMenu.classList.remove('flex');
            if (menuIcon) menuIcon.classList.remove('hidden');
            if (closeIcon) closeIcon.classList.add('hidden');
        }
    }

    if (menuBtn) {
        menuBtn.addEventListener('click', toggleMenu);
    }

    // Close mobile menu when a link is clicked
    if (mobileLinks) {
        mobileLinks.forEach(link => {
            link.addEventListener('click', () => {
                if (isMenuOpen) toggleMenu();
            });
        });
    }


    // --- Dynamic AOS (Animate On Scroll) Setup ---

    // Animate Courses Cards
    const coursesCards = document.querySelectorAll('#courses .bg-card');
    coursesCards.forEach((card, index) => {
        card.setAttribute('data-aos', 'fade-up');
        card.setAttribute('data-aos-delay', (index % 3) * 100);
    });

    // Animate Why Choose Cards
    const whyChooseCards = document.querySelectorAll('section.bg-hero .bg-card');
    whyChooseCards.forEach((card, index) => {
        card.setAttribute('data-aos', 'fade-up');
        card.setAttribute('data-aos-delay', (index % 3) * 100);
    });

    // Animate Mentors Cards
    const mentorsCards = document.querySelectorAll('#mentors-carousel .bg-card');
    mentorsCards.forEach((card, index) => {
        card.setAttribute('data-aos', 'zoom-in');
        card.setAttribute('data-aos-delay', (index % 4) * 100);
    });

    if (typeof window.AOS !== 'undefined') {
        window.AOS.init({
            once: true,
            offset: 50,
            duration: 800
        });
    }

    // Roadmap Auto-Hover Loop
    const roadmapSteps = document.querySelectorAll('.roadmap-step');
    const roadmapContainer = roadmapSteps[0]?.parentElement;
    if (roadmapSteps.length > 0 && roadmapContainer) {
        let roadmapIndex = 0;
        let roadmapInterval;

        const startRoadmapLoop = () => {
            if (roadmapInterval) clearInterval(roadmapInterval);
            roadmapInterval = setInterval(() => {
                roadmapSteps.forEach(step => step.classList.remove('is-active'));
                roadmapSteps[roadmapIndex].classList.add('is-active');
                roadmapIndex = (roadmapIndex + 1) % roadmapSteps.length;
            }, 1250); // 1.25-second interval
        };

        const stopRoadmapLoop = () => {
            clearInterval(roadmapInterval);
            roadmapInterval = null;
            roadmapSteps.forEach(step => step.classList.remove('is-active'));
        };

        // Start initial loop with first step active
        roadmapSteps[0].classList.add('is-active');
        roadmapIndex = 1;
        startRoadmapLoop();

        // Pause on hover
        roadmapContainer.addEventListener('mouseenter', stopRoadmapLoop);
        roadmapContainer.addEventListener('mouseleave', () => {
            roadmapIndex = 0;
            startRoadmapLoop();
        });
    }

    // --- Premium LMS Showcase Logic ---
    const lmsTabs = document.querySelectorAll('.lms-tab');
    const lmsImages = [
        document.getElementById('tab-img-0'),
        document.getElementById('tab-img-1'),
        document.getElementById('tab-img-2'),
        document.getElementById('tab-img-3')
    ];

    if (lmsTabs.length > 0) {
        let currentLmsTab = 0;
        let lmsAutoplayInterval;

        const activateLmsTab = (index) => {
            lmsTabs.forEach((tab, i) => {
                const progressBar = tab.querySelector('.lms-progress');
                const arrow = tab.querySelector('.lms-arrow');
                const iconContainer = tab.querySelector('div.rounded-full');

                if (i === index) {
                    // Set active
                    tab.classList.remove('border-border', 'bg-card', 'hover:border-primary/50');
                    tab.classList.add('border-primary', 'bg-primary/5', 'shadow-sm', 'active');
                    if (arrow) {
                        arrow.classList.remove('opacity-0');
                        arrow.classList.add('opacity-100');
                    }

                    // Active Icon styles
                    if (iconContainer) {
                        iconContainer.classList.remove('bg-secondary', 'text-primary/70');
                        iconContainer.classList.add('bg-white', 'text-primary', 'shadow-sm');
                    }

                    // Start progress animation
                    if (progressBar) {
                        progressBar.style.transition = 'none';
                        progressBar.style.width = '0%';
                        void progressBar.offsetWidth; // force reflow
                        progressBar.style.transition = lmsAutoplayInterval ? 'width 4000ms linear' : 'width 300ms ease';
                        progressBar.style.width = '100%';
                    }

                    // Show image
                    if (lmsImages[i]) {
                        lmsImages[i].classList.remove('opacity-0');
                        lmsImages[i].classList.add('opacity-100');
                    }
                } else {
                    // Set inactive
                    tab.classList.add('border-border', 'bg-card', 'hover:border-primary/50');
                    tab.classList.remove('border-primary', 'bg-primary/5', 'shadow-sm', 'active');
                    if (arrow) {
                        arrow.classList.remove('opacity-100');
                        arrow.classList.add('opacity-0');
                    }

                    // Inactive Icon styles
                    if (iconContainer) {
                        iconContainer.classList.add('bg-secondary', 'text-primary/70');
                        iconContainer.classList.remove('bg-white', 'text-primary', 'shadow-sm');
                    }

                    // Reset progress animation
                    if (progressBar) {
                        progressBar.style.transition = 'none';
                        progressBar.style.width = '0%';
                    }

                    // Hide image
                    if (lmsImages[i]) {
                        lmsImages[i].classList.remove('opacity-100');
                        lmsImages[i].classList.add('opacity-0');
                    }
                }
            });
            currentLmsTab = index;
        };

        const startLmsCycle = () => {
            if (lmsAutoplayInterval) clearInterval(lmsAutoplayInterval);
            lmsAutoplayInterval = setInterval(() => {
                let nextTab = (currentLmsTab + 1) % lmsTabs.length;
                activateLmsTab(nextTab);
            }, 4000);
        };

        const stopLmsCycle = () => {
            clearInterval(lmsAutoplayInterval);
            lmsAutoplayInterval = null;
            // Keep the progress bar full for the current active tab
            const activeBar = lmsTabs[currentLmsTab].querySelector('.lms-progress');
            if (activeBar) {
                activeBar.style.transition = 'width 300ms ease';
                activeBar.style.width = '100%';
            }
        };

        // Click interaction
        lmsTabs.forEach((tab, index) => {
            tab.addEventListener('click', () => {
                stopLmsCycle();
                activateLmsTab(index);
            });

            // Re-start cycle on mouse leave if we want it to continue? 
            // The user said "automatic hove hota hai", usually means it cycles automatically.
            // Let's make it pause on hover and resume on leave for better UX.
            tab.addEventListener('mouseenter', () => {
                stopLmsCycle();
                activateLmsTab(index);
            });
        });

        const lmsSection = document.querySelector('.lms-tab')?.closest('.grid');
        if (lmsSection) {
            lmsSection.addEventListener('mouseleave', () => {
                startLmsCycle();
                activateLmsTab(currentLmsTab);
            });
        }

        // Initialize
        activateLmsTab(0);
        startLmsCycle();
    }
});

document.addEventListener('DOMContentLoaded', () => {
    gsap.registerPlugin(ScrollTrigger);
    initLoader();
    initNavigation();
    initScrollAnimations();
    initCounters();
    initFlashMessages();
    initScrollToTop();
});

function initLoader() {
    const loader = document.getElementById('loading-screen');
    if (!loader) return;
    window.addEventListener('load', () => {
        gsap.to(loader, {
            opacity: 0,
            duration: 0.8,
            ease: 'power2.out',
            onComplete: () => loader.remove()
        });
        animateHero();
    });
}

function animateHero() {
    const hero = document.querySelector('.hero-content');
    if (!hero) return;
    gsap.from(hero.children, {
        y: 40,
        opacity: 0,
        stagger: 0.12,
        duration: 1,
        ease: 'power3.out'
    });
}

function initNavigation() {
    const nav = document.querySelector('.nav-wrapper');
    const mobileBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');

    if (mobileBtn && mobileMenu) {
        mobileBtn.addEventListener('click', () => {
            const isHidden = mobileMenu.classList.contains('hidden');
            mobileMenu.classList.toggle('hidden');
            if (!isHidden) return;
            gsap.fromTo(
                mobileMenu,
                { height: 0, opacity: 0 },
                { height: 'auto', opacity: 1, duration: 0.3, ease: 'power2.out' }
            );
        });
    }

    window.addEventListener('scroll', () => {
        if (!nav) return;
        if (window.scrollY > 24) {
            nav.classList.add('scrolled');
        } else {
            nav.classList.remove('scrolled');
        }
    });
}

function initScrollAnimations() {
    gsap.utils.toArray('.section-trigger').forEach((section) => {
        gsap.from(section, {
            y: 60,
            opacity: 0,
            duration: 1,
            ease: 'power2.out',
            scrollTrigger: {
                trigger: section,
                start: 'top 75%'
            }
        });
    });

    gsap.utils.toArray('.project-card').forEach((card, index) => {
        gsap.from(card, {
            y: 40,
            opacity: 0,
            delay: index * 0.05,
            scrollTrigger: {
                trigger: card,
                start: 'top 80%'
            }
        });
    });

    gsap.utils.toArray('.timeline-item').forEach((item) => {
        gsap.from(item, {
            x: -30,
            opacity: 0,
            duration: 0.8,
            scrollTrigger: {
                trigger: item,
                start: 'top 85%'
            }
        });
    });

    gsap.utils.toArray('.project-preview').forEach((preview) => {
        gsap.from(preview, {
            scale: 0.95,
            opacity: 0,
            duration: 0.9,
            scrollTrigger: {
                trigger: preview,
                start: 'top 80%'
            }
        });
    });

    gsap.utils.toArray('.partner-logo').forEach((logo) => {
        gsap.from(logo, {
            y: 30,
            opacity: 0,
            duration: 0.6,
            scrollTrigger: {
                trigger: logo,
                start: 'top 90%'
            }
        });
    });

    gsap.utils.toArray('.workflow-node').forEach((node, index) => {
        gsap.from(node, {
            y: 40,
            opacity: 0,
            duration: 0.7,
            delay: index * 0.1,
            scrollTrigger: {
                trigger: node,
                start: 'top 85%'
            }
        });
    });
}

function initCounters() {
    const counters = document.querySelectorAll('[data-counter]');
    counters.forEach((counter) => {
        const target = parseInt(counter.dataset.counter, 10);
        ScrollTrigger.create({
            trigger: counter,
            start: 'top 85%',
            onEnter: () => animateCounter(counter, target)
        });
    });
}

function animateCounter(element, target) {
    gsap.fromTo(
        { value: 0 },
        { value: target, duration: 1.8, ease: 'power2.out',
            onUpdate: function() {
                element.textContent = Math.round(this.targets()[0].value).toLocaleString('fr-FR');
            }
        }
    );
}

function initFlashMessages() {
    document.querySelectorAll('[data-flash]').forEach((flash) => {
        setTimeout(() => {
            gsap.to(flash, {
                x: 40,
                opacity: 0,
                duration: 0.4,
                onComplete: () => flash.remove()
            });
        }, 4500);
    });
}

function initScrollToTop() {
    const btn = document.createElement('button');
    btn.id = 'scroll-top';
    btn.className = 'fixed bottom-6 right-6 w-12 h-12 rounded-full bg-aurora text-midnight shadow-glow opacity-0 pointer-events-none transition-all duration-300 z-40';
    btn.innerHTML = '&uarr;';
    document.body.appendChild(btn);

    window.addEventListener('scroll', () => {
        if (window.scrollY > 400) {
            btn.style.opacity = '1';
            btn.style.pointerEvents = 'auto';
        } else {
            btn.style.opacity = '0';
            btn.style.pointerEvents = 'none';
        }
    });

    btn.addEventListener('click', () => {
        window.scrollTo({ top: 0, behavior: 'smooth' });
    });
}

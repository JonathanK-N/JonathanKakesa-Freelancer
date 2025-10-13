// Main JavaScript file for Cognito Inc. website
// Animations, interactions, and dynamic behaviors

document.addEventListener('DOMContentLoaded', function() {
    // Initialize GSAP
    gsap.registerPlugin(ScrollTrigger);
    
    // Loading screen animation
    initLoadingScreen();
    
    // Navigation functionality
    initNavigation();
    
    // Scroll animations
    initScrollAnimations();
    
    // Interactive elements
    initInteractiveElements();
    
    // Form enhancements
    initFormEnhancements();
    
    // Parallax effects
    initParallaxEffects();
});

// Loading Screen Animation
function initLoadingScreen() {
    const loadingScreen = document.getElementById('loading-screen');
    
    if (loadingScreen) {
        // Animate loading screen out after page load
        window.addEventListener('load', function() {
            gsap.to(loadingScreen, {
                opacity: 0,
                duration: 0.8,
                ease: "power2.out",
                onComplete: function() {
                    loadingScreen.style.display = 'none';
                    // Trigger entrance animations
                    animatePageEntrance();
                }
            });
        });
    }
}

// Page Entrance Animations
function animatePageEntrance() {
    // Hero content animation
    const heroContent = document.querySelector('.hero-content');
    if (heroContent) {
        gsap.from(heroContent.children, {
            y: 50,
            opacity: 0,
            duration: 1,
            stagger: 0.2,
            ease: "power2.out"
        });
    }
    
    // Animate navigation
    gsap.from('nav', {
        y: -100,
        opacity: 0,
        duration: 0.8,
        ease: "power2.out"
    });
}

// Navigation Functionality
function initNavigation() {
    const mobileMenuBtn = document.getElementById('mobile-menu-btn');
    const mobileMenu = document.getElementById('mobile-menu');
    
    if (mobileMenuBtn && mobileMenu) {
        mobileMenuBtn.addEventListener('click', function() {
            const isHidden = mobileMenu.classList.contains('hidden');
            
            if (isHidden) {
                mobileMenu.classList.remove('hidden');
                gsap.from(mobileMenu, {
                    height: 0,
                    opacity: 0,
                    duration: 0.3,
                    ease: "power2.out"
                });
            } else {
                gsap.to(mobileMenu, {
                    height: 0,
                    opacity: 0,
                    duration: 0.3,
                    ease: "power2.out",
                    onComplete: function() {
                        mobileMenu.classList.add('hidden');
                    }
                });
            }
        });
    }
    
    // Smooth scrolling for anchor links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const target = document.querySelector(this.getAttribute('href'));
            if (target) {
                target.scrollIntoView({
                    behavior: 'smooth',
                    block: 'start'
                });
            }
        });
    });
    
    // Navigation background on scroll
    window.addEventListener('scroll', function() {
        const nav = document.querySelector('nav');
        if (window.scrollY > 50) {
            nav.classList.add('backdrop-blur-lg');
        } else {
            nav.classList.remove('backdrop-blur-lg');
        }
    });
}

// Scroll Animations
function initScrollAnimations() {
    // Fade in animations for sections
    gsap.utils.toArray('section').forEach(section => {
        gsap.from(section, {
            y: 50,
            opacity: 0,
            duration: 1,
            scrollTrigger: {
                trigger: section,
                start: "top 80%",
                end: "bottom 20%",
                toggleActions: "play none none reverse"
            }
        });
    });
    
    // Project cards animation
    gsap.utils.toArray('.project-card').forEach((card, index) => {
        gsap.from(card, {
            y: 50,
            opacity: 0,
            duration: 0.8,
            delay: index * 0.1,
            scrollTrigger: {
                trigger: card,
                start: "top 85%",
                toggleActions: "play none none reverse"
            }
        });
    });
    
    // Service cards animation
    gsap.utils.toArray('.service-card').forEach((card, index) => {
        gsap.from(card, {
            x: index % 2 === 0 ? -50 : 50,
            opacity: 0,
            duration: 1,
            scrollTrigger: {
                trigger: card,
                start: "top 80%",
                toggleActions: "play none none reverse"
            }
        });
    });
    
    // Testimonial cards animation
    gsap.utils.toArray('.testimonial-card').forEach((card, index) => {
        gsap.from(card, {
            scale: 0.8,
            opacity: 0,
            duration: 0.8,
            delay: index * 0.2,
            scrollTrigger: {
                trigger: card,
                start: "top 85%",
                toggleActions: "play none none reverse"
            }
        });
    });
    
    // Counter animation
    gsap.utils.toArray('[data-counter]').forEach(counter => {
        const target = parseInt(counter.getAttribute('data-counter'));
        gsap.from(counter, {
            textContent: 0,
            duration: 2,
            ease: "power2.out",
            snap: { textContent: 1 },
            scrollTrigger: {
                trigger: counter,
                start: "top 80%",
                toggleActions: "play none none reverse"
            }
        });
    });
}

// Interactive Elements
function initInteractiveElements() {
    // Project card hover effects
    document.querySelectorAll('.project-card').forEach(card => {
        card.addEventListener('mouseenter', function() {
            gsap.to(this, {
                y: -10,
                duration: 0.3,
                ease: "power2.out"
            });
        });
        
        card.addEventListener('mouseleave', function() {
            gsap.to(this, {
                y: 0,
                duration: 0.3,
                ease: "power2.out"
            });
        });
    });
    
    // Button hover effects
    document.querySelectorAll('button, .btn, a[class*="bg-electric-blue"]').forEach(btn => {
        btn.addEventListener('mouseenter', function() {
            gsap.to(this, {
                scale: 1.05,
                duration: 0.2,
                ease: "power2.out"
            });
        });
        
        btn.addEventListener('mouseleave', function() {
            gsap.to(this, {
                scale: 1,
                duration: 0.2,
                ease: "power2.out"
            });
        });
    });
    
    // Glow effect on hover for special elements
    document.querySelectorAll('.gradient-text').forEach(element => {
        element.addEventListener('mouseenter', function() {
            gsap.to(this, {
                textShadow: "0 0 20px #00D4FF",
                duration: 0.3
            });
        });
        
        element.addEventListener('mouseleave', function() {
            gsap.to(this, {
                textShadow: "none",
                duration: 0.3
            });
        });
    });
}

// Form Enhancements
function initFormEnhancements() {
    // Form field focus animations
    document.querySelectorAll('input, textarea').forEach(field => {
        field.addEventListener('focus', function() {
            gsap.to(this, {
                scale: 1.02,
                duration: 0.2,
                ease: "power2.out"
            });
        });
        
        field.addEventListener('blur', function() {
            gsap.to(this, {
                scale: 1,
                duration: 0.2,
                ease: "power2.out"
            });
        });
    });
    
    // Form submission animation
    document.querySelectorAll('form').forEach(form => {
        form.addEventListener('submit', function(e) {
            const submitBtn = this.querySelector('input[type="submit"], button[type="submit"]');
            if (submitBtn) {
                submitBtn.disabled = true;
                submitBtn.innerHTML = 'Envoi en cours...';
                
                gsap.to(submitBtn, {
                    scale: 0.95,
                    duration: 0.1,
                    yoyo: true,
                    repeat: 1
                });
            }
        });
    });
}

// Parallax Effects
function initParallaxEffects() {
    // Background elements parallax
    gsap.utils.toArray('.bg-gradient-to-r').forEach(bg => {
        gsap.to(bg, {
            yPercent: -50,
            ease: "none",
            scrollTrigger: {
                trigger: bg,
                start: "top bottom",
                end: "bottom top",
                scrub: true
            }
        });
    });
    
    // Hero background animation
    const heroSection = document.querySelector('section');
    if (heroSection) {
        gsap.to(heroSection.querySelectorAll('.absolute'), {
            y: -100,
            ease: "none",
            scrollTrigger: {
                trigger: heroSection,
                start: "top top",
                end: "bottom top",
                scrub: true
            }
        });
    }
}

// Utility Functions
function animateCounter(element, target, duration = 2) {
    gsap.to(element, {
        textContent: target,
        duration: duration,
        ease: "power2.out",
        snap: { textContent: 1 },
        onUpdate: function() {
            element.textContent = Math.ceil(element.textContent);
        }
    });
}

// Testimonials Carousel (if needed)
function initTestimonialsCarousel() {
    const testimonials = document.querySelectorAll('.testimonial-card');
    if (testimonials.length > 2) {
        let currentIndex = 0;
        
        setInterval(() => {
            gsap.to(testimonials[currentIndex], {
                opacity: 0,
                x: -100,
                duration: 0.5,
                onComplete: function() {
                    testimonials[currentIndex].style.display = 'none';
                }
            });
            
            currentIndex = (currentIndex + 1) % testimonials.length;
            
            testimonials[currentIndex].style.display = 'block';
            gsap.from(testimonials[currentIndex], {
                opacity: 0,
                x: 100,
                duration: 0.5
            });
        }, 5000);
    }
}

// Flash messages auto-hide
document.querySelectorAll('[class*="flash"]').forEach(flash => {
    setTimeout(() => {
        gsap.to(flash, {
            opacity: 0,
            x: 100,
            duration: 0.5,
            onComplete: function() {
                flash.remove();
            }
        });
    }, 5000);
});

// Scroll to top functionality
function addScrollToTop() {
    const scrollBtn = document.createElement('button');
    scrollBtn.innerHTML = '↑';
    scrollBtn.className = 'fixed bottom-8 right-8 w-12 h-12 bg-electric-blue text-dark-bg rounded-full font-bold opacity-0 pointer-events-none transition-all duration-300 z-50';
    scrollBtn.id = 'scroll-to-top';
    document.body.appendChild(scrollBtn);
    
    window.addEventListener('scroll', function() {
        if (window.scrollY > 500) {
            scrollBtn.style.opacity = '1';
            scrollBtn.style.pointerEvents = 'auto';
        } else {
            scrollBtn.style.opacity = '0';
            scrollBtn.style.pointerEvents = 'none';
        }
    });
    
    scrollBtn.addEventListener('click', function() {
        window.scrollTo({
            top: 0,
            behavior: 'smooth'
        });
    });
}

// Initialize scroll to top
addScrollToTop();

// Performance optimization
function debounce(func, wait) {
    let timeout;
    return function executedFunction(...args) {
        const later = () => {
            clearTimeout(timeout);
            func(...args);
        };
        clearTimeout(timeout);
        timeout = setTimeout(later, wait);
    };
}

// Optimized scroll handler
const optimizedScrollHandler = debounce(function() {
    // Handle scroll-based animations here
}, 16); // ~60fps

window.addEventListener('scroll', optimizedScrollHandler);

// Console welcome message
console.log(`
🚀 Cognito Inc. - Jonathan Kakesa
💻 Développé avec passion et innovation
🌟 Contactez-moi pour vos projets : jonathan@cognito-inc.com
`);

// Export functions for potential external use
window.CognitoAnimations = {
    animateCounter,
    initTestimonialsCarousel,
    debounce
};
// ── Hamburger menu — slide from right drawer ─────────────────────
const hamburger = document.getElementById('hamburger');
const mobileMenu = document.getElementById('mobileMenu');
const mobileClose = document.getElementById('mobileClose');

// Create backdrop dynamically
const backdrop = document.createElement('div');
backdrop.className = 'mobile-backdrop';
document.body.appendChild(backdrop);

function openMenu() {
  hamburger.classList.add('open');
  mobileMenu.classList.add('open');
  backdrop.classList.add('open');
  document.body.style.overflow = 'hidden';
}
function closeMenu() {
  hamburger.classList.remove('open');
  mobileMenu.classList.remove('open');
  backdrop.classList.remove('open');
  document.body.style.overflow = '';
}

if (hamburger && mobileMenu) {
  hamburger.addEventListener('click', () => {
    mobileMenu.classList.contains('open') ? closeMenu() : openMenu();
  });
  if (mobileClose) mobileClose.addEventListener('click', closeMenu);
  backdrop.addEventListener('click', closeMenu);
  // Close on nav link click
  mobileMenu.querySelectorAll('.mobile-link').forEach(link => {
    link.addEventListener('click', closeMenu);
  });
}

// ── Navbar scroll shadow ─────────────────────────────────────────
const navbar = document.getElementById('navbar');
if (navbar) {
  window.addEventListener('scroll', () => {
    navbar.style.boxShadow = window.scrollY > 10
      ? '0 2px 20px rgba(0,0,0,0.08)'
      : 'none';
  }, { passive: true });
}

// ── Scroll reveal ────────────────────────────────────────────────
const revealEls = document.querySelectorAll('.reveal-up, .reveal-right, .reveal-left');
if (revealEls.length) {
  const observer = new IntersectionObserver(entries => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        const delay = entry.target.style.animationDelay || '0s';
        const ms = parseFloat(delay) * 1000;
        setTimeout(() => entry.target.classList.add('visible'), ms);
        observer.unobserve(entry.target);
      }
    });
  }, { threshold: 0.12 });
  revealEls.forEach(el => observer.observe(el));
}

// ── FAQ accordion ────────────────────────────────────────────────
document.querySelectorAll('.faq-question').forEach(btn => {
  btn.addEventListener('click', () => {
    const item = btn.closest('.faq-item');
    const answer = item.querySelector('.faq-answer');
    const isOpen = item.classList.contains('open');
    // Close all
    document.querySelectorAll('.faq-item').forEach(i => {
      i.classList.remove('open');
      i.querySelector('.faq-answer').style.maxHeight = null;
    });
    // Open clicked if it was closed
    if (!isOpen) {
      item.classList.add('open');
      answer.style.maxHeight = answer.scrollHeight + 'px';
    }
  });
});

// ── Contact form ─────────────────────────────────────────────────
const contactForm = document.getElementById('contactForm');
if (contactForm) {
  contactForm.addEventListener('submit', e => {
    e.preventDefault();
    const btn = contactForm.querySelector('button[type=submit]');
    btn.textContent = 'Request Sent ✓';
    btn.disabled = true;
    btn.style.background = '#5c6b3a';
    const msg = document.getElementById('formSuccess');
    if (msg) msg.style.display = 'block';
    contactForm.reset();
  });
}

// ── Active nav link highlight ────────────────────────────────────
const currentPath = window.location.pathname.split('/').pop() || 'index.html';
document.querySelectorAll('.nav-link').forEach(link => {
  const href = link.getAttribute('href');
  if (href && href.includes(currentPath) && currentPath !== '') {
    link.classList.add('active');
  }
});

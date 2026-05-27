/* ============================================================
   NAVIGATION – switch between pages
   ============================================================ */
(function () {
  'use strict';

  const navLinks = document.querySelectorAll('.nav-link');
  const pages    = document.querySelectorAll('.page');
  const sidebar  = document.getElementById('sidebar');
  const toggle   = document.getElementById('sidebar-toggle');

  /** Show a page by id, hide others */
  function showPage(pageId) {
    pages.forEach(p => p.classList.toggle('active', p.id === pageId));
    navLinks.forEach(l => l.classList.toggle('active', l.dataset.page === pageId));
    // Scroll main content back to top
    document.getElementById('main-content').scrollTo({ top: 0, behavior: 'smooth' });
    // Update hash without triggering scroll
    history.pushState(null, '', '#' + pageId);
  }

  /** Wire nav link clicks */
  navLinks.forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      showPage(link.dataset.page);
      // Close sidebar on mobile after navigation
      sidebar.classList.remove('open');
    });
  });

  /** Mobile sidebar toggle */
  if (toggle) {
    toggle.addEventListener('click', () => sidebar.classList.toggle('open'));
    // Close sidebar when clicking outside on mobile
    document.addEventListener('click', e => {
      if (!sidebar.contains(e.target) && !toggle.contains(e.target)) {
        sidebar.classList.remove('open');
      }
    });
  }

  /** Restore page from hash on load */
  function restoreFromHash() {
    const hash = window.location.hash.replace('#', '');
    const validPages = ['profile', 'experience', 'education', 'projects', 'certifications'];
    if (validPages.includes(hash)) {
      showPage(hash);
    } else {
      showPage('profile');
    }
  }

  restoreFromHash();
  window.addEventListener('hashchange', restoreFromHash);

  /* -----------------------------------------------------------
     Quick-nav anchor links inside pages
     If the anchor target is in a hidden section, reveal it first
  ----------------------------------------------------------- */
  document.querySelectorAll('.quick-nav a').forEach(link => {
    link.addEventListener('click', e => {
      e.preventDefault();
      const targetId = link.getAttribute('href').replace('#', '');
      const target   = document.getElementById(targetId);
      if (!target) return;
      // Determine which page owns the target
      const ownerPage = target.closest('.page');
      if (ownerPage && !ownerPage.classList.contains('active')) {
        showPage(ownerPage.id);
      }
      setTimeout(() => {
        target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      }, 50);
    });
  });
})();

/* ============================================================
   PDF TOGGLE – open in new tab
   ============================================================ */
function togglePDF(containerId, pdfSrc) {
  window.open(pdfSrc, '_blank', 'noopener,noreferrer');
}

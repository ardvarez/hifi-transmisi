(function () {
  'use strict';

  // Injeksi otomatis link stylesheet hifi-theme.css jika belum ada
  function injectThemeCss() {
    if (document.getElementById('hifi-unified-theme-css')) return;

    // Hitung path relatif ke assets/css/hifi-theme.css berdasarkan posisi dokumen saat ini
    const scripts = document.getElementsByTagName('script');
    let basePath = '';
    for (let s of scripts) {
      if (s.src && s.src.includes('hifi-theme.js')) {
        basePath = s.src.replace(/js\/hifi-theme\.js(\?.*)?$/, 'css/hifi-theme.css');
        break;
      }
    }

    const link = document.createElement('link');
    link.id = 'hifi-unified-theme-css';
    link.rel = 'stylesheet';
    link.href = basePath || '/assets/css/hifi-theme.css';
    document.head.appendChild(link);
  }

  // Toast Container Manager
  let toastContainer = null;
  function getToastContainer() {
    if (!toastContainer) {
      toastContainer = document.getElementById('hifi-toast-container');
      if (!toastContainer) {
        toastContainer = document.createElement('div');
        toastContainer.id = 'hifi-toast-container';
        toastContainer.style.cssText =
          'position: fixed; top: 20px; right: 20px; z-index: 99999; display: flex; flex-direction: column; gap: 10px; max-width: 360px; pointer-events: none;';
        document.body.appendChild(toastContainer);
      }
    }
    return toastContainer;
  }

  // Window Toast API seragam untuk semua halaman
  window.HiFi = window.HiFi || {};
  window.HiFi.showToast = function (message, type = 'info', duration = 3000) {
    const container = getToastContainer();
    const toast = document.createElement('div');
    toast.style.cssText =
      'pointer-events: auto; background: #0F172A; color: #FFFFFF; padding: 12px 16px; border-radius: 8px; font-size: 13px; font-family: Inter, sans-serif; box-shadow: 0 4px 12px rgba(0,0,0,0.15); display: flex; align-items: center; gap: 8px; animation: hifiSlideDown 0.25s ease; border-left: 4px solid #0A58CA;';

    if (type === 'success') toast.style.borderLeftColor = '#16A34A';
    if (type === 'error') toast.style.borderLeftColor = '#DC2626';
    if (type === 'warning') toast.style.borderLeftColor = '#D97706';

    toast.innerText = message;
    container.appendChild(toast);

    setTimeout(() => {
      toast.style.opacity = '0';
      toast.style.transition = 'opacity 0.25s ease';
      setTimeout(() => toast.remove(), 250);
    }, duration);
  };

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', injectThemeCss);
  } else {
    injectThemeCss();
  }
})();

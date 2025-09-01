function applyDarkMode() {
    if (localStorage.getItem('darkMode') === 'true') {
        document.body.classList.add('dark-mode');
    }
}

function toggleDarkMode() {
    document.body.classList.toggle('dark-mode');
    localStorage.setItem('darkMode', document.body.classList.contains('dark-mode'));
}

function showLoading() {
    let overlay = document.getElementById('loadingOverlay');
    if (!overlay) {
        overlay = document.createElement('div');
        overlay.id = 'loadingOverlay';
        overlay.className = 'loading-overlay';
        overlay.textContent = 'Loading...';
        document.body.appendChild(overlay);
    }
}

function hideLoading() {
    const overlay = document.getElementById('loadingOverlay');
    if (overlay) overlay.remove();
}

function showError(message) {
    let err = document.getElementById('error');
    if (!err) {
        err = document.createElement('div');
        err.id = 'error';
        err.className = 'error-message';
        // Optionally style the error element if not styled via CSS
        err.style.position = 'fixed';
        err.style.top = '20px';
        err.style.left = '50%';
        err.style.transform = 'translateX(-50%)';
        err.style.backgroundColor = '#f44336';
        err.style.color = '#fff';
        err.style.padding = '12px 24px';
        err.style.borderRadius = '4px';
        err.style.zIndex = '1000';
        document.body.appendChild(err);
    }
    err.textContent = message;
}

document.addEventListener('DOMContentLoaded', () => {
    applyDarkMode();
    document.addEventListener('keydown', (e) => {
        if (e.shiftKey && e.key === 'D') {
            toggleDarkMode();
        }
        if ((e.ctrlKey || e.metaKey) && e.key === 'Enter') {
            const form = document.querySelector('form');
            if (form) form.requestSubmit();
        }
    });
});

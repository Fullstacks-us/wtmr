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
    const err = document.getElementById('error');
    if (err) {
        err.textContent = message;
    } else {
        alert(message);
    }
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

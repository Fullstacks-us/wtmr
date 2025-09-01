// Configuration for different environments
const CONFIG = {
    // For local development, use relative paths
    // For GitHub Pages deployment, you'll need to set the API_BASE_URL to your backend server
    API_BASE_URL: window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1'
        ? '' // Local development - use relative paths
        : (window.API_BASE_URL || ''), // Production - set window.API_BASE_URL in your deployment
    
    // Environment detection
    isLocal: window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1',
    isGitHubPages: window.location.hostname.includes('github.io')
};

// Warn if API_BASE_URL is not set in production (but not in GitHub Pages demo mode)
if (!CONFIG.isLocal && !CONFIG.isGitHubPages && !CONFIG.API_BASE_URL) {
    alert('API_BASE_URL is not set for production. Please configure window.API_BASE_URL in your deployment.');
}
// API helper functions
const API = {
    async call(endpoint, options = {}) {
        const url = CONFIG.API_BASE_URL + endpoint;
        
        try {
            const response = await fetch(url, {
                ...options,
                headers: {
                    'Content-Type': 'application/json',
                    ...options.headers
                }
            });
            
            if (!response.ok) {
                throw new Error(`HTTP error! status: ${response.status}`);
            }
            
            return response;
        } catch (error) {
            console.error('API call failed:', error);
            
                alert('API is not available. This is a demo deployment. Please set window.API_BASE_URL in your deployment or refer to the deployment documentation for instructions.');
            } else {
                alert('Cannot connect to API. Please check the server.');
            }
            throw error;
        }
    },

    async get(endpoint) {
        const response = await this.call(endpoint);
        return response.json();
    },

    async post(endpoint, data) {
        const response = await this.call(endpoint, {
            method: 'POST',
            body: JSON.stringify(data)
        });
        return response.json();
    },

    async postFormData(endpoint, formData) {
        const response = await this.call(endpoint, {
            method: 'POST',
            body: formData,
            headers: {} // Let browser set Content-Type for FormData
        });
        return response.json();
    }
};
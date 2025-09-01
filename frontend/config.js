// Configuration for different environments
const CONFIG = {
    // For local development, use relative paths
    // For GitHub Pages deployment, you'll need to set the API_BASE_URL to your backend server
    API_BASE_URL: window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1' 
        ? '' // Local development - use relative paths
        : 'https://your-backend-server.com', // Production - replace with actual backend URL
    
    // Environment detection
    isLocal: window.location.hostname === 'localhost' || window.location.hostname === '127.0.0.1',
    isGitHubPages: window.location.hostname.includes('github.io')
};

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
            
            // Show user-friendly error messages
            if (CONFIG.isGitHubPages) {
                alert('API is not available. This is a demo deployment. Please configure your backend server URL in config.js');
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
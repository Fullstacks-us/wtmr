# Water & Mileage Logger (WTMR)

A lightweight, Tailscale-secured web application for logging water tests, meter readings, and mileage records. Built with Python FastAPI backend and HTML/CSS/JS frontend.

Always reference these instructions first and fallback to search or bash commands only when you encounter unexpected information that does not match the info here.

## Working Effectively

### Bootstrap and Run the Application

**Prerequisites:** Python 3.12+ (available in this environment)

1. **Backend Setup** (Takes ~10 seconds total):
   ```bash
   cd backend
   python3 -m venv venv                    # ~3 seconds
   source venv/bin/activate               # instant
   pip install -r requirements.txt       # ~7 seconds
   ```
   **If pip install fails due to network timeouts**: Retry the command or use `pip install --timeout 120 -r requirements.txt`

2. **Start the Server**:
   ```bash
   cd backend
   source venv/bin/activate
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```
   - Server starts in ~2-3 seconds
   - Access API: http://localhost:8000/health
   - Access Frontend: http://localhost:8000/static/index.html

3. **CRITICAL BUG FIX REQUIRED**: On fresh clone, you must fix the static file path in `backend/main.py`:
   ```python
   # CHANGE THIS LINE:
   app.mount("/static", StaticFiles(directory="frontend"), name="static")
   # TO THIS:
   app.mount("/static", StaticFiles(directory="../frontend"), name="static")
   ```
   Without this fix, the server will fail to start with "Directory 'frontend' does not exist" error.

## Validation

**ALWAYS run these complete end-to-end scenarios after making changes:**

### 1. Water Test Workflow Validation
- Navigate to http://localhost:8000/static/index.html
- Click "New Water Test"
- Fill in: pH: 7.4, Chlorine: 2.1, Hardness: 200, Site: "Pool-001", Notes: "Test entry"
- **IMPORTANT**: Upload any image file (form requires it)
- Click "Save Test" - should show "Test saved successfully!" alert
- Navigate back and click "View History" - verify your entry appears

### 2. Water Meter Reading Validation  
- Click "New Water Meter Reading"
- Enter Current Reading: 1250.5, Notes: "Test reading"
- Click "Save Reading" - should show success with delta calculation
- Verify in history view

### 3. Mileage Log Validation
- Click "New Mileage Log" 
- Fill Start/End locations, distance, purpose
- Save and verify in history

### 4. Data Persistence Validation
After creating entries, verify files exist:
```bash
cd backend
ls -la db/        # Should show water_log.json, meter_log.json, mileage_log.json
ls -la images/    # Should show uploaded image files with UUID prefixes
```

## Known Issues and Workarounds

### 1. CRITICAL: Static File Path Bug
**Issue**: Fresh clones have incorrect static file mounting path
**Fix**: Change `directory="frontend"` to `directory="../frontend"` in `backend/main.py` line 27

### 2. JSON Format Inconsistency in Water Logs  
**Issue**: Water log save/read functions use different JSON formats (array vs lines)
**Symptoms**: 500 error when viewing water test history
**Fix**: In `backend/routes/water.py`, the `get_water_logs()` function should use `json.load(f)` not line-by-line parsing

### 3. Required Image Uploads
**Issue**: Water test forms require image uploads (not optional)
**Workaround**: Always upload a test image file when testing water test functionality

## No Build Process Required

- **Frontend**: Pure HTML/CSS/JS - no npm, webpack, or build steps needed
- **Backend**: Direct Python execution - no compilation required  
- **No Tests**: Repository contains no test files or test infrastructure
- **No Linting**: No linting configuration present (flake8, pylint, etc.)

## Directory Structure & Navigation

### Key Locations
```
/backend/               # Python FastAPI application
  main.py              # Main server file (fix static path here)
  requirements.txt     # Python dependencies  
  routes/              # API endpoint definitions
    water.py           # Water test endpoints (has JSON bug)
    meter.py           # Water meter endpoints
    mileage.py         # Mileage logging endpoints
  db/                  # JSON data storage (created on first run)
  images/              # Uploaded photos (created on first run)
  venv/                # Virtual environment (you create this)

/frontend/             # Static HTML/CSS/JS files
  index.html           # Main dashboard page
  form-water-test.html # Water test entry form
  form-meter.html      # Water meter reading form  
  form-mileage.html    # Mileage logging form
  history.html         # Data viewing/filtering page
  export.html          # Data export functionality
```

### Important Files to Check When Debugging
- `backend/main.py`: Server configuration, static file mounting
- `backend/routes/water.py`: Water test logic (check JSON handling)
- `frontend/index.html`: Main navigation and health check
- Any files in `backend/db/`: Saved application data

## Common Development Tasks

### Making Backend Changes
1. Edit Python files in `backend/` or `backend/routes/`
2. Server auto-reloads (uvicorn --reload)
3. Test changes via browser at http://localhost:8000/static/index.html

### Making Frontend Changes
1. Edit HTML/CSS/JS files in `frontend/`
2. Refresh browser (no build step needed)
3. Validate complete user workflows

### Adding New Features
- API endpoints: Add to appropriate file in `backend/routes/`
- Frontend forms: Create new HTML file in `frontend/`
- Navigation: Update links in `frontend/index.html`

### Troubleshooting Server Issues
1. Check if running: `curl http://localhost:8000/health`
2. View server logs in terminal where uvicorn is running
3. Common errors:
   - Static directory not found → Fix path in main.py
   - 500 on API calls → Check JSON format in route files
   - Module import errors → Ensure venv is activated

## Environment & Configuration

### Optional Environment Setup
- Copy `backend/.env.example` to `backend/.env` if needed
- Default configuration works for local development
- Environment variables are not required for basic operation

### Port and Access
- Default port: 8000
- Backend API: http://localhost:8000/
- Frontend access: http://localhost:8000/static/
- Health check: http://localhost:8000/health

### Data Storage
- Uses JSON files, not a database
- Data persists in `backend/db/` directory
- Images stored in `backend/images/` directory
- No database setup or migrations required

## Performance Notes

- **Startup time**: ~10 seconds for full setup from scratch
- **Server start**: ~2-3 seconds
- **No timeouts needed**: All operations complete quickly
- **Memory usage**: Minimal - suitable for development environments
- **File I/O**: Direct JSON file read/write (not optimized for high volume)

This is a simple application perfect for rapid development and testing. The main complexity is ensuring the static file path is correct and understanding the JSON storage format.
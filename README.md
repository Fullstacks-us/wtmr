# Water & Mileage Logger

A lightweight, Tailscale-secured web-based system for logging water tests, meter readings, and mileage records. Built for iPhone/desktop use with no public access — Tailscale-only.

## 🚀 Features

- **Water Test Logging**
  - pH, Chlorine, Hardness readings
  - Photo capture/upload
  - Test site tracking
  - Category-based organization

- **Water Meter Logging**
  - Reading input with delta calculation
  - Optional photo documentation
  - Daily tracking

- **Mileage Logging**
  - Start/End locations
  - Distance tracking
  - Billable flag
  - Purpose documentation

- **History & Export**
  - Filterable history view
  - Date range selection
  - Category filtering
  - Full-text search
  - CSV export
  - Photo viewing

## 🛠️ Tech Stack

- **Frontend**: HTML/JS (Vite + React optional)
- **Backend**: Python + FastAPI
- **Storage**: JSON Lines (1-per-record)
- **Network**: Tailscale-secured
- **Authentication**: Tailscale device validation

## 🏗️ Setup

1. **Clone & Install**
   ```bash
   git clone https://github.com/Fullstacks-us/wtmr.git
   cd wtmr
   ```

2. **Backend Setup**
   ```bash
   cd backend
   python3 -m venv venv
   source venv/bin/activate  # or `venv\Scripts\activate` on Windows
   pip install -r requirements.txt
   uvicorn main:app --host 0.0.0.0 --port 8000
   ```

3. **Frontend Setup**
   ```bash
   cd frontend
   # For static HTML version:
   python3 -m http.server 3000
   ```

4. **Tailscale Setup (Optional)**
   - Install Tailscale on your VPS and devices
   - Join devices to your tailnet
   - Access via Tailscale IP

## 🚀 Deployment

This app automatically deploys to GitHub Pages when changes are pushed to `main`. The frontend will be available at:
https://fullstacks-us.github.io/wtmr/

For backend deployment options and configuration, see [DEPLOYMENT.md](DEPLOYMENT.md).

## 📝 Usage

1. **Water Tests**
   - Navigate to water test form
   - Enter readings
   - Upload photo if needed
   - Save record

2. **Water Meter**
   - Enter current reading
   - System calculates delta
   - Add optional notes/photo

3. **Mileage**
   - Enter start/end locations
   - Add distance
   - Mark if billable
   - Add purpose

4. **History View**
   - Filter by date/category
   - Search across fields
   - View/edit/delete records
   - Export to CSV

## 🔒 Security

- No public access
- Tailscale-only network
- Optional delete PIN
- Local data storage

## 🚧 Future Features

- DeepSeek summarization
- Combined master export
- Chart drilldowns
- Mobile push reminders
- Scheduled backups
- Offline-first PWA
- Vite + Tailwind polish

## 📁 Project Structure

```
project-root/
├── backend/
│   ├── main.py
│   ├── routes/
│   │   ├── water.py
│   │   ├── meter.py
│   │   ├── mileage.py
│   │   └── summarize.py
│   └── db/
├── frontend/
│   ├── index.html
│   ├── history.html
│   ├── export.html
│   └── scripts/
├── images/
└── docker-compose.yml
```

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details. 
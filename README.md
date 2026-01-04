# 🦈 Manhwa Search Aggregator

A real-time manhwa search engine that aggregates results from multiple platforms with a beautiful galaxy-themed pixel shark UI.

## Features

- 🔍 **Real-time Search**: Fetches live data from multiple manhwa platforms
- 📊 **Smart Ranking**: Results sorted by trust score and relevance
- 🎨 **Beautiful UI**: Galaxy-themed interface with animated pixel shark
- ⚡ **Fast Performance**: Concurrent scraping for quick results
- 🌐 **Multiple Sources**: MangaDex, Webtoons, AsuraScans, and more

## Architecture

```
Backend (Python/Flask):
- Flask REST API server
- Concurrent web scrapers for multiple platforms
- Smart ranking algorithm based on source trust and relevance

Frontend (React):
- Modern React UI with smooth animations
- Real-time search results
- Responsive design with card-based layout
```

## Installation & Setup

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the Flask server
python app.py
```

The backend will run on `http://localhost:5000`

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install dependencies
npm install

# Start the development server
npm start
```

The frontend will run on `http://localhost:3000`

## Usage

1. Start both backend and frontend servers
2. Open `http://localhost:3000` in your browser
3. Enter a manhwa title in the search bar
4. Watch the pixel shark swim while results load!
5. Browse ranked results from multiple platforms

## API Endpoints

### `GET /api/search?q={query}`

Search for manhwas across all platforms.

**Parameters:**
- `q` (required): Search query

**Response:**
```json
{
  "query": "solo leveling",
  "total_results": 15,
  "results": [
    {
      "title": "Solo Leveling",
      "url": "https://...",
      "thumbnail": "https://...",
      "source": "MangaDex",
      "description": "...",
      "trust_score": 9,
      "ranking_score": 8.5
    }
  ]
}
```

### `GET /api/health`

Check API health status.

## Adding New Scrapers

1. Create a new scraper in `backend/scrapers/`:

```python
from .base_scraper import BaseScraper

class YourSiteScraper(BaseScraper):
    def __init__(self):
        super().__init__(
            name="YourSite",
            base_url="https://yoursite.com",
            trust_score=7
        )
    
    def search(self, query):
        # Implement search logic
        return results
```

2. Register in `backend/scrapers/__init__.py`
3. Add to scrapers list in `backend/app.py`

## Trust Score System

- **10**: Official platforms (Webtoons)
- **9**: Major databases (MangaDex)
- **7-8**: Popular scanlation sites
- **5-6**: Community sites
- **1-4**: Aggregator sites

## Technologies Used

### Backend
- Flask (Web framework)
- Requests (HTTP client)
- BeautifulSoup4 (Web scraping)
- Flask-CORS (Cross-origin requests)

### Frontend
- React 18
- Axios (API client)
- CSS3 (Animations & styling)

## Deployment

### GitHub Codespaces

This project is optimized for GitHub Codespaces:

1. Open in Codespaces
2. Run backend: `cd backend && python app.py`
3. Run frontend: `cd frontend && npm start`
4. Access via Codespaces URL

### Production Deployment

**Backend (e.g., Railway, Render):**
```bash
gunicorn app:app
```

**Frontend (e.g., Vercel, Netlify):**
```bash
npm run build
```

## Development

### Project Structure
```
manhwa-search-aggregator/
├── backend/
│   ├── app.py                  # Flask server
│   ├── scrapers/              # Web scrapers
│   │   ├── base_scraper.py
│   │   ├── mangadex.py
│   │   ├── webtoons.py
│   │   └── asura_scans.py
│   └── utils/
│       └── ranking.py         # Ranking algorithm
├── frontend/
│   ├── src/
│   │   ├── App.jsx           # Main component
│   │   ├── components/       # UI components
│   │   └── styles/          # CSS files
│   └── public/
└── README.md
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add new scrapers or improve existing ones
4. Submit a pull request

## Legal Notice

This tool is for educational purposes. Respect the terms of service of all platforms. Always use official platforms when available.

## License

MIT License - feel free to use and modify!

## Support

Found a bug? Have a feature request? Open an issue on GitHub!

---

Made with 🦈 and ❤️ for manhwa lovers
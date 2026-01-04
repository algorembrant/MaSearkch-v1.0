from flask import Flask, request, jsonify
from flask_cors import CORS
from scrapers import MangaDexScraper, WebtoonsScraper, AsuraScansScraper
from utils import rank_results
import concurrent.futures
from typing import List, Dict

app = Flask(__name__)
CORS(app)

# Initialize scrapers
scrapers = [
    MangaDexScraper(),
    WebtoonsScraper(),
    AsuraScansScraper()
]

def search_scraper(scraper, query: str) -> List[Dict]:
    """Search a single scraper and return results"""
    try:
        return scraper.search(query)
    except Exception as e:
        print(f"Error with {scraper.name}: {e}")
        return []

@app.route('/api/search', methods=['GET'])
def search():
    """Search endpoint - searches all platforms concurrently"""
    query = request.args.get('q', '').strip()
    
    if not query:
        return jsonify({'error': 'Query parameter "q" is required'}), 400
    
    # Search all scrapers concurrently for speed
    all_results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(scrapers)) as executor:
        future_to_scraper = {
            executor.submit(search_scraper, scraper, query): scraper 
            for scraper in scrapers
        }
        
        for future in concurrent.futures.as_completed(future_to_scraper):
            results = future.result()
            all_results.extend(results)
    
    # Rank results based on trust score and relevance
    ranked_results = rank_results(all_results, query)
    
    return jsonify({
        'query': query,
        'total_results': len(ranked_results),
        'results': ranked_results
    })

@app.route('/api/health', methods=['GET'])
def health():
    """Health check endpoint"""
    return jsonify({
        'status': 'healthy',
        'scrapers': [s.name for s in scrapers]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
from .base_scraper import BaseScraper
from typing import List, Dict
import requests

class MangaDexScraper(BaseScraper):
    """MangaDex API scraper - official API for manhwa/manga"""
    
    def __init__(self):
        super().__init__(
            name="MangaDex",
            base_url="https://api.mangadex.org",
            trust_score=9  # High trust - official platform
        )
    
    def search(self, query: str) -> List[Dict]:
        """Search MangaDex using their official API"""
        results = []
        
        try:
            # MangaDex API search endpoint
            api_url = f"{self.base_url}/manga"
            params = {
                'title': query,
                'limit': 10,
                'contentRating[]': ['safe', 'suggestive', 'erotica'],
                'includes[]': ['cover_art'],
                'order[relevance]': 'desc'
            }
            
            response = self.session.get(api_url, params=params, timeout=10)
            response.raise_for_status()
            data = response.json()
            
            for manga in data.get('data', []):
                attributes = manga.get('attributes', {})
                title = attributes.get('title', {})
                
                # Get English or first available title
                manga_title = title.get('en') or next(iter(title.values()), 'Unknown')
                
                # Get description
                description = attributes.get('description', {})
                desc_text = description.get('en') or next(iter(description.values()), '')
                
                # Get cover image
                cover_id = None
                for rel in manga.get('relationships', []):
                    if rel.get('type') == 'cover_art':
                        cover_id = rel.get('attributes', {}).get('fileName')
                        break
                
                thumbnail = ''
                if cover_id:
                    thumbnail = f"https://uploads.mangadex.org/covers/{manga['id']}/{cover_id}.256.jpg"
                
                results.append({
                    'title': manga_title,
                    'url': f"https://mangadex.org/title/{manga['id']}",
                    'thumbnail': thumbnail,
                    'source': self.name,
                    'description': desc_text[:200] + '...' if len(desc_text) > 200 else desc_text,
                    'trust_score': self.trust_score
                })
        
        except Exception as e:
            print(f"MangaDex search error: {e}")
        
        return results
from .base_scraper import BaseScraper
from typing import List, Dict

class AsuraScansScraper(BaseScraper):
    """AsuraScans scraper - popular scanlation site"""
    
    def __init__(self):
        super().__init__(
            name="AsuraScans",
            base_url="https://asuracomic.net",
            trust_score=7  # Medium-high trust - popular fan site
        )
    
    def search(self, query: str) -> List[Dict]:
        """Search AsuraScans"""
        results = []
        
        try:
            # AsuraScans search
            search_url = f"{self.base_url}/series"
            params = {
                's': query
            }
            
            response = self.session.get(search_url, params=params, timeout=10)
            response.raise_for_status()
            
            soup = self.get_soup(search_url + f"?s={query}")
            if not soup:
                return results
            
            # Find manga cards
            cards = soup.find_all('div', class_='bsx') or soup.find_all('div', class_='bs')
            
            for card in cards[:10]:
                try:
                    link_tag = card.find('a')
                    if not link_tag:
                        continue
                    
                    url = link_tag.get('href', '')
                    
                    title_tag = card.find('div', class_='tt') or card.find('h2')
                    title = title_tag.get_text(strip=True) if title_tag else 'Unknown'
                    
                    img_tag = card.find('img')
                    thumbnail = img_tag.get('src', '') or img_tag.get('data-src', '')
                    
                    # Get description if available
                    desc_tag = card.find('div', class_='excerpt')
                    description = desc_tag.get_text(strip=True) if desc_tag else ''
                    
                    results.append({
                        'title': title,
                        'url': url,
                        'thumbnail': thumbnail,
                        'source': self.name,
                        'description': description[:200] + '...' if len(description) > 200 else description,
                        'trust_score': self.trust_score
                    })
                except Exception as e:
                    print(f"Error parsing AsuraScans card: {e}")
                    continue
        
        except Exception as e:
            print(f"AsuraScans search error: {e}")
        
        return results
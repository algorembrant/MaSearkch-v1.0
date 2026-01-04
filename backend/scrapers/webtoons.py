from .base_scraper import BaseScraper
from typing import List, Dict
import requests

class WebtoonsScraper(BaseScraper):
    """Webtoons official platform scraper"""
    
    def __init__(self):
        super().__init__(
            name="Webtoons",
            base_url="https://www.webtoons.com",
            trust_score=10  # Highest trust - official platform
        )
    
    def search(self, query: str) -> List[Dict]:
        """Search Webtoons using their search API"""
        results = []
        
        try:
            # Webtoons search API
            search_url = f"{self.base_url}/en/search"
            params = {
                'keyword': query
            }
            
            response = self.session.get(search_url, params=params, timeout=10)
            response.raise_for_status()
            
            soup = self.get_soup(search_url + f"?keyword={query}")
            if not soup:
                return results
            
            # Find all search results
            cards = soup.find_all('li', class_='challenge_item') or soup.find_all('li', class_='card_item')
            
            for card in cards[:10]:
                try:
                    link_tag = card.find('a')
                    if not link_tag:
                        continue
                    
                    url = link_tag.get('href', '')
                    if not url.startswith('http'):
                        url = self.base_url + url
                    
                    title_tag = card.find('p', class_='subj') or card.find('div', class_='info')
                    title = title_tag.get_text(strip=True) if title_tag else 'Unknown'
                    
                    img_tag = card.find('img')
                    thumbnail = img_tag.get('src', '') if img_tag else ''
                    
                    desc_tag = card.find('p', class_='summary')
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
                    print(f"Error parsing Webtoons card: {e}")
                    continue
        
        except Exception as e:
            print(f"Webtoons search error: {e}")
        
        return results
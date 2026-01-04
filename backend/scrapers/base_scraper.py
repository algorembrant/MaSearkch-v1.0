from abc import ABC, abstractmethod
from typing import List, Dict
import requests
from bs4 import BeautifulSoup

class BaseScraper(ABC):
    """Base class for all manga/manhwa scrapers"""
    
    def __init__(self, name: str, base_url: str, trust_score: int):
        self.name = name
        self.base_url = base_url
        self.trust_score = trust_score  # 1-10, higher = more trusted
        self.session = requests.Session()
        self.session.headers.update({
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        })
    
    @abstractmethod
    def search(self, query: str) -> List[Dict]:
        """
        Search for manhwa by query
        Returns list of dicts with keys: title, url, thumbnail, source, description
        """
        pass
    
    def get_soup(self, url: str) -> BeautifulSoup:
        """Helper method to get BeautifulSoup object"""
        try:
            response = self.session.get(url, timeout=10)
            response.raise_for_status()
            return BeautifulSoup(response.content, 'lxml')
        except Exception as e:
            print(f"Error fetching {url}: {e}")
            return None
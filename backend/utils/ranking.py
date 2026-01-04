from typing import List, Dict

def rank_results(results: List[Dict], query: str) -> List[Dict]:
    """
    Rank search results based on:
    1. Trust score of the source (primary factor)
    2. Title relevance to query (secondary factor)
    """
    
    def calculate_relevance(result: Dict, query: str) -> float:
        """Calculate how relevant a result is to the query"""
        title = result.get('title', '').lower()
        query_lower = query.lower()
        
        # Exact match
        if query_lower == title:
            return 10.0
        
        # Title starts with query
        if title.startswith(query_lower):
            return 8.0
        
        # Query is in title
        if query_lower in title:
            return 6.0
        
        # Check word matches
        query_words = set(query_lower.split())
        title_words = set(title.split())
        matches = len(query_words.intersection(title_words))
        
        if matches > 0:
            return 4.0 + (matches * 0.5)
        
        return 1.0
    
    # Calculate ranking score for each result
    for result in results:
        trust_score = result.get('trust_score', 5)
        relevance = calculate_relevance(result, query)
        
        # Trust score is weighted more heavily (70% trust, 30% relevance)
        result['ranking_score'] = (trust_score * 0.7) + (relevance * 0.3)
    
    # Sort by ranking score (highest first)
    ranked_results = sorted(results, key=lambda x: x.get('ranking_score', 0), reverse=True)
    
    return ranked_results
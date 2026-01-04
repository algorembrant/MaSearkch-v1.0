import React, { useState } from 'react';
import axios from 'axios';
import SearchBar from './components/SearchBar';
import ManhwaCard from './components/ManhwaCard';
import PixelShark from './components/PixelShark';

function App() {
  const [results, setResults] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);
  const [searched, setSearched] = useState(false);

  const handleSearch = async (query) => {
    setLoading(true);
    setError(null);
    setSearched(true);

    try {
      const response = await axios.get(`/api/search?q=${encodeURIComponent(query)}`);
      setResults(response.data.results || []);
    } catch (err) {
      setError('Failed to fetch results. Please try again.');
      console.error('Search error:', err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app">
      <PixelShark />
      
      <div className="container">
        <header className="header">
          <h1 className="title">
            <span className="title-icon">🦈</span>
            Manhwa Search Aggregator
          </h1>
          <p className="subtitle">Search across multiple platforms instantly</p>
        </header>

        <SearchBar onSearch={handleSearch} loading={loading} />

        {loading && (
          <div className="loading-container">
            <div className="loading-text">Searching across platforms...</div>
          </div>
        )}

        {error && (
          <div className="error-message">
            <span className="error-icon">⚠️</span>
            {error}
          </div>
        )}

        {!loading && searched && results.length === 0 && (
          <div className="no-results">
            <span className="no-results-icon">📭</span>
            <p>No manhwas found. Try a different search term.</p>
          </div>
        )}

        {!loading && results.length > 0 && (
          <div className="results-container">
            <div className="results-header">
              <h2>Found {results.length} results</h2>
              <p className="results-note">Sorted by trust score and relevance</p>
            </div>
            <div className="results-grid">
              {results.map((manhwa, index) => (
                <ManhwaCard 
                  key={`${manhwa.source}-${manhwa.url}-${index}`} 
                  manhwa={manhwa} 
                  index={index}
                />
              ))}
            </div>
          </div>
        )}

        {!loading && !searched && (
          <div className="welcome-message">
            <div className="welcome-icon">🌊</div>
            <h2>Dive into the world of manhwas!</h2>
            <p>Search for your favorite manhwas across multiple platforms</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
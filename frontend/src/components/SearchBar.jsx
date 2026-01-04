import React, { useState } from 'react';

const SearchBar = ({ onSearch, loading }) => {
  const [query, setQuery] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    if (query.trim()) {
      onSearch(query.trim());
    }
  };

  return (
    <form className="search-bar" onSubmit={handleSubmit}>
      <div className="search-container">
        <input
          type="text"
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="Search for manhwas..."
          className="search-input"
          disabled={loading}
        />
        <button 
          type="submit" 
          className="search-button"
          disabled={loading || !query.trim()}
        >
          {loading ? (
            <span className="loading-spinner">⟳</span>
          ) : (
            '🔍'
          )}
        </button>
      </div>
    </form>
  );
};

export default SearchBar;
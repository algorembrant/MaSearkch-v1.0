import React from 'react';

const ManhwaCard = ({ manhwa, index }) => {
  const getTrustBadge = (score) => {
    if (score >= 9) return { text: 'Verified', color: '#10b981' };
    if (score >= 7) return { text: 'Trusted', color: '#3b82f6' };
    if (score >= 5) return { text: 'Popular', color: '#8b5cf6' };
    return { text: 'Community', color: '#6b7280' };
  };

  const badge = getTrustBadge(manhwa.trust_score);

  return (
    <div className="manhwa-card" style={{ animationDelay: `${index * 0.05}s` }}>
      <div className="card-rank">#{index + 1}</div>
      <div className="card-content">
        <div className="card-image-container">
          {manhwa.thumbnail ? (
            <img 
              src={manhwa.thumbnail} 
              alt={manhwa.title}
              className="card-image"
              onError={(e) => {
                e.target.style.display = 'none';
                e.target.parentElement.classList.add('no-image');
              }}
            />
          ) : (
            <div className="card-image-placeholder">📖</div>
          )}
          <div 
            className="trust-badge"
            style={{ backgroundColor: badge.color }}
          >
            {badge.text}
          </div>
        </div>
        
        <div className="card-details">
          <h3 className="card-title">{manhwa.title}</h3>
          <p className="card-source">
            <span className="source-icon">🌐</span>
            {manhwa.source}
          </p>
          {manhwa.description && (
            <p className="card-description">{manhwa.description}</p>
          )}
          <a 
            href={manhwa.url} 
            target="_blank" 
            rel="noopener noreferrer"
            className="card-link"
          >
            Read on {manhwa.source} →
          </a>
        </div>
      </div>
    </div>
  );
};

export default ManhwaCard;
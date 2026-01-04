import React, { useEffect, useState } from 'react';

const PixelShark = () => {
  const [position, setPosition] = useState({ x: 10, y: 50 });
  const [direction, setDirection] = useState(1);

  useEffect(() => {
    const moveShark = () => {
      setPosition(prev => {
        let newX = prev.x + (direction * 0.5);
        let newY = prev.y + Math.sin(newX * 0.05) * 0.3;

        if (newX > 100) {
          setDirection(-1);
          return { x: 100, y: newY };
        } else if (newX < -10) {
          setDirection(1);
          return { x: -10, y: newY };
        }

        return { x: newX, y: newY };
      });
    };

    const interval = setInterval(moveShark, 50);
    return () => clearInterval(interval);
  }, [direction]);

  return (
    <div 
      className="pixel-shark"
      style={{
        left: `${position.x}%`,
        top: `${position.y}%`,
        transform: `scaleX(${direction})`
      }}
    >
      <svg width="80" height="40" viewBox="0 0 80 40">
        {/* Shark body - pixel art style */}
        <rect x="20" y="15" width="8" height="8" fill="#4a90e2" />
        <rect x="28" y="15" width="8" height="8" fill="#5ba3f5" />
        <rect x="36" y="15" width="8" height="8" fill="#5ba3f5" />
        <rect x="44" y="15" width="8" height="8" fill="#4a90e2" />
        <rect x="52" y="15" width="8" height="8" fill="#3a7bc8" />
        
        {/* Shark fin */}
        <rect x="36" y="7" width="8" height="8" fill="#4a90e2" />
        <rect x="36" y="23" width="8" height="8" fill="#4a90e2" />
        
        {/* Shark tail */}
        <rect x="12" y="15" width="8" height="8" fill="#3a7bc8" />
        <rect x="4" y="11" width="8" height="8" fill="#3a7bc8" />
        <rect x="4" y="19" width="8" height="8" fill="#3a7bc8" />
        
        {/* Eye */}
        <rect x="52" y="17" width="4" height="4" fill="#ffffff" />
        <rect x="54" y="19" width="2" height="2" fill="#000000" />
        
        {/* Mouth */}
        <rect x="60" y="19" width="4" height="4" fill="#2a5a98" />
      </svg>
    </div>
  );
};

export default PixelShark;
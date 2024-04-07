import React from 'react';
import './styles/modal.css';

const PaintingItem = ({ painting, onClose }) => {
  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <button className="close-button" onClick={onClose}>X</button>
        <div className="painting-details">
          <h2>{painting.name}</h2>
          <p>Автор: {painting.author}</p>
          <p>Тип: {painting.type}</p>
          <p>Цена: {painting.price}$</p>
        </div>
        <img src={painting.photo} alt={painting.name} className="image" />
      </div>
    </div>
  );
};

export default PaintingItem;



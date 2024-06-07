import React from 'react';
import './styles/modal.css';
import trashIcon from './photos/trash-svgrepo-com.svg'
import { useState, useEffect } from 'react';
import {jwtDecode} from "jwt-decode";
import axios from "axios";

const PaintingItem = ({ painting, onClose }) => {
  const [isAdmin, setIsAdmin] = useState(false);
  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token){
      const decodedToken = jwtDecode(token);
      if (decodedToken.role === "admin"){
        setIsAdmin(true);
      }
    }
  }, [])

  const handleDelete = async () => {
    try {
      console.log({ "painting_photo": painting.photo })
      const response = await axios.delete('http://localhost:8000/paintings/delete', { data: { "painting_photo": painting.photo } });
      window.location.reload()
      console.log('Response:', response);
      // Дополнительные действия после успешного удаления
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="modal-overlay">
      <div className="modal-content">
        <button className="close-button" onClick={onClose}>X</button>
        <div className="painting-details">
          <h2>{painting.name}</h2>
          <p>Автор: {painting.author}</p>
          <p>Тип: {painting.type}</p>
          <p>Цена: {painting.price}$</p>
          {isAdmin && <a onClick={handleDelete}><img src={trashIcon} className='trash'/></a>}
        </div>
        <img src={painting.photo} alt={painting.name} className="image" />
      </div>
    </div>
  );
};

export default PaintingItem;



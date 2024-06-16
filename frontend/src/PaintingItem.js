import React from 'react';
import './styles/modal.css';
import trashIcon from './photos/trash-svgrepo-com.svg'
import updateIcon from './photos/arrow-change-svgrepo-com.svg'
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
      console.log({ "id": painting.id })
      const response = await axios.delete(`http://localhost:8000/paintings/delete/${painting.id}`);
      window.location.reload()
      console.log('Response:', response);
      // Дополнительные действия после успешного удаления
    } catch (error) {
      console.error('Error:', error);
    }
  };

  const handleUpdate = async () => {
    try {
      const newPrice = prompt("Enter new price:");
      if (newPrice) {
        const updated_data = {
          name: painting.name,
          photo: painting.photo,
          author: painting.author,
          price: parseInt(newPrice),
          type: painting.type
        };
        const response = await axios.put(`http://localhost:8000/paintings/update/${painting.id}`, updated_data);
        window.location.reload();
        console.log('Response:', response);
      }
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
          {isAdmin && (
            <div className="update_button">
              <a onClick={handleUpdate}>
                <img src={updateIcon} className="update" alt="Update Icon" />
              </a>
            </div>
          )}
          {isAdmin && (
            <a onClick={handleDelete}>
              <img src={trashIcon} className="trash" alt="Trash Icon" />
            </a>
          )}
        </div>
        <img src={painting.photo} alt={painting.name} className="image" />
      </div>
    </div>
  );
};

export default PaintingItem;



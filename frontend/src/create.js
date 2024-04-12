import React from "react";
import { useNavigate } from "react-router-dom";
import { useState, useEffect } from "react";
import axios from 'axios';
import './styles/auth.css';

const Createpage= () => {
    const navigate = useNavigate();
    const [paintingData, setPaintingData] = useState({
        name: "",
        photo: "",
        author: "",
        price: "",
        type: "",
    });

    const handleInputChange = (event) => {
        const { name, value } = event.target;
        setPaintingData((prevState) => ({
          ...prevState,
          [name]: value,
        }));
      };
    const handleSubmit = async (event) => {
    
        event.preventDefault();
        try {
            const response = await axios.post("http://localhost:8000/paintings/create", paintingData);
            console.log(paintingData);
            navigate("/");
          } catch (error) {
            console.error('Error:', error);
          }    
    };


    return (
        <div className="container">
        <div className="form-container">
            <h1 className="title">Add Page</h1>
            <form onSubmit={handleSubmit}>
            <div className="input-group">
                <label htmlFor="name">Name*</label>
                <input
                type="text"
                id="name"
                name="name"
                value={paintingData.name}
                onChange={handleInputChange}
                required
                />
            </div>
            <div className="input-group">
                <label htmlFor="photo">Photo*</label>
                <input
                type="text"
                id="photo"
                name="photo"
                value={paintingData.photo}
                onChange={handleInputChange}
                required
                />
            </div>
            <div className="input-group">
                <label htmlFor="author">Author*</label>
                <input
                type="text"
                id="author"
                name="author"
                value={paintingData.author}
                onChange={handleInputChange}
                required
                />
            </div>
            <div className="input-group">
                <label htmlFor="price">Price*</label>
                <input
                type="text"
                id="price"
                name="price"
                value={paintingData.price}
                onChange={handleInputChange}
                required
                />
            </div>
            <div className="input-group">
                <label htmlFor="type">Type*</label>
                <input
                type="text"
                id="type"
                name="type"
                value={paintingData.type}
                onChange={handleInputChange}
                required
                />
            </div>
            <button type="submit" className="primary-button">
                Add
            </button>
            </form>
            <div className="links">
            <span>
                Thanks for your investment! 
            </span>
            </div>
        </div>
        </div>
    );
};


export default Createpage
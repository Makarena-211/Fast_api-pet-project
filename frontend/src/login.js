import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import './styles/auth.css';
import axios from 'axios';
import {jwtDecode} from "jwt-decode";

const Loginpage = () => {
  const navigate = useNavigate();
  const [userData, setUserData] = useState({
    email: "",
    password: "",
  });

  const handleInputChange = (event) => {
    const { name, value } = event.target;
    setUserData((prevState) => ({
      ...prevState,
      [name]: value,
    }));
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    try {
      const response = await axios.post("http://localhost:8000/login/authenticate_user", userData);
      if (response.data){
        localStorage.setItem('token', response.data.token);
        const token = localStorage.getItem('token');
        const decodedToken = jwtDecode(token);
        console.log(decodedToken);
        navigate("/");
      } else{
        alert(response.data.message)
      }
      
    } catch (error) {
      console.error('Error:', error);
    }
  };


  return (
    <div className="container">
      <div className="form-container">
        <h1 className="title">Login Page</h1>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="email">Email Address*</label>
            <input
              type="email"
              id="email"
              name="email"
              value={userData.email}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="password">Password*</label>
            <input
              type="password"
              id="password"
              name="password"
              value={userData.password}
              onChange={handleInputChange}
              required
            />
          </div>
          <button type="submit" className="primary-button">
            LOGIN
          </button>
        </form>
        <div className="links">
          <span>
            Don't have an account? <a href="/auth">Create one</a>
          </span>
        </div>
      </div>
    </div>
  );
};

export default Loginpage;

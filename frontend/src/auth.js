import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import './styles/auth.css';
import axios from 'axios';

const Authpage = () => {
  const navigate = useNavigate();
  const [userData, setUserData] = useState({
    name: "",
    last_name: "",
    email: "",
    role: "",
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
      const response = await axios.post("http://localhost:8000/login/create_user", userData);
      // console.log('Response:', response.data);
      navigate("/");
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="container">
      <div className="form-container">
        <h1 className="title">Auth Page</h1>
        <form onSubmit={handleSubmit}>
          <div className="input-group">
            <label htmlFor="first-name">Name*</label>
            <input
              type="text"
              id="first-name"
              name="name"
              value={userData.name}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="last-name">Last Name*</label>
            <input
              type="text"
              id="last-name"
              name="last_name"
              value={userData.last_name}
              onChange={handleInputChange}
              required
            />
          </div>
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
            <label htmlFor="role">Role*</label>
            <input
              type="text"
              id="role"
              name="role"
              value={userData.role}
              onChange={handleInputChange}
              required
            />
          </div>
          <div className="input-group">
            <label htmlFor="password">Set A Password*</label>
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
            GET STARTED
          </button>
        </form>
        <div className="links">
          <span>
            Already have an account? <a href="/login">Log In</a>
          </span>
        </div>
      </div>
    </div>
  );
};

export default Authpage;

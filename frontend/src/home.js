import React, { useState, useEffect } from "react";
import './styles/header.css';
import settingsIcon from './photos/settings-svgrepo-com.svg';
import accountIcon from './photos/account-svgrepo-com.svg'
import logo from './photos/logo.jpg'
import PaintingItem from "./PaintingItem.js";
import {jwtDecode} from "jwt-decode";



function Homepage() {
    const [lastScrollTop, setLastScrollTop] = useState(0);
    const [scrollDirection, setScrollDirection] = useState("");
    const [paintings, setPaintings] = useState([]);
    const [selectedPainting, setSelectedPainting] = useState(null);
    const [isModalOpen, setIsModalOpen] = useState(false);


    useEffect(() => {
      window.addEventListener("scroll", handleScroll);
      return () => {
        window.removeEventListener("scroll", handleScroll);
      };
    }, []);
  
    
  
    useEffect(() => {
      async function fetchData() {
        try {
          const response = await fetch("http://localhost:8000/paintings");
          const data = await response.json();
          setPaintings(data);
        } catch (error) {
          console.error("Ошибка при загрузке данных:", error);
        }
      }
      fetchData();
    }, []);
  
    const handleScroll = () => {
      const currentScroll =
        window.pageYOffset || document.documentElement.scrollTop;
      if (currentScroll > lastScrollTop) {
        setScrollDirection("down");
      } else {
        setScrollDirection("up");
      }
      setLastScrollTop(currentScroll <= 0 ? 0 : currentScroll);
    };

    const openPaintingItem = (painting) => {
      setSelectedPainting(painting);
      setIsModalOpen(true); // Установка состояния для открытия модального окна
    };

    const closePaintingItem = () => {
      setSelectedPainting(null);
      setIsModalOpen(false); // Установка состояния для закрытия модального окна
    };


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
    

  
    return (
      <div className="base">
      <header className={`header ${scrollDirection === "down" ? "hide" : ""}`}>
        <h1>Paintlog</h1>
        <img src={logo} className="logo" />
        <nav>
          <ul className="nav-list">
            {isAdmin && <li><a href="/create">Add</a></li>}
            <li><a href="#">Ссылка 2</a></li>
            <li><a href="#">Ссылка 3</a></li>
            <li><img src={settingsIcon} className="icon" /></li>
            <li><a href="/auth"><img src={accountIcon} className="icon" /></a></li>
          </ul>
        </nav>
      </header>
      <div className="main">
        <div className="paintings-container">
          {paintings.map((painting) => (
            <div key={painting.id} className="painting-item" onClick={() => openPaintingItem(painting)}> 
              <div className="painting-details">
                <h2>{painting.name}</h2>
                <p>Автор: {painting.author}</p>
                <p>Тип: {painting.type}</p>
              </div>
              <img src={painting.photo} alt={painting.name} className="painting-image" />

              
            </div>
          ))}
        </div>  
      </div>
      {isModalOpen && selectedPainting && (
        <PaintingItem painting={selectedPainting} onClose={closePaintingItem} />
      )}
    </div>
    );
  }
  
  export default Homepage;
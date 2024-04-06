
import './styles/App.css';
import React from 'react';
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Createpage from './create';
import Homepage from './home';

function App() {
  return (
  <>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage/>}></Route>
        <Route path="/create" element={<Createpage/>}></Route>
      </Routes>
    </BrowserRouter>
  </>
  );
}

export default App;

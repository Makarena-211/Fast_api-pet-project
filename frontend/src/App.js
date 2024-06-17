
import './styles/App.css';
import React from 'react';
import {BrowserRouter, Route, Routes} from 'react-router-dom'
import Createpage from './create';
import Homepage from './home';
import Authpage from './auth';
import Loginpage from './login';

function App() {
  return (
  <>
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Homepage/>}></Route>
        <Route path="/auth" element={<Authpage/>}></Route>
        <Route path="/create" element={<Createpage/>}></Route>
        <Route path="/login" element={<Loginpage/>}></Route>
      </Routes>
    </BrowserRouter>
  </>
  );
}

export default App;

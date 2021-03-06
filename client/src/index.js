import React from 'react';
import ReactDOM from 'react-dom';
import './index.css';
import 'bootstrap/dist/css/bootstrap.min.css';
//import App from './App';
//import reportWebVitals from './reportWebVitals';
//import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";

import Homepage from './Components/Homepage.js';
//import DoctorDashboard from './Doctor_Dashboard';

ReactDOM.render(
  <React.StrictMode>
    <Homepage />
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
/*reportWebVitals();*/

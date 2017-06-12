// Libs
import React from 'react';
import { render } from 'react-dom';
import { Router, Route, hashHistory } from 'react-router';

// CSS 
import './css/style.css';

// Components
import App from './components/App';
import Home from './components/Home';

// Render
render((
  <Router history={hashHistory}>
    <Route path="/" component={Home} />
  </Router>
), document.getElementById('root'));
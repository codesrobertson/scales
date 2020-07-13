import React from 'react';
import { HashRouter, Route, Switch } from 'react-router-dom';
// import logo from './logo.svg';
import './App.css';
// import { Form, Button, FormGroup, FormControl, ControlLabel } from "react-bootstrap";
import Result from './Result.js';
import Home from './Home.js';

function App() {
  return (
    <HashRouter>
      <div>
        <Switch>
          <Route path="/" component={Home} exact />
          <Route path="/result" component={Result} exact />
        </Switch>
      </div>
    </HashRouter>  
  );
}

export default App;


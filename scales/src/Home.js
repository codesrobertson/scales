import Form from './Form.js';
import React from 'react';

const Home = (props) => {
  return (
    <div className="App">
      <div className="Site-title">Scales</div>
      <div className="Tagline">Uncover what the media we consume is consumed by</div>
      <h2>To analyze a news article, copy and paste its url into the form field below:</h2>
      <Form />
      <h5>This project is the product of a unique pocket of time, coming after the API designed by Politifact lost technical support, and before the Poynter Institute's Tech and Check Cooperative completes their work of uniting fact-checkers, developers, and data scientists to build an API for a database of checked facts.</h5>
      <p>Find out more about technology and fact-checking at:</p>
    </div>
  );
}

export default Home;

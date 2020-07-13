import React from 'react';

const Result = (props) => {
  return (
    <div className="Result">
      <div className="Site-title">Scales</div>
      <div className="Page-title">Your Analyzed Search Result</div>

      <h2>Is it news?</h2>
      <p>The machine learning model used by Scales thinks your search is: {}...</p>

      <h2>How much is bias?</h2>

      <div className="Percentages">{}</div>
      <h3>^Was this article's polarity score.</h3>
      <div className="Percentages">{}</div>
      <h3>^Was this article's subjectivity score.</h3>
    </div>
  );
}

export default Result;
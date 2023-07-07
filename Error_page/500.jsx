import React from 'react';
import './500ErrorPage.css';

const InternalServerErrorPage = () => {
  return (
    <div className="error-page-container">
      <div className="error-page-content">
        <h1 className="error-page-title">Oops! Internal Server Error</h1>
        <p className="error-page-message">We're sorry, but there was an internal server error.</p>
        <p className="error-page-suggestion">Please try one of the following options:</p>
        <ul className="error-page-options">
          <li className="error-page-option">Reload the page and try again</li>
          <li className="error-page-option">Go back to the previous page and try again later</li>
          <li className="error-page-option">Contact our support team and provide them with the error details</li>
        </ul>
      </div>
    </div>
  );
};

export default InternalServerErrorPage;

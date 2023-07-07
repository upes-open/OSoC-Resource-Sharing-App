import React from 'react';
import './404ErrorPage.css';

const NotFoundPage = () => {
  return (
    <div className="error-page-container">
      <div className="error-page-content">
        <h1 className="error-page-title">Oops! Page Not Found</h1>
        <p className="error-page-message">We're sorry, but the page you are looking for cannot be found.</p>
        <p className="error-page-suggestion">Please check the URL for any mistakes or try one of the following options:</p>
        <ul className="error-page-options">
          <li className="error-page-option"><a href="/">Go back to the homepage</a></li>
          <li className="error-page-option">Use the navigation menu to find the information you need</li>
          <li className="error-page-option">Contact our support team for further assistance</li>
        </ul>
      </div>
    </div>
  );
};

export default NotFoundPage;

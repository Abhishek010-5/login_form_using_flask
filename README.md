# Flask Authentication App

## Overview
This Flask application provides user authentication functionalities, including **signup**, **login**, and **password reset**, using **OTP (One-Time Password)** for verification. The application also includes validation for emails and passwords.

> **Note:** I am a beginner, and I have implemented things on my own. As a result, the code may look a bit messy or unorganized.

## Features
- **User Signup**
- **User Login**
- **Forgot Password**
- **OTP-based password reset**

## Technologies Used
- **Flask**
- **MongoDB**
- **hashlib**
- **Custom utilities and validations**

## Directory Structure
```plaintext
├── app.py
├── templates/
│   ├── index.html
│   ├── home.html
│   └── forget_password.html
├── utils/
│   ├── email_utils.py
│   ├── otp_utils.py
│   └── reset.py
├── validations/
│   └── validation_utils.py
└── database.py

Installation
Clone the repository:

bash
git clone <repository-url>
cd <repository-directory>
Set up a virtual environment and install dependencies:

bash
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
Set up your database: Ensure you have MongoDB set up and running. Update your database connection settings in database.py.

Configuration
Ensure you have the following environment variables set up:

FLASK_ENV: Set to development or production as needed.

MONGODB_URI: MongoDB connection string.

Usage
Run the application:

bash
python app.py
Access the application: Open your browser and navigate to http://127.0.0.1:5000/.

API Endpoints
User Signup
Endpoint: /signup

Method: POST

Description: Registers a new user.

Request Body:

json
{
  "fullname": "Your Name",
  "email": "your.email@example.com",
  "password": "yourpassword",
  "confirmPassword": "yourpassword"
}
User Login
Endpoint: /login

Method: POST

Description: Logs in an existing user.

Request Body:

json
{
  "email": "your.email@example.com",
  "password": "yourpassword"
}
Forgot Password
Endpoint: /forget_password

Method: PUT

Description: Sends an OTP or resets the password based on the action specified.

Request Body:

json
{
  "action": "send_otp",  // or "reset_password"
  "email": "your.email@example.com",
  "otp": "123456",      // required only for "reset_password"
  "password": "newpassword"  // required only for "reset_password"
}
Rendered Templates
Landing Page: / -> Redirects to /index

Home Page: /home

Forgot Password Page: /forgot_password

Validations
The app includes the following validations:

Email Validation

Password Validation

User Existence Validation

Utilities
Email Utils: Functions to send OTPs via email.

OTP Utils: Functions to generate and verify OTPs.

Validation Utils: Functions to validate emails and passwords.

Reset: Function to reset the user's password.

Error Handling
The application returns appropriate error messages with HTTP status codes for various error scenarios, such as invalid input or user not found.

Contributing
If you wish to contribute, please follow these guidelines:

Fork the repository.

Create a new branch (git checkout -b feature-branch).

Commit your changes (git commit -m 'Add new feature').

Push to the branch (git push origin feature-branch).

Open a Pull Request.

Future Improvements

Add more robust error handling.
Implement a front-end framework like React or Vue.
Add user profile management features.

Acknowledgments
Thanks to the open-source community for providing valuable resources and libraries.




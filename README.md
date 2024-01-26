# Flask API testing

This project demonstrates how to test a simple Flask API using the Pytest framework. 
The Flask API includes endpoints for creating and retrieving user information.
---
## Prerequisites

Make sure you have Python installed on your machine.

* Clone the repository
  > git clone https://github.com/ArtemPurtoian/Flask_API_testing.git

* Navigate to the project directory
  > cd Flask_API_testing

* Install dependencies
  > pip install -r requirements.txt
---
## Running the Flask API

* Execution of the tests doesn't require running the API (fixture used).
However, if you'd like to manually make some requests run the app

* > python app.py

  The API will be available at your localhost http://127.0.0.1:5000/


* Endpoints:
  > /api/welcome 
   
  > /api/greet/{name}
 
  > /api/users
---
## Running Tests

* To run locally
  > pytest
* To run in a Docker container
  > docker build -t flask_api .

  > docker run flask_api



The tests cover various scenarios, including creating a new user, 
getting a users list, handling duplicate usernames, checking the status codes, 
JSON format and others.
---
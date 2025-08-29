# BFHL REST API (Python)

This project is a simple REST API built with Python for the Bajaj Finserv Health Limited (BFHL) assignment.
It demonstrates REST API design principles like request handling, JSON responses, and structured API endpoints.

### Features
- RESTful API implementation in Python
- Handles POST and GET requests
- JSON input/output
- Easy to extend for future use cases

### Tech Stack
- Python 3.9+
- Flask / FastAPI (depending on your implementation – update accordingly)
- JSON for request/response format

### Installation & Setup
- Clone this repository:
  ```bash
  git clone https://github.com/YashasviAga/bfhl-rest-api-python.git
  cd bfhl-rest-api-python
- Create a virtual environment:
  ```bash
  python -m venv venv
  source venv/bin/activate    # On Linux/Mac
  venv\Scripts\activate       # On Windows
- Install dependencies:
  ```bash
  pip install -r requirements.txt
- Run the application:
  ```bash
  python app.py

The server should start at http://127.0.0.1:5000/ (default Flask) or http://127.0.0.1:8000/ (FastAPI).

### API Endpoints
1. Health Check
- Endpoint: /
- Method: GET
- Response:
  ```json
  { "status": "success", "message": "API is running" }

2. Process Data
- Endpoint: /bfhl
- Method: POST
- Request:
  ```json
  {
    "data": ["A", "B", "1", "2"]
  }
- Response:
  ```json
  {
    "is_success": true,
    "user_id": "yashasvi_agarwal_123",
    "email": "your_email@example.com",
    "roll_number": "XX123",
    "numbers": ["1", "2"],
    "alphabets": ["A", "B"],
    "highest_alphabet": ["B"]
  }

### Testing
You can test the API using:
- Postman
- curl
- Any frontend client consuming REST APIs
  Example:
  ```bash
    curl -X POST http://127.0.0.1:5000/bfhl \
    -H "Content-Type: application/json" \
    -d '{"data": ["A", "B", "1", "2"]}'

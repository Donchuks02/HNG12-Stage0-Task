# Basic Information Retrieval API

## Overview
This project is a public API built using Django REST Framework (DRF) that retrieves my basic information in JSON format. The API provides the following details:
- My email
- Current datetime as an ISO 8601 formatted timestamp
- This Project GitHub Repo URL

The API also includes Cross-Origin Resource Sharing (CORS) handling to allow secure requests from different origins.

## Features
- **Django REST Framework**: Implements a RESTful API.
- **Current Datetime**: Returns the server's current datetime in ISO 8601 format.
- **CORS Handling**: Configured to allow cross-origin requests.
- **Simple JSON Response**: Provides my basic information in a structured format.

## Technologies Used
- **Django** (v5.1.5)
- **Django REST Framework** (v3.15.2)
- **django-cors-headers** (v4.6.0)
- **Python** (v3.12)

## Installation
Follow these steps to set up the project locally:

### Prerequisites
Ensure you have the following installed:
- Python 3.12
- pip (Python package manager)
- Virtual environment (optional but recommended)

### Clone the Repository
```bash
git clone https://github.com/Donchuks02/HNG12-Stage0-Task.git
cd HNG12-Stage0-Task
```

### Create a Virtual Environment (Optional but Recommended)
```bash
python -m venv env
source env/bin/activate  # On Windows use: env\Scripts\activate
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

## Configuration
### Update `.env` File (Optional)
If using environment variables, create a `.env` file and set the following:
```
EMAIL=your_email@example.com
GITHUB_URL=https://github.com/YourUsername
```

### Apply Migrations
```bash
python manage.py migrate
```

## Running the Server
Start the development server:
```bash
python manage.py runserver
```

The API will be available at:
```
http://127.0.0.1:8000/
```

## API Endpoints
| Method | Endpoint       | Description                       |
|--------|---------------|-----------------------------------|
| GET    | '/'  | Returns email, datetime, and Project's GitHub URL |

### Sample Response
```json
{
    "email": "your_email@example.com",
    "current_datetime": "2025-01-29T12:34:56Z",
    "github_url": "https://github.com/YourUsername"
}
```

## CORS Configuration
This API supports CORS for cross-origin requests. The settings can be adjusted in `settings.py`:
```python
INSTALLED_APPS = [
    'corsheaders',
    ...
]

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',
    ...
]

CORS_ALLOW_ALL_ORIGINS = True  # Set to False and define allowed origins in production
```

## Deployment
To deploy the API, follow these general steps:
1. Choose a hosting provider (Render, DigitalOcean, AWS, etc.).
2. Set up a production database if needed.
3. Configure environment variables for production.
4. Apply migrations and start the production server.

## License
This project is licensed under the MIT License.

## Author
- **Chukwudi David Okoro** - [GitHub](https://github.com/Donchuks02)


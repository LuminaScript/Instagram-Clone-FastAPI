# Instagram-Clone-FastAPI: Backend in FastAPI & SQLAlchemy
## Intro.
**Prerequisites:** Before you begin, make sure you have FastAPI installed. You can install it using pip with the following command:
```bash
pip install fastapi

```

Activate Virtual Enviorment

```bash
source venv/bin/activate

```

Install Project Enviornemnt

```bash
pip install -r requirements.txt

```

Running the server
```bash
uvicorn main:app --reload
```

## Fucntionality

This project, built using a full-stack approach with Python FastAPI, SQLAlchemy, and SQLite, offers comprehensive functionality for uploading, managing, and posting content to Instagram.

### FastAPI Authentication User Module
This FastAPI module provides user authentication and token generation functionality for your application. Users can log in securely, and access tokens are generated for protected routes.

- **User Login**: Users can log in with their username and password via a POST request to /login. If credentials are valid, an access token is generated and returned.
- **Access Token Management**: Access tokens are created and validated using JWT. The **create_access_token** function generates tokens, and **get_current_user** verifies them.

### Database

### Routine


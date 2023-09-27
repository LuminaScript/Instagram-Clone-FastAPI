# Instagram-Clone-FastAPI: Backend in FastAPI & SQLAlchemy
## Prerequisites
Make sure you have FastAPI installe.
```bash
pip install fastapi

```
Create a Virtual Enviornment
```bash
python3 -m venv myenv
```
Activate Virtual Enviornment
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

### Database
This FastAPI project includes three database models: DbUser represents user data, DbPost captures Instagram-like posts, and DbComment stores comments on posts. 

- **Relationships Among Models**: DbUser for post creation, DbPost for multiple comments per post, supporting user auth, post creation, and comments.

### Routine
These routers collectively form the backbone of the Instagram clone application, providing essential functionalities related to user interactions, post management, and comments.

- **Comment Router (```/comment)**: This router is responsible for managing comments on posts. It allows users to retrieve all comments for a specific post (GET /all/{post_id}) and create new comments (POST /).
- **Post Router (/post)**: The Post router handles various aspects of posts in the application. It facilitates the creation of new posts with images, captions, and other details (POST /). Users can also retrieve all posts (GET /all) and upload images for their posts (POST /image). Additionally, it provides the functionality to delete a post by its ID (POST /delete/{id}).
- **User Router (/user)**: This router is responsible for user-related operations. It enables user registration by allowing users to create a new account with a username, email, and password (POST /).
  
### User Authentication
This FastAPI module provides user authentication and token generation functionality for your application. Users can log in securely, and access tokens are generated for protected routes.

- **User Login**: Users can log in with their username and password via a POST request to /login. If credentials are valid, an access token is generated and returned.
- **Access Token Management**: Access tokens are created and validated using JWT. The **create_access_token** function generates tokens, and **get_current_user** verifies them.










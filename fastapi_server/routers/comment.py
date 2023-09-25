from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from db import db_comment
from routers.schemas import UserAuth, CommentBase
from auth.oauth2 import get_current_user
from db.db_comment import get_all

router = APIRouter(
        prefix='/comment',
        tags=['comment']
)

@router.get('/all/{post_id}')
def comments(post_id: int, db: Session = Depends(get_db)):
        return get_all(db, post_id)

@router.post('')
def create(request: CommentBase, db: Session = Depends(get_db), current_user: UserAuth = Depends(get_current_user)):
        return db_comment.create(db, request)
        
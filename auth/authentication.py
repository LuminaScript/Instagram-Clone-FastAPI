from fastapi import APIR
from fastapi.param_fuctions import OAuth2PasswordRequest
from db.database import get_db
import sqlalchemy.orm
from sqlalchemy.orm.session import Session
from db.models import DbUser
router = APIRouter(
        tags=['authentication']
)

@router.post('/login')
def login(request: OAuth2PasswordRequest = Depends(), db: Session = Depends(get_db)):
        user = db.query(DbUser).filter(DbUser.username == request.username).first()
        if not user:
                raise HTTPException()
        
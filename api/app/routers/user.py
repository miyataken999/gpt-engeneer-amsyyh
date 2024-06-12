from fastapi import APIRouter, HTTPException
from sqlalchemy.orm import Session
from .models import User
from .schemas import UserSchema

router = APIRouter()

@router.post("/register")
async def register_user(user: UserSchema, db: Session):
    # check if username already exists
    existing_user = db.query(User).filter_by(username=user.username).first()
    if existing_user:
        raise HTTPException(status_code=400, detail="Username already exists")
    new_user = User(username=user.username, password=user.password, profile=user.profile, team_id=user.team_id)
    db.add(new_user)
    db.commit()
    return {"message": "User created successfully"}

@router.post("/login")
async def login_user(username: str, password: str, db: Session):
    user = db.query(User).filter_by(username=username, password=password).first()
    if not user:
        raise HTTPException(status_code=401, detail="Invalid username or password")
    return {"message": "Logged in successfully"}
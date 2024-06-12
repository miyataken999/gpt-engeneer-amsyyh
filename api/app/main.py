from fastapi import FastAPI
from routers import user, team

app = FastAPI()

app.include_router(user.router)
app.include_router(team.router)
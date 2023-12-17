from fastapi import FastAPI, Depends, status

from auth.jwt_bearer import JWTBearer
from config.config import initiate_database
from routes.user import router as UserRouter
from routes.candidate import router as CandidateRouter

app = FastAPI()

token_listener = JWTBearer()


@app.on_event("startup")
async def start_database():
    await initiate_database()


@app.get("/health")
async def root():
    return {"message": "Eleva Assignment Server Running."}


app.include_router(UserRouter, tags=["User"], prefix="/user")
app.include_router(CandidateRouter, tags=["Candidates"], prefix="/candidate", dependencies=[Depends(token_listener)], )

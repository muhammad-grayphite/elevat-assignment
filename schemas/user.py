from pydantic import BaseModel
from fastapi.security import HTTPBasicCredentials
from pydantic import EmailStr, UUID4


class UserSignIn(HTTPBasicCredentials):
    class Config:
        schema_extra = {
            "example": {
                "username": "admin@gmail.com",
                "password": "admin123"
            }
        }


class UserData(BaseModel):
    uuid: UUID4
    first_name: str
    last_name: str
    email: EmailStr

    class Config:
        schema_extra = {
            "example": {
                "uuid": "55edadce-56c5-4a94-9b7f-3bd3fe273743",
                "first_name": "Haziq",
                "last_name": "M",
                "email": "haziq@gmail.com",
            }
        }

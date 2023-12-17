from typing import Optional, Any, Literal, List
from beanie import Document
from pydantic import BaseModel, EmailStr, UUID4

CANDIDATE_QUERY_PARAM = {
    "first_name": (Optional[str], None),
    "last_name": (Optional[str], None),
    "email": (Optional[EmailStr], None),
    "uuid": (Optional[UUID4], None),
    "career_level": (Optional[str], None),
    "job_major": (Optional[str], None),
    "years_of_experience": (Optional[int], None),
    "degree_type": (Optional[str], None),
    "skills": (Optional[List[str]], None),
    "nationality": (Optional[str], None),
    "city": (Optional[str], None),
    "salary": (Optional[str], None),
    "gender": (Optional[str], None)
}


class Candidate(Document):
    first_name: str
    last_name: str
    email: EmailStr
    uuid: UUID4
    career_level: str
    job_major: str
    years_of_experience: int
    degree_type: str
    skills: List[str]
    nationality: str
    city: str
    salary: float
    gender: Literal['Male', 'Female', 'Not Specified']

    class Config:
        json_schema_extra = {
            "example": {
                "first_name": "Haziq",
                "last_name": "M",
                "email": "haziq@gmail.com",
                "uuid": "55edadce-56c5-4a94-9b7f-3bd3fe273713",
                "career_level": "Senior",
                "job_major": "Software Consultant",
                "years_of_experience": 7,
                "degree_type": "Computer Science",
                "skills": ["software", "coding"],
                "nationality": "Pakistan",
                "city": "Lahore",
                "salary": "60000",
                "gender": "Male"
            }
        }

    class Settings:
        name = "candidate"


class UpdateCandidateModel(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[EmailStr]
    career_level: Optional[str]
    job_major: Optional[str]
    years_of_experience: Optional[int]
    degree_type: Optional[str]
    skills: Optional[List[str]]
    nationality: Optional[str]
    city: Optional[str]
    salary: Optional[float]
    gender: Optional[Literal['Male', 'Female', 'Not Specified']]

    class Collection:
        name = "candidate"

    class Config:
        schema_extra = {
            "example": {
                "first_name": "Haziq",
                "last_name": "M",
                "email": "haziq@gmail.com",
                "uuid": "55edadce-56c5-4a94-9b7f-3bd3fe273713",
                "career_level": "Senior",
                "job_major": "Software Consultant",
                "years_of_experience": 7,
                "degree_type": "Computer Science",
                "skills": ["software", "coding"],
                "nationality": "Pakistan",
                "city": "Lahore",
                "salary": "60000",
                "gender": "Male"
            }
        }


class Response(BaseModel):
    status_code: int
    response_type: str
    description: str
    data: Optional[Any]

    class Config:
        schema_extra = {
            "example": {
                "status_code": 200,
                "response_type": "success",
                "description": "Operation successful",
                "data": "Sample data",
            }
        }

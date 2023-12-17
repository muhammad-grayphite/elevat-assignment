from fastapi import APIRouter, Body, Query, Depends
import pandas as pd
from fastapi.responses import StreamingResponse
import io
from pydantic import create_model
from database.database import *
from models.candidate import *

router = APIRouter()

query_model = create_model("Query", **CANDIDATE_QUERY_PARAM)


@router.get("/all-candidates/", response_description="Candidates retrieved", response_model=Response)
async def get_candidates(params: query_model = Depends()):
    if params:
        print(params)
        params = params.dict()
        params = {k: v for k, v in params.items() if v}
        print(params)
    else:
        params = {}
    candidates = await retrieve_candidates(params)
    return {
        "status_code": 200,
        "response_type": "success",
        "description": "Candidates data retrieved successfully",
        "data": candidates,
    }


@router.get("/generate-report")
async def generate_report():
    candidates = await retrieve_candidates({})
    df = pd.DataFrame(candidates)
    stream = io.StringIO()
    df.to_csv(stream, index=False)
    response = StreamingResponse(
        iter([stream.getvalue()]), media_type="text/csv"
    )
    response.headers["Content-Disposition"] = "attachment; filename=candidates.csv"
    return response


@router.get(
    "/{id}", response_description="Candidate data retrieved", response_model=Response
)
async def get_candidate_data(id: PydanticObjectId):
    candidate = await retrieve_candidate(id)
    if candidate:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Candidate data retrieved successfully",
            "data": candidate,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Candidate doesn't exist",
    }


@router.post(
    "/",
    response_description="Candidate data added into the database",
    response_model=Response,
)
async def add_candidate_data(candidate: Candidate = Body(...)):
    new_candidate = await add_candidate(candidate)
    return {
        "status_code": 201,
        "response_type": "success",
        "description": "Candidate created successfully.",
        "data": new_candidate,
    }


@router.delete("/{id}", response_description="Candidate data deleted from the database")
async def delete_candidate_data(id: PydanticObjectId):
    deleted_candidate = await delete_candidate(id)
    if deleted_candidate:
        return {
            "status_code": 204,
            "response_type": "success",
            "description": "Candidate deleted Successfully.",
            "data": False,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Candidate id doesn't exist",
        "data": False,
    }


@router.put("/{id}", response_model=Response)
async def update_candidate(id: PydanticObjectId, req: UpdateCandidateModel = Body(...)):
    updated_candidate = await update_candidate_data(id, req.dict())
    if updated_candidate:
        return {
            "status_code": 200,
            "response_type": "success",
            "description": "Candidate updated",
            "data": updated_candidate,
        }
    return {
        "status_code": 404,
        "response_type": "error",
        "description": "Candidate id doesn't exist",
        "data": False,
    }

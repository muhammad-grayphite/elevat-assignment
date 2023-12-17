from typing import List, Union
from beanie import PydanticObjectId
from models.user import User
from models.candidate import Candidate

user_collection = User
candidate_collection = Candidate


async def add_user(new_user: User) -> User:
    user = await new_user.create()
    return user


async def retrieve_candidates(q: dict) -> List[Candidate]:
    if q:
        candidates = []
        async for document in candidate_collection.find(q):
            candidates.append(document)
    else:
        candidates = await candidate_collection.all().to_list()
    return candidates


async def add_candidate(new_candidate: Candidate) -> Candidate:
    candidate = await new_candidate.create()
    return candidate


async def retrieve_candidate(id: PydanticObjectId) -> Candidate:
    candidate = await candidate_collection.get(id)
    if candidate:
        return candidate


async def delete_candidate(id: PydanticObjectId) -> bool:
    candidate = await candidate_collection.get(id)
    if candidate:
        await candidate.delete()
        return True


async def update_candidate_data(id: PydanticObjectId, data: dict) -> Union[bool, Candidate]:
    des_body = {k: v for k, v in data.items() if v is not None}
    update_query = {"$set": {field: value for field, value in des_body.items()}}
    candidate = await candidate_collection.get(id)
    if candidate:
        await candidate.update(update_query)
        return candidate
    return False

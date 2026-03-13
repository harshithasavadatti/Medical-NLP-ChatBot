from fastapi import APIRouter
from pydantic import BaseModel

from app.services.query_service import QueryService

router = APIRouter()

service = QueryService()


class QueryRequest(BaseModel):
    mrd_number: str
    query: str


@router.post("/query")
def query_patient(request: QueryRequest):

    result = service.query(
        mrd_number=request.mrd_number,
        question=request.query
    )

    return {
        "mrd_number": request.mrd_number,
        "answer": result["answer"],
        "confidence": result["confidence"]
    }
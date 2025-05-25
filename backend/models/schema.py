from pydantic import BaseModel

class QuestionRequest(BaseModel):
    question: str

class QueryResponse(BaseModel):
    sql: str | None = None
    data: list[dict] = []
    note: str | None = None
    error: str | None = None
    trace: str | None = None

from fastapi import APIRouter
from backend.models.schema import QuestionRequest, QueryResponse
from backend.mcp.registry import match_query
from backend.mcp.context import QueryContext
from backend.mcp.executor import execute_sql

router = APIRouter()

@router.post("/ask", response_model=QueryResponse)
async def ask_question(req: QuestionRequest):
    ctx = QueryContext(req.question)
    ctx.sql = match_query(ctx.question)

    if not ctx.sql:
        return QueryResponse(
            sql=None,
            note="這是 MCP demo 模式，目前僅支援：\n" + "\n".join(match_query.__globals__['MCP_REGISTRY'].keys())
        )

    data, error, trace = execute_sql(ctx.sql)
    return QueryResponse(sql=ctx.sql, data=data, error=error, trace=trace)

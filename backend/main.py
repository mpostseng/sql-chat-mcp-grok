from fastapi import FastAPI
from backend.mcp.router import router

app = FastAPI()
app.include_router(router)

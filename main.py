from fastapi import FastAPI
from app.mcp.router import router

app = FastAPI()
app.include_router(router)

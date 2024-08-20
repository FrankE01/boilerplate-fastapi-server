from fastapi import FastAPI
from api.v1.routers import app_router
from core.config import settings

app = FastAPI(title=settings.title, version=settings.version)

app.include_router(app_router)

@app.get("/", include_in_schema=False)
async def root():
    return {"message": "Connected to Vestir API", "status": "healty"}

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", reload=True, port=8000)
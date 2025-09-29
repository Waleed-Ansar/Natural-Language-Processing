from fastapi import APIRouter, FastAPI
from api import API


app = FastAPI()
router = APIRouter()
api = API()

router.include_router(api.router)

app.include_router(router, prefix='/book_ai')

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="localhost",
        port=8000,
        reload=True
    )
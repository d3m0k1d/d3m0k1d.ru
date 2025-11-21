import fastapi 
import uvicorn

#Import routes
from app.api.v1.posts import router as post_router

app = fastapi.FastAPI()

#Include routes
app.include_router(post_router)

 

from fastapi import APIRouter, Depends, HTTPException, Body
from sqlalchemy.ext.asyncio import AsyncSession
from pydantic import BaseModel
from app.schemas.posts import PostCreate, PostRead, PostRead
from app.db_engine import get_async_session
from app.models.posts import Post


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_posts():
    pass


@router.get("/{id}")
async def get_post(id: int):
    pass


@router.post("/")
async def create_post(
    post: PostCreate = Body(...), db: AsyncSession = Depends(get_async_session)
):
    new_post = Post(title=post.title, content=post.content, images=post.images)
    try:
        db.add(new_post)
        await db.commit()
        await db.refresh(new_post)
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

    return new_post


@router.put("/{id}")
async def update_post(id: int):
    pass


@router.delete("/{id}")
async def delete_post(id: int):
    pass

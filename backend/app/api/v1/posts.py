from typing import Optional
from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.ext.asyncio import AsyncSession
from app.schemas.posts import PostCreate, PostRead, PostRead
from app.db_engine import get_async_session
from app.models.posts import Post


router = APIRouter(
    prefix="/posts",
    tags=["posts"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def get_posts(
    page: int = Query(1, ge=1), db: AsyncSession = Depends(get_async_session)
):
    pass


@router.get("/{id}", response_model=PostRead)
async def get_post(id: int, db: AsyncSession = Depends(get_async_session)):
    post = await db.get(Post, id)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    else:
        return post


@router.post("/", response_model=PostRead)
async def create_post(
    title: str,
    content: str,
    images: Optional[str] = None,
    db: AsyncSession = Depends(get_async_session),
) -> Post:
    try:
        post = PostCreate(title=title, content=content, images=images)
    except Exception as e:
        raise HTTPException(status_code=423, detail=str("Validation error"))

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

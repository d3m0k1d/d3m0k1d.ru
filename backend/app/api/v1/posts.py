from fastapi import APIRouter

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
async def create_post():
    pass


@router.put("/{id}")
async def update_post(id: int):
    pass


@router.delete("/{id}")
async def delete_post(id: int):
    pass



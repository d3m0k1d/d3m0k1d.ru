from app.db_engine import init_db

from app.models.posts import Post


if __name__ == "__main__":
    import asyncio

    asyncio.run(init_db())

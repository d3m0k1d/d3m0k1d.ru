from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
import dotenv
import os

dotenv.load_dotenv()

PG_USER = dotenv.get_key(".env", "POSTGRES_USER")
PG_PASSWORD = dotenv.get_key(".env", "POSTGRES_PASSWORD")
PG_HOST = dotenv.get_key(".env", "POSTGRES_HOST")
PG_PORT = dotenv.get_key(".env", "POSTGRES_PORT")
PG_DB = dotenv.get_key(".env", "POSTGRES_DB")

DATABASE_URL = (
    f"postgresql+asyncpg://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_DB}"
)

engine = create_async_engine(
    DATABASE_URL,
    echo=False,
    future=True,
)

async_session_maker = async_sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False,
)


class Base(DeclarativeBase):
    pass


async def get_async_session():
    async with async_session_maker() as session:
        yield session


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

from pydantic import BaseModel, Field
from typing import Optional


class PostCreate(BaseModel):
    title: str = Field(min_length=3, max_length=150)
    content: str = Field(min_length=10)
    images: Optional[str] = Field(default=None)

    class Config:
        from_attributes = True


class PostRead(BaseModel):
    id: int = Field()
    title: str = Field(min_length=3, max_length=150)
    content: str = Field(min_length=10)
    images: str = Field()

    class Config:
        from_attributes = True


class PostUpdate(BaseModel):
    title: str = Field(min_length=3, max_length=150)
    content: str = Field(min_length=10)
    images: Optional[str] = Field(default=None)

    class Config:
        from_attributes = True

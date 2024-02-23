from pydantic import BaseModel, Field


class CreateBook(BaseModel):
    title: str = Field(max_length=30)
    price: float
    author: str = Field(max_length=30)
    rating: int = Field(gt=-0, lt=6)
    published: bool = Field(default=True)
    description: str

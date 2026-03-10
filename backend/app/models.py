from pydantic import BaseModel
from datetime import date
from typing import Optional

# Модель для контент-карточки
class Content(BaseModel):
    id: int
    title: str
    type: Optional[str] = None # фильм/сериал/игра/книга
    cover_url: Optional[str] = None
    release_year: Optional[int] = None
    author: Optional[str] = None
    rating: Optional[int] = None
    review_text: Optional[str] = None
    created_at: date

# Модель для создания контент-карточки
class ContentCreate(BaseModel):
    title: str
    type: Optional[str] = None
    cover_url: Optional[str] = None
    release_year: Optional[int] = None
    author: Optional[str] = None
    rating: Optional[int] = None
    review_text: Optional[str] = None
    created_at: Optional[date] = None

# Модель для ответа с контент-карточками
class ContentResponse(BaseModel):
    id: int
    title: str
    type: Optional[str] = None
    cover_url: Optional[str] = None
    release_year: Optional[int] = None
    author: Optional[str] = None
    rating: Optional[int] = None
    review_text: Optional[str] = None
    created_at: date
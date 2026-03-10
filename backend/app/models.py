from pydantic import BaseModel
from datetime import date, datetime
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
    created_at: datetime

# Модель для создания контент-карточки
class ContentCreate(BaseModel):
    title: str
    type: Optional[str] = None
    cover_url: Optional[str] = None
    release_year: Optional[int] = None
    author: Optional[str] = None
    rating: Optional[int] = None
    review_text: Optional[str] = None

# Модель для ответа с контент-карточками
class ContentResponse(BaseModel):
    id: int
    title: str
    type: str
    cover_url: str
    release_year: int
    author: str
    rating: int
    review_text: str
    created_at: datetime
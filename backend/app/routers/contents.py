from fastapi import APIRouter, HTTPException, Depends, Request
from datetime import date, datetime
import asyncpg
from ..database import get_db
from ..models import ContentCreate, ContentResponse

router = APIRouter(prefix="/contents", tags=["contents"])

@router.get("/", response_model=list[ContentResponse])
async def get_contents(
    conn: asyncpg.Connection = Depends(get_db)
):
    """Получить все контент-карточки"""

    rows = await conn.fetch("""
        SELECT * 
        FROM contents
        ORDER BY created_at DESC
    """)

    return [dict(row) for row in rows]

@router.post("/", response_model=ContentResponse, status_code=201)
async def create_content(
    content: ContentCreate,
    conn: asyncpg.Connection = Depends(get_db)
):
    """Создать новую контент-карточку"""

    # Проверяем, что обязательные поля заполнены
    if not content.title:
        raise HTTPException(status_code=400, detail="Title is required")

    row = await conn.fetchrow("""
        INSERT INTO contents (title, type, cover_url, release_year, author, rating, review_text, created_at)
        VALUES ($1, $2, $3, $4, $5, $6, $7, $8)
        RETURNING id, title, type, cover_url, release_year, author, rating, review_text, created_at
    """,
        content.title,
        content.type,
        content.cover_url,
        content.release_year,
        content.author,
        content.rating,
        content.review_text,
        datetime.now()
    )
    
    if not row:
        raise HTTPException(status_code=500, detail="Failed to create content")
    
    return dict(row)
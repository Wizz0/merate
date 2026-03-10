from fastapi import APIRouter, HTTPException, Depends, Request
from datetime import date
import asyncpg
from ..database import get_db
from ..models import ContentCreate, ContentResponse

router = APIRouter(prefix="/contents", tags=["contents"])

@router.get("/")
async def get_contents(
    conn: asyncpg.Connection = Depends(get_db)
):
    """Получить все контент-карточки"""

    rows = await conn.fetch("""
        SELECT * FROM contents
    """)

    return [dict(row) for row in rows]
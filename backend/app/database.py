import os
import asyncio
import asyncpg

DATABASE_URL = "postgresql://postgres:postgres@localhost:5433/merate"

async def get_db():
    """Подключение к базе данных"""
    conn = await asyncpg.connect(DATABASE_URL)
    try:
        yield conn
    finally:
        await conn.close()
import os
import asyncio
import asyncpg

async def get_db():
    """Подключение к базе данных"""
    
    conn = await asyncpg.connect(
        host="postgres",
        port=5432,
        user="postgres",
        password="postgres",
        database="merate"
    )
    try:
        print("✅ Подключено к базе данных")
        yield conn
    finally:
        await conn.close()
        print("❌ Соединение закрыто")
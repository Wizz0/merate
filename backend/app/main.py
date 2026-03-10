import os
from fastapi import FastAPI
from .routers import contents

app = FastAPI(
    title="MeRate API",
    description="Бэкенд для контейнернего приложения рецензий",
    version="0.1.0"
)

# Подключаем роутеры
app.include_router(contents.router)

@app.get("/")
async def root():
    return {"message": "MeRate API", "status": "running"}

@app.get("/health")
async def health():
    return {"status": "healthy"}
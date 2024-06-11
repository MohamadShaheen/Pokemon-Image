import os
from fastapi import FastAPI
from dotenv import load_dotenv
from routers import images_router

load_dotenv()

host = os.getenv('DATABASE_HOST')
port = os.getenv('SERVER_PORT')

app = FastAPI()

app.include_router(images_router.router, prefix='/images')


@app.get('/')
async def root():
    return f'Hey Mate! Go to {host}:{port}/docs. Do not use CMD, it is naive!'

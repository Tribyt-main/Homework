from fastapi import FastAPI
from FastAPI.routers import task, user

app = FastAPI()

@app.get('/')
async def welcome()->dict:
    return {'message': 'Welcome Taskmanager'}

app.include_router(task.router)
app.include_router(user.router)

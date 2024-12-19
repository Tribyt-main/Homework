from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

users = {1: 'Имя: Exemple, Возраст: 18'}


@app.get('/')
async def users_db() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def user_add(
        username: Annotated[str, Path(min_length=3,
                                      max_length=20,
                                      description='Enter your name',
                                      example='Alek')],
        age: Annotated[int, Path(ge=18,
                                 le=120,
                                 description='Enter your age')]
):
    user = max(users) + 1
    users[user] = f'Имя: {username}, Возраст: {age}'
    return f'User {username} is registered'


@app.put('/user/{user_id}/{username}/{age}')
async def user_update(
        user_id: int,
        username: Annotated[str, Path(min_length=3,
                                                    max_length=20,
                                                    description='Enter your name',
                                                    example='Alek')],
        age: Annotated[int, Path(ge=18,
                                 le=120,
                                 description='Enter your age')]
):
    users[user_id] = f'Имя: {username}, Возраст: {age}'
    return f'The user{user_id} is updated'


@app.delete('/user/{user_id}')
async def user_deleted(user_id: int):
    del users[user_id]
    return f'User{user_id} is deleted'

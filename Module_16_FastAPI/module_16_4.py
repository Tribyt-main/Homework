from fastapi import FastAPI, Path, HTTPException
from typing import Annotated
from pydantic import BaseModel

app = FastAPI()

# users = {1: 'Имя: Exemple, Возраст: 18'}
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def users_db():
    return users


@app.post('/users/{username}/{age}')
async def user_add(
        username: Annotated[str, Path(min_length=3,
                                      max_length=20,
                                      description='Enter your name',
                                      example='Alek')],
        age: Annotated[int, Path(ge=18,
                                 le=120,
                                 description='Enter your age')]
):
    user = User(id=len(users) + 1, username=username, age=age)
    users.append(user.model_dump())
    return user

@app.put('/users/{user_id}/{username}/{age}')
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
    try:
        for user in users:
            if user['id'] == user_id:
                user['username'] = username
                user['age'] = age
            return User(**user)
    except IndexError:
        raise HTTPException(status_code=404, detail='User not found')


@app.delete('/users/{user_id}')
async def user_deleted(user_id: int):
    for user in users:
        if user['id'] == user_id:
            del user
        return f'User{user_id} is deleted'

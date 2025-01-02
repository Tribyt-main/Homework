from typing import List
from fastapi import FastAPI, HTTPException, Path
from pydantic import BaseModel
from typing_extensions import Annotated


app = FastAPI()

users: List[dict] = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get('/users')
async def get_users() -> List[User]:
    return users

@app.post('/user/{username}/{age}')
async def post_user(
    username: Annotated[str, Path(title="Enter username", min_length=1, max_length=50)],
    age: Annotated[int, Path(title="Enter age", ge=0, le=120)]) -> User:

    new_id = users[-1]['id'] + 1 if users else 1
    new_user = User(id=new_id, username=username, age=age)
    users.append(new_user.model_dump())
    return new_user


@app.put('/user/{user_id}/{username}/{age}')
async def update_user(
    user_id: Annotated[int, Path(title="Enter User ID")],
    username: Annotated[str, Path(title="Enter username", min_length=1, max_length=50)],
    age: Annotated[int, Path(title="Enter age", ge=0, le=120)]) -> User:

    for user in users:
        if user['id'] == user_id:
            user['username'] = username
            user['age'] = age
            return User(**user)
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete('/user/{user_id}')
async def delete_user(user_id: Annotated[int, Path(title="Enter User ID")]) -> User:
    for index, user in enumerate(users):
        if user['id'] == user_id:
            removed_user = users.pop(index)
            return User(**removed_user)
    raise HTTPException(status_code=404, detail="User was not found")
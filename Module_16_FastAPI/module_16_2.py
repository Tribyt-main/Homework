from fastapi import FastAPI, Path
from typing import Annotated


app = FastAPI()

@app.get("/")
async def first_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_name}/{age}")
async def users_info(
        user_name: Annotated[str, Path(min_length=5,
                                     max_length=20,
                                     description="Enter your username")],
        age: Annotated[int, Path(ge=18,
                                  le=120,
                                  description="Enter your age")]):
    return {"Информация о пользователе": user_name, "Возраст": age}

@app.get("/user/{user_id}")
async def user_number(user_id: int = Path(ge=1, le=100, discription="Введите ID от 1 до 100", exemple="1")):
    return {"Вы вошли как пользователь №": user_id}

from fastapi import FastAPI


app = FastAPI()

@app.get("/")
async def first_page():
    return "Главная страница"

@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

@app.get("/user/{user_id}")
async def user_number(user_id: int):
    return {"Вы вошли как пользователь №": user_id}

@app.get("/user")
async def users_info(user_id: str, age: int):
    return {"Информация о пользователе": user_id, "Возраст": age}

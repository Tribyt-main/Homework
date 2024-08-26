class Database:
    def __init__(self):
        self.data = {}

    def add_user(self, username, password):
        self.data[username] = password


class User:
    """
    Класс пользователя содержащий атрибуты: логин, пароль
    """

    def __init__(self, username, password, password_confirm):
        self.username = username
        if password == password_confirm:
            self.password = password


if __name__ == '__main__':
    database = Database()
    while True:
        choice = int(input('Приветствую! Выберите действие: \n1 - Вход, \n2 - Регистрация\n'))
        if choice == 1:
            login = input('Введите логин: ')
            password = input('Введите пароль: ')
            if login in database.data:
                if password == database.data[login]:
                    print(f'Добро пожаловать, {login}!')
                    break
                else:
                    print('Введёт не верный пароль!')
            else:
                print('Пользователь не найден!\nЗарегистрируйтесь в системе!')
        if choice == 2:
            # Создание переменной внутри функции :=
            user = User(input('Введите логин: '), password := input('Введите пароль: '),
                        password_confirm := input('Подтвердите пароль: '))
            if len(password) < 8:
                print('Пароль не может быть короче 8 символов!')
                continue
            elif password.islower():
                print('В пароле должна быть хотя бы одна заглавная буква!')
                continue
            elif password.isdigit():
                print('Пароль должен иметь хотя бы одну цифру')
                continue
            elif password != password_confirm:
                print('Пароли не совпадают!')
                continue  # exit('Пароли не совпадают!')
            else:
                database.add_user(user.username, user.password)
        print(database.data)

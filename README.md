## Тестовое задание компании ООО Вижуал

Установка:

- Клонирование репозитория ```git clone git@github.com:Chinpakamon/vizual_test.git```
- Установка
  зависимостей ```cd vizual_test && python3 -m venv venv && source venv/bin/activate/ && pip install -r requirements.txt```
- Миграции и запуск сервера в файле
  backend ```python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver```

### Пример работы и выполнения запросов в Postman:

1) Создание нового пользователя (при создании устанавливать текущую дату регистрации).

Выполним POST запрос на адрес ```http://127.0.0.1:8000/user/auth/users/```:

```commandline
Запрос:
    {
        "email": "admin@mail.ru",
        "username": "chinpakamon",
        "password": "54321password12345"
    }

Ответ:
    {
        "id": 1,
        "email": "admin@mail.ru",
        "username": "chinpakamon",
        "registration_date": "2024-01-31T15:32:13.423147Z"
    }
```

2) Получение токена.

Для этого выполним ```POST``` запрос на адрес ```http://127.0.0.1:8000/user/auth/token/login/```:

```commandline
Запрос:
    {
        "password": "54321password12345",
        "email": "admin@mail.ru"
    }
Ответ:
    {
        "auth_token": "8f80eea8113e9826b02a4fa31c20fc97b02442d5"
    }
```

Для дальнейших операций и запросов понадобится полученный токен, то есть следующие запросы только для авторизованных
пользователей.
Токен нужно вставить в Headers:
```Authorization``` :  ```Token your_token_here```

3) Получение списка пользователей.

Для этого выполним ```GET``` запрос на адрес ```http://127.0.0.1:8000/user/auth/users/```:

```commandline
Ответ:
    [
        {
            "id": 1,
            "email": "admin@mail.ru",
            "username": "chinpakamon",
            "registration_date": "2024-01-31T15:32:13.423147Z",
            "password": "pbkdf2_sha256$720000$T55iS4MPkazcPZ6MJxU0so$dj42PwfsBvF5SE9W9uGz7ioqihiLMnkl6l+qIYJgGBU="
        },
        {
            "id": 2,
            "email": "meme@mail.ru",
            "username": "Kostya",
            "registration_date": "2024-01-31T14:38:30.563595Z",
            "password": "pbkdf2_sha256$720000$SuAjZ0YvuSJPoBlmQthimk$o8s4UHsxBIyEeJEvI8Clc3z/wwkjdaBDRCVnsJK876M="
        },
        ...
    ]
```

4) Получение отдельного пользователя.

Для этого нужно выполнить ```GET``` запрос на адрес ```http://127.0.0.1:8000/user/auth/users/1/```:

```commandline
Ответ:
    {
        "id": 1,
        "email": "admin@mail.ru",
        "username": "chinpakamon",
        "registration_date": "2024-01-31T15:32:13.423147Z",
        "password": "pbkdf2_sha256$720000$T55iS4MPkazcPZ6MJxU0so$dj42PwfsBvF5SE9W9uGz7ioqihiLMnkl6l+qIYJgGBU="
    }
```

5) Удаление пользователя.

Для удаления пользователя нужно сделать ```DELETE``` запрос на ```http://127.0.0.1:8000/user/auth/users/me/```. Удалить можно
только себя и с подтверждением пароля.
```commandline
Запрос:
    {
        "current_password" : "54321password12345"
    }
```

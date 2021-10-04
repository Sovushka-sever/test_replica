# Replica
учебное задание по созданию реплики базы данных

### Стек технологий:

- Ubuntu 20.04.1
- Python 3.7.6
- Django 3.2.7

### Установка

Для начала вам нужно склонировать репозиторий в требуемую директорию
```
git clone https://github.com/Sovushka-sever/my_library.git
```
- Настроить виртуальное окружение и его активировать:
```
source venv/bin/activate
```
- Перейти в корневую папку проекта и установите все требуемые пакеты:
```
pip install -r requirements.txt
```
- Создайте свой файл с настройками .env 
- Пример настроек:
```
DB_NAME=имя_базы
POSTGRES_USER=пользователь_postgres
POSTGRES_PASSWORD=пароль_пользователя
DB_HOST=db
DB_PORT=5432
DB_ENGINE=django.db.backends.postgresql

DB_NAME_REPLICA=имя_реплики_базы
POSTGRES_USER_REPLICA=пользователь_postgres
POSTGRES_PASSWORD_REPLICA=пароль_пользователя
DB_HOST_REPLICA=db_replica1
DB_PORT_REPLICA=5432
DB_ENGINE_REPLICA=django.db.backends.postgresql
```
- Создайте миграции:
```
python3 manage.py makemigrations
```
- Выполнить миграции:
```
python3 manage.py migrate
```
- Запустите сервер: 
```
python3 manage.py runserver
```

## Дополнительные команды

- Для создания суперюзера:
```
python3 manage.py createsuperuser
```

## Авторы
* **Sovushka-sever** 

### API Yatube
API, позволяющий работать с проектом Yatube. С помощью данного API можно с легкостью применять CRUD-операции к Yatube, давая возможность приложениям и сервисам взаимодействовать с проектом.

### Установка

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/turtlecowabunga/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
./venv/Scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python ./yatube_api/manage.py migrate
```

Запустить проект:

```
python ./yatube_api/manage.py runserver
```

### Документация

Всевозможные запросы к API описаны в документации, которая находится по адресу http://127.0.0.1:8000/redoc/. Примеры запросов представлены ниже.  
  
Получение публикаций:
```
GET /api/v1/posts/
```

Добавление комментария:
```
POST /api/v1/posts/{post_id}/comments/
```

Получить JWT-токен:
```
POST /api/v1/jwt/create/
```

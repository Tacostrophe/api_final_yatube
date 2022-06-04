# api_final
### Описание проекта:
Данный проект является ветвью проекта [Yatube](https://github.com/Tacostrophe/hw05_final) и позволяет при помощи API взаимодействовать с его объектами:
- публикациями;
- группами;
- комментариями;
- подписками.

### Примеры API запросов:
#### **GET** /api/v1/posts/
Получить список всех публикаций. При указании параметров limit и offset выдача должна работать с пагинацией.

###### Пример ответа:
```
{
  "count": 123,
  "next": ".../?offset=400&limit=100",
  "previous": ".../?offset=200&limit=100",
  "results": [
    {
      "id": {post_id},
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": {group_id}
    }
  ]
}
```
#### **PUT** /api/v1/posts/{post_id}/comments/{comment_id}/
Обновление комментария к публикации по id. Обновить комментарий может только автор комментария.
###### Пример запроса:
```
{
  "text": "string"
}
```
###### Пример ответа:
```
{
  "id": {comment_id},
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": {post_id}
}
```
#### **POST** /api/v1/follow/
Подписка пользователя от имени которого сделан запрос на пользователя переданного в теле запроса. Анонимные запросы запрещены.
###### Пример запроса:
```
{
  "following": "string"
}
```
###### Пример ответа:
```
{
  "user": "string",
  "following": "string"
}
```
### Как запустить проект:

Клонировать репозиторий:

```
git clone https://github.com/Tacostrophe/api_final_yatube.git
```

В репозитории создать и активировать виртуальное окружение:

```
python3 -m venv /path/to/new/virtual/environment
```
```
source /path/to/new/virtual/environment/bin/activate
```

Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

<sub>Всегда рад замечаниям и советам</sub>

<h1>Данный репозиторий содержит выполненное тестовое задание</h1>

Текст задания

<h1>User Stories </h1>

- Anonymous user can see navigation bar at the top of the page <br>
- Anonymous user can start the quiz by pressing a button<br>
- Anonymous user can see 3 random and unique questions with True/False answer<br>
- After the submission, the anonymous user can see a page with the following statistics<br>
        ○ How many correct answers did he get<br>
        ○ A message showing if he passed or failed the quiz<br>
- Superuser can see a link “Create question”, in the navigation bar<br>
- Superuser can create quiz questions in a custom form, that has fields Question, Correct <br>
answer (True/False)
- Superuser can access an Admin Panel to manage questions and review submissions<br>
    (CRUD: create, read, update, delete abilities).

Bonus features

- Superuser can click a button “Random question” below the custom form, to prefill fields
- Question and Correct answer with a data fetched from Quiz API service
https://opentdb.com/api_config.php
Application is containerized using Docker/docker-compose


## Установка

1. Клонируем репозиторий с гитхаба

    ```bash
    git clone git@github.com:way2thesky/quiz_app.git
    ```

2. Устанавливаем docker и docker-compose

3. Запускаем докер контейнеры и проект
   1. ```bash
       docker-compose build
      ```
   2. ```bash
       docker-compose up
      ```
4. Выполняем миграцию базы данных
     ```bash
        docker-compose run django_web /usr/local/bin/python manage.py migrate
    ```



5. Создаем администратора для django
    ```bash
        docker-compose run django_web /usr/local/bin/python manage.py createsuperuser
    ```    


## Использование

Приложение запущенно и доступно на порту 8001

### Функционал для администратора системы

Функционал для администратора системы полностью реализован на админке django.

1. переходим на url http://127.0.0.1:8001/admin
2. авторизуемся под созданным нами администратором
3. создаем, меняем удаляем опросники, вопросы в них и варианты ответов.
 
4. переходим на url http://127.0.0.1:8001/create_quiz/ на данном url Админ может создавать, рандомные опросы.



## База данных

База данных в проекте используется postgres
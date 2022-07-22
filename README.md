Порядок установки Клонировать репозиторий к себе, установить и активировать виртуальное окружение:

python -m venv venv venv\Scripts\activate.bat git clone https://github.com/duzz23/Questions_test.git перейти в папку проекта, установить зависимости:

cd sending pip install -r requirements.txt запустить и применить миграции:

python manage.py makemigrations 

python manage.py migrate 

Запустить проект:

python manage.py runserver

Данный приложение реализован на Django CMS 

Имя: admin Пароль: admin

Программ опросник
Включает в себя: 

User_register - приложение регистрации пользователя 

(Вариант 1)
Answer - приложение опросник 

(Вариант 2 django rest API )
question - приложение опросник 
url
http://127.0.0.1:8000/question/
http://127.0.0.1:8000/answer/


<img width="1280" alt="Снимок экрана 2022-07-20 в 17 06 17" src="https://user-images.githubusercontent.com/19858001/180005831-4dce75cb-363b-40dd-bc87-05a5f5c2067a.png">
<img width="1280" alt="Снимок экрана 2022-07-20 в 17 06 15" src="https://user-images.githubusercontent.com/19858001/180005844-427fd9d6-8e62-4bac-90c6-89d4d16a2890.png">
<img width="1280" alt="Снимок экрана 2022-07-20 в 17 06 10" src="https://user-images.githubusercontent.com/19858001/180005973-3235b90b-ae7a-4634-ba36-f0707e71f41c.png">
<img width="1280" alt="Снимок экрана 2022-07-20 в 17 06 47" src="https://user-images.githubusercontent.com/19858001/180005981-e6733271-7fd3-4fa1-98c7-76b6be4af35b.png">
<img width="1280" alt="Снимок экрана 2022-07-20 в 17 06 25" src="https://user-images.githubusercontent.com/19858001/180006028-89c3e7fe-c626-41cb-9d0d-33088e3e8f20.png">

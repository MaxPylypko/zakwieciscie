# "Zakwieciscie" польська онлайн-крамниця квітів

## Хто підтримує проект та вносить вклад у проект

🔘 **Підтримка та вклад:**
Проект підтримується та розробляється командою ентузіастів Django.

🔘 **Перелік учасників команди:**

- Пилипко Максим/Pylypko Maksym - лідер команди (Teamlead)
[GitHub](https://github.com/MaxPylypko) [Figma](https://www.figma.com/@7683301f_66d3_4)

- Гончаров Єгор/Honcharov Yehor - розробник (Full-Stack Developer)
[GitHub](https://github.com/YehorHoncharov) [Figma](https://www.figma.com/@d4a8c8c6_69dd_4)

- Киприч Таїсія/Kyprych Taisiia - розробник (Full-Stack Developer)
[GitHub](https://github.com/Taisiia773) [Figma](https://www.figma.com/@taisiiakiprych)

## Що робить проект

🔘 **Назва проекту та короткий опис:**
"Zakwieciscie"- Цей проект представляє собою інтернет-магазин різноманітних товарів (в основному квітів), де користувачі можуть їх переглядати, замовляти та купувати. Магазин надає зручний інтерфейс для користувачів, а також адміністративну панель для управління товарами, замовленнями та користувачами.

🔘 **Інтерактивна демоверсія проекту:**
[Демо версія проекту](http://example.com/demo)

## Чому проект корисний

🔘 **Корисність проекту:**
Проект є корисним як для користувачів, так і для розробників-початківців, оскільки він надає всі необхідні інструменти для створення повноцінного вебсайту. Для початківців це чудова можливість вивчити основи роботи з Django та здобути практичні навички.

## Як користувачі можуть приступити до роботи з вашим проектом

🔘 **Необхідні модулі:**
- Django
- 
Короткий опис кожного модуля:
- **Django:** основний фреймворк для розробки вебдодатків на Python.

🔘 **Інструкція по запуску проекту локально:**
1. Клонуйте репозиторій: `git clone [https://github.com/yourusername/yourproject.git`
2. Перейдіть в директорію проекту: `cd yourproject`
3. Встановіть віртуальне середовище: `python -m venv venv`
4. Активуйте віртуальне середовище: `source venv/bin/activate`
5. Встановіть необхідні залежності: `pip install -r requirements.txt`
6. Зробіть міграції бази даних: `python manage.py migrate`
7. Запустіть сервер: `python manage.py runserver`

🔘 **Інструкція по запуску проекту на PythonAnywhere:**
1. Зареєструйтеся на [PythonAnywhere](https://www.pythonanywhere.com/).
2. Створіть новий вебдодаток і виберіть Django.
3. Завантажте ваш проект на сервер.
4. Встановіть необхідні модулі: `pip install -r requirements.txt`
5. Налаштуйте базу даних та статичні файли відповідно до документації PythonAnywhere.
6. Запустіть міграції бази даних: `python manage.py migrate`
7. Перезапустіть вебдодаток.

## Як користувач може отримати допомогу по вашому проекту

🔘 **Структура проекту:**
- **Основні застосунки:**
  - zakwieciscie/ - головний проект Django
  - authorize/ - додаток для управління користувачами та автентифікації
  - catalog/ - додаток з товарами (каталог)
  - contacts/ - додаток з контактами замовників

🔘 **Приклад створення головного додатку:**
```shell
python manage.py startapp main
```

```python
# main/views.py
from django.shortcuts import render

def home(request):
    return render(request, 'main/home.html')
```

**Зображення:**
![Створення головного додатку](https://example.com/image.jpg)

🔘 **Створення додатку сторінки (Blueprint):**
```python
# main/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
]
```

**Зображення:**
![Створення Blueprint](https://example.com/image2.jpg)

🔘 **Налаштування Blueprint у файлі urls:**
```python
# project/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]
```

**Зображення:**
![Налаштування Blueprint](https://example.com/image3.jpg)

🔘 **Опис файлів settings, mail_config, login_manager:**
```python
# project/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    # інші додатки
]

# mail_config.py
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.example.com'
EMAIL_PORT = 587

# login_manager.py
from django.contrib.auth import authenticate, login, logout
```

**Зображення:**
![Файли конфігурації](https://example.com/image4.jpg)

🔘 **Шаблони HTML:**
```html
<!-- main/templates/main/home.html -->
<!DOCTYPE html>
<html>
<head>
    <title>Home</title>
</head>
<body>
    <h1>Welcome to the Home Page</h1>
</body>
</html>
```

**Зображення:**
![Шаблони HTML](https://example.com/image5.jpg)

🔘 **Приклад views.py з коментарями:**
```python
# main/views.py
from django.shortcuts import render

# Головна сторінка
def home(request):
    return render(request, 'main/home.html')
```

**Зображення:**
![Views.py](https://example.com/image6.jpg)

🔘 **Приклад models.py з коментарями:**
```python
# blog/models.py
from django.db import models

# Модель статті блогу
class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()

    def __str__(self):
        return self.title
```

**Зображення:**
![Models.py](https://example.com/image7.jpg)

🔘 **Опис міграцій:**
```shell
python manage.py makemigrations
python manage.py migrate
```

**Зображення:**
![Міграції](https://example.com/image8.jpg)

🔘 **Опис бази даних:**
SQLite3 - легка та зручна база даних для розробки. ID виконує роль первинного ключа у таблицях бази даних, забезпечуючи унікальність кожного запису.

🔘 **Опис файлів javascript:**
```javascript
// main/static/main/script.js
function showMessage() {
    alert("Hello, World!");
}
```

**Зображення:**
![Javascript](https://example.com/image9.jpg)

## Висновок по роботі над проектом

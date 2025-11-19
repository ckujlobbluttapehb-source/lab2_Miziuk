# Лабораторная работа №2
## Создание Web-страницы с текстом
Создадим директорию lab2, и с помощью команды ```py -m django startproject firstwebpage``` создадим проект firstwebpage

Перейдем в новую директорию и выполним команду ```python manage.py startapp app_name```, где app_name – это имя подключаемого приложения. 
## Добавление приложения flatpages
Для добавления приложения откроем файл settings.py, найдем кортеж INSTALLED_APPS и добавим в коец элемента строку 'flatpages'

<img width="378" height="205" alt="image" src="https://github.com/user-attachments/assets/debb7b4b-d3cc-4644-bdcd-8b4acd351502" />

Импортируем views нашего приложения и создаем новый адрес в файле urls.py

<img width="420" height="186" alt="image" src="https://github.com/user-attachments/assets/4b817d55-8e84-4d22-afd9-4d85323f5c49" />

Для того, чтобы в будущем при обращении генерировался ответ, необходимо создать функцию home в файле views.py в директории flatpages.

<img width="457" height="129" alt="image" src="https://github.com/user-attachments/assets/a65872a0-1e48-4e6b-b69e-1dace4ff3c55" />

Теперь запускаем работу сервера, переходим на страницу и убеждаемся, что вес сделали правильно.

<img width="462" height="106" alt="image" src="https://github.com/user-attachments/assets/f509d721-ed64-4586-88eb-34336400bf09" />

## Задание
При переходе по ссылке http://127.0.0.1:8000/hello/ возвращается тот же самый текст, это делается корректировкой файла views.py

<img width="443" height="99" alt="image" src="https://github.com/user-attachments/assets/500b7dfe-c53a-4df5-8e08-4408fbd12674" />

Убран тип выводимого текста из файла views.py, когда не указываем content_type, Django автоматически ставит text/html; charset=utf-8, что правильно для веб-страниц

## HTML-шаблоны
Создаем папку templates в директории flatpages. Затем, в папке templates создаем файл index.html со следующим кодом:
```
<!DOCTYPE html>
<html>
    <head>
        <title>Привет, Мир!</title>
    </head>
    <body>
        <h1>Привет, Мир!</h1>
        <h2>Это учебный сайт, с его помощью будут изучены технологии 
            python/django, html/css.</h2>
        <h3>Как видите, здесь используются заголовки различных 
            уровней.</h3>
        <p>Здесь есть маркированный список:</p>
        <h4>
		<ul>
            <li>Элемент 1;</li>
            <li>элемент 2;</li>
            <li>элемент 3;</li>
            <li>последний элемент.</li>
        </ul>
		</h4>
        <p>И нумерованный список:</p>
        <h4>
		<ol>
            <li>Элемент 1;</li>
            <li>элемент 2;</li>
            <li>элемент 3;</li>
            <li>последний элемент.</li>
        </ol>
		</h4>
        <p>И даже таблица:</p>
        <table style="border: none">
            <thead>
                <tr>
                    <th>Столбик 1</th>
                    <th>Столбик 2</th>
                    <th>Столбик 3</th>
                    <th>Столбик 4</th>
                </tr>
            </thead>
            <tr>
                <td>Строка 1 Столбец 1</td>
                <td>Строка 1 Столбец 2</td>
                <td>Строка 1 Столбец 3</td>
                <td>Строка 1 Столбец 4</td>
            </tr>
            <tr>
                <td>Строка 2 Столбец 1</td>
                <td>Строка 2 Столбец 2</td>
                <td>Строка 2 Столбец 3</td>
                <td>Строка 2 Столбец 4</td>
            </tr>
            <tr>
                <td>Строка 3 Столбец 1</td>
                <td>Строка 3 Столбец 2</td>
                <td>Строка 3 Столбец 3</td>
                <td>Строка 3 Столбец 4</td>
            </tr>
			            <tr>
                <td>Строка 4 Столбец 1</td>
                <td>Строка 4 Столбец 2</td>
                <td>Строка 4 Столбец 3</td>
                <td>Строка 4 Столбец 4</td>
            </tr>
            <tr>
                <td>Строка 5 Столбец 1</td>
                <td>Строка 5 Столбец 2</td>
                <td>Строка 5 Столбец 3</td>
                <td>Строка 5 Столбец 4</td>
            </tr>
        </table>
    </body>
</html>
```

Добавляем операции импортирования в flatpages\views.py

```
from django.shortcuts import render
from django import template
```

И изменяем функцию-представление home:

```
def home(request):
    return render(request, 'templates/index.html')
```

А также для того, чтобы файл index.html был найден в директории templates, необходимо в файле settings.py изменить поле DIRS кортеже TEMPLATES. Поле DIRS должно содержать адрес директории, в которой располагается файл index.html: ```'DIRS': [os.path.join(BASE_DIR, 'flatpages/templates')]```

Шаблон запущен:

<img width="1237" height="753" alt="image" src="https://github.com/user-attachments/assets/c0cbbf99-7fab-4761-a684-b32fbf4c7ca4" />

## Задание 
Полностью обновленный код с добавленными 2 строками и столбцами, границами таблицы и заголовками списков:

```
<!DOCTYPE html>
<html>
<head>
    <title>Привет, Мир!</title>
</head>
<body>
    <h1>Привет, Мир!</h1>
    <h2>Это учебный сайт, с его помощью будут изучены технологии python/django, html/css.</h2>
    <h3>Как видите, здесь используются заголовки различных уровней.</h3>
    
    <h4>Здесь есть маркированный список:</h4>
    <ul>
        <li>Элемент 1;</li>
        <li>элемент 2;</li>
        <li>элемент 3;</li>
        <li>последний элемент.</li>
    </ul>

    <h4>И нумерованный список:</h4>
    <ol>
        <li>Элемент 1;</li>
        <li>элемент 2;</li>
        <li>элемент 3;</li>
        <li>последний элемент.</li>
    </ol>

    <h4>И даже таблица:</h4>
    <table border="1" style="border-collapse: collapse; width: 100%;">
        <thead>
            <tr>
                <th>Столбик 1</th>
                <th>Столбик 2</th>
                <th>Столбик 3</th>
                <th>Столбик 4</th>
                <th>Столбик 5</th>
                <th>Столбик 6</th>
            </tr>
        </thead>
        <tr>
            <td>Строка 1 Столбец 1</td>
            <td>Строка 1 Столбец 2</td>
            <td>Строка 1 Столбец 3</td>
            <td>Строка 1 Столбец 4</td>
            <td>Строка 1 Столбец 5</td>
            <td>Строка 1 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 2 Столбец 1</td>
            <td>Строка 2 Столбец 2</td>
            <td>Строка 2 Столбец 3</td>
            <td>Строка 2 Столбец 4</td>
            <td>Строка 2 Столбец 5</td>
            <td>Строка 2 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 3 Столбец 1</td>
            <td>Строка 3 Столбец 2</td>
            <td>Строка 3 Столбец 3</td>
            <td>Строка 3 Столбец 4</td>
            <td>Строка 3 Столбец 5</td>
            <td>Строка 3 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 4 Столбец 1</td>
            <td>Строка 4 Столбец 2</td>
            <td>Строка 4 Столбец 3</td>
            <td>Строка 4 Столбец 4</td>
            <td>Строка 4 Столбец 5</td>
            <td>Строка 4 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 5 Столбец 1</td>
            <td>Строка 5 Столбец 2</td>
            <td>Строка 5 Столбец 3</td>
            <td>Строка 5 Столбец 4</td>
            <td>Строка 5 Столбец 5</td>
            <td>Строка 5 Столбец 6</td>
        </tr>
        <!-- ДОБАВЛЕННЫЕ СТРОКИ -->
        <tr>
            <td>Строка 6 Столбец 1</td>
            <td>Строка 6 Столбец 2</td>
            <td>Строка 6 Столбец 3</td>
            <td>Строка 6 Столбец 4</td>
            <td>Строка 6 Столбец 5</td>
            <td>Строка 6 Столбец 6</td>
        </tr>
        <tr>
            <td>Строка 7 Столбец 1</td>
            <td>Строка 7 Столбец 2</td>
            <td>Строка 7 Столбец 3</td>
            <td>Строка 7 Столбец 4</td>
            <td>Строка 7 Столбец 5</td>
            <td>Строка 7 Столбец 6</td>
        </tr>
    </table>
</body>
</html>
```

Также создаем идентичный шаблон под названием static_handler.html

## Настройка обработки статичных файлов для Django

Создадим папку static в директории flatpages, а в ней файл index.css с кодом:

```
body {
    background: #1abc9c; 
    font-family: Tahoma, Arial, sans-serif; 
    color: #333;
}
table {
    border-collapse: collapse;
}
p, h4 {
    font-size: 20px; 
    margin-bottom: 0;
}
h4 {
    font-size: 14px; 
}
ul, ol {
    margin: 0;
}
table tr td {
    padding: 5px;
}
table {
	width: 100%;
}

img {
	height: 30px;
	width: auto;
}

```

После этого в файл страницы static_handler.html во внутрь тега <head> вставим тег подключения css-скрипта:

```
<link rel="stylesheet" href="/static/index.css">
```
Так же добавим картинку: 

```
<body>
    <img src="https://via.placeholder.com/150x30/3498db/ffffff?text=Logo" alt="Logo">
    <!-- остальной код без изменений -->
</body>
```

В flatpages/views.py добавим новую функцию:

```
def static_handler(request):
    return render(request, 'static_handler.html')
```

Итого:

✅ Зеленый фон

✅ Картинка высотой 30px

✅ Шрифт с засечками для h1

✅ Таблица на 100% ширины

✅ Границы у таблицы

<img width="1911" height="890" alt="image" src="https://github.com/user-attachments/assets/ea887d4f-25c8-4cf6-8992-a043aa9eb71c" />

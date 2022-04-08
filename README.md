# Export-Write-CSV

Удобный скрипт для экспортирования и импортирования CSV-данных.  

С его помощью можно:

- быстро занести данные в БД для дальнейшей с ними работы;
- скачать имеющиеся данные в файл с расширением **csv**, структурированный по столбцам.  

<details>  
    <summary> Структура </summary>

```cmd
+---table_management
|   |   db.sqlite3
|   |   manage.py
|   +---static
|   |   \---data  <-- Директория для таблиц
|   |           README.md
|   +---table
|   |   |   admin.py
|   |   |   apps.py
|   |   |   management.py  <-- Ручное
|   |   |   models.py
|   |   |   urls.py
|   |   |   views.py
|   |   |   __init__.py
|   |   +---management
|   |   |   |   __init__.py
|   |   |   +---commands
|   |   |   |   |   load_data_csv.py  <-- Для импорта данных в БД через py manage.py load_data_csv
|   |   |   |   |   _private.py
|   |   |   |   |   __init__.py
|   +---table_management
|   |   |   asgi.py
|   |   |   settings.py
|   |   |   urls.py
|   |   |   wsgi.py
|   |   |   __init__.py
|   \---templates
|           base.html
\---venv
```
    
</details>

**Важно** помнить, что для корректной записи/чтения данных надо указыать те поля, которые заданы в самой исследуемой модели **Django** (даже поле **id**).

## Пример:

Для импортирования [(1)](#Import) и экспортирования [(2) ](#Export) данных БД **Student**
<a name="Import"/><a name="Export"/>

```py
class Student(models.Model):

    roll = models.CharField(max_length=200)
    sclass = models.CharField(max_length=200)
    fname = models.CharField(max_length=200)
    lname = models.CharField(max_length=200)
```

надо

## Import

в файле **views.py**, с 23 – 27 строку указать желаемые поля для импорта.

```py
writer.writerow(
    [
        ...
    ]
)
```

Само сохранение файла происходит в 4 этапа:

- активация виртуального окружения:

```py
source venv/Scripts/activate
```  

- переход к файлу **manage.py**:

```py
cd table_management/
```

- запуск сервера:

```py
py manage.py runserver
```

- переход по следующему пути в адресной строке:

```py
127.0.0.1:8000/main/
```

## Export

### Способ_1

в файле **load_data_csv.py**, с 26 – 30 строку указать [**ВСЕ**](#1) (1) поля для экспорта:

```py
created = model(
    ...
)
```

и затем вызывается данная команда через **manage.py**

```py
py manage.py load_data_csv
```

### Способ 2

Осуществить миграции, предварительно активировав виртуальное окружение:

```py
py manage.py migrate
```

запустить скрипт **management.py**, с 22 – 26 строку указать [**ВСЕ**](#1) (1) поля для экспорта:

```py
created = [
    (
        ...
    ) if i else 1 for i in reader
]
```

<a name="1"/>

## Примечение

При использовании [способа №1](#способ_1) важно учесть, БД создастся в текущей директории.
<a name="способ_1"/>
___

#### 1 – имеется в виду, что все поля, значения аргументов `null` и `blank` не `True`

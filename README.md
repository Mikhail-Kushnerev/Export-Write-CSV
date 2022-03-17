# Export-Write-CSV

Удобный скрипт для экспортирования и импортирования CSV-данных.  

С его помощью можно:

- быстро занести данные в БД для дальнейшей с ними работы;
- скачать имеющиеся данные в файл с расширением **csv**, структурированный по столбцам.  

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

в файле **views.py**, с 23 – 27 строку указать желаемые поля для импорта. Само сохранение файла происходит в 4 этапа:

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

### Способ 1

в файле **load_data_csv.py**, с 26 – 30 строку указать [**ВСЕ**](#1) (1) поля для экспорта.

```py
py manage.py load_data_csv
```

### Способ 2

Осуществить миграции, предварительно активировав виртуальное окружение:

```py
py manage.py migrate
```

запустить скрипт **management.py**, с 22 –  строку указать [**ВСЕ**](#1) (1) поля для экспорта. Также
<a name="1"/>
___

#### 1 – имеется в виду, что все поля, значения аргументов `null` и `blank` не `True`

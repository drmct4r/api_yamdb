### Проект «YaMDb» - База с отзывами и оценками пользователей на музыкальные произведения, книги и фильмы.

## Описание
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории: «Книги», «Фильмы», «Музыка». Список категорий (Category) может быть расширен администратором (например, можно добавить категорию «Изобразительное искусство» или «Ювелирка»). Сами произведения в YaMDb не хранятся, здесь нельзя посмотреть фильм или послушать музыку. В каждой категории есть произведения: книги, фильмы или музыка. Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все» и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Насекомые» и вторая сюита Баха. Произведению может быть присвоен жанр (Genre) из списка предустановленных (например, «Сказка», «Рок» или «Артхаус»). Новые жанры может создавать только администратор. Благодарные или возмущённые пользователи оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число). На одно произведение пользователь может оставить только один отзыв.

## Технологии
* Python 3.7 
* Django 3.2
* Django REST Framework 3.12

## Как запустить проект:
Клонировать репозиторий и перейти в него в командной строке: 
```
git clone https://github.com/drmct4r/api_yamdb.git
```
```
cd api_yamdb/
```
Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
```
. venv/Scripts/activate
```
Обновить пакетный установщик pip и установить зависимости из файла requirements.txt:
```
python -m pip install --upgrade pip
```
```
pip install -r requirements.txt
```
Выполнить миграции:
```
python manage.py migrate
```
Запустить проект:
```
python manage.py runserver
```

## Примеры запросов к API
http://127.0.0.1:8000/api/v1/auth/signup/

http://127.0.0.1:8000/api/v1/genres/

http://127.0.0.1:8000/api/v1/titles/{titles_id}/

http://127.0.0.1:8000/api/v1/users/{username}/

## Авторы
Студенты 52 когорты курса бэкенд-разработки Яндекс.Практикума 
Сивков Олег, Кондратьев Константин и Шарапов Вячеслав
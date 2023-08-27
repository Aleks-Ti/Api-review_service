# review_service

Api-review_service

## Проект Отзывы к произведениям

Проект review_service собирает отзывы пользователей на произведения.
Сами произведения в review_service не хранятся, здесь нельзя посмотреть
фильм или послушать музыку.

Произведения делятся на категории, такие как «Книги», «Фильмы», «Музыка».
Например, в категории «Книги» могут быть произведения «Винни-Пух и все-все-все»
и «Марсианские хроники», а в категории «Музыка» — песня «Давеча» группы «Жуки»
и вторая сюита Баха. Список категорий может быть расширен (например, можно добавить
категорию «Изобразительное искусство» или «Ювелирка»).

Произведению может быть присвоен жанр из списка предустановленных
(например, «Сказка», «Рок» или «Артхаус»).
Добавлять произведения, категории и жанры может только администратор.

Благодарные или возмущённые пользователи оставляют к произведениям
текстовые отзывы и ставят произведению оценку в диапазоне
от одного до десяти (целое число); из пользовательских оценок формируется
усреднённая оценка произведения — рейтинг (целое число).
На одно произведение пользователь может оставить только один отзыв.

Пользователи могут оставлять комментарии к отзывам.

Добавлять отзывы, комментарии и ставить оценки могут только
аутентифицированные пользователи.

### Как запустить проект

Клонировать репозиторий и перейти в него в командной строке:

```bash
git clone https://github.com/Aleks-Ti/Api-review_service.git
```

```bash
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```bash
python -3.11 -m venv env
```

```bash
source venv/Sourse/activate
```

```bash
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```bash
pip install -r requirements.txt
```

Выполнить миграции:

```bash
python manage.py migrate
```

Запустить проект:

```bash
python manage.py runserver
```

### Разработчики

### Team Leader - Александр Ткаченко

Разрабатывала системы:
    - система регистрации и аутентификации,
    - права доступа,
    - работа с токеном,
    - систему подтверждения через e-mail.

#### Developer - Ольга Ковешникова

Разрабатывала системы:
    - произведений,
    - категорий,
    - жанров;

#### Developer - Денис Лесиков

Разрабатывал системы:
    - отзыва,
    - комментариев,
    - рейтинг произведений.

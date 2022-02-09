# Книга рецептов

Сервис с рецептами.

## Использование Docker

### Настройка проекта
Загрузите проект в нужный репозиторий:

```bash
git clone https://github.com/VSBoiko/django_recipebook.git
```

Создайте `.env` файл в корне репозитория:

```bash
cp .env.dist .env
```

Внесите при необходимости корректировки в переменные окружения.

### Запуск проекта

В корне репозитория выполните команду:

```bash
docker-compose up --build
```

При первом запуске данный процесс может занять несколько минут.

### Остановка контейнеров

Для остановки контейнеров выполните команду:

```bash
docker-compose stop
```

Проект доступен по адресу http://127.0.0.1:8000
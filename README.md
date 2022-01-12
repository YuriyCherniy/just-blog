# Просто блог #
just-blog - блог с минималистичным дизайном и со всем необходимым инструментарием для комфортной работы.
* Простой дизайн не отвлекает читателя от контента
* Встроен WYSIWYG редактор Django CKEditor
* Реалезована удобная работа с изображениями(загрузка, удаление, вставка в текст) из административного интерфейса Django без сторонних файловых менеджеров
* Для коммуникации с пользователями имеется старая добрая гостевая комната
* Счетчик сообщений в гостевой с уведомлениями для администратор
* Система тегов для групировки контента по тематикам

## Запуск на локальном хосте ##
Клонируем репозиторий
```
git clone https://github.com/YuriyCherniy/just-blog.git
```
Переходим в корневую папку проекта
```
cd just-blog/
```
Создаём виртуальное окружение
```
python3 -m venv .venv
```
Активируем виртуальное окружение
```
source .venv/bin/activate
```
Устанавливаем зависимости
```
pip3 install -r requirements/dev.txt
```
Создаём файл для хранения переменных
```
touch .env
```
Помещаем в файл .env следующее содержимое
```
SECRET_KEY=django-insecure-vvk8k^sc_65!yym6jq#ija-3j)nnvup)d4a7w1442scx2gj=_d
DEBUG=True
POSTGRES_DB=blog_db
POSTGRES_USER=user_postgres
POSTGRES_USER_PASSWORD=0000
RECAPTCHA_PRIVATE_KEY=None
RECAPTCHA_PUBLIC_KEY=None
SECRET_ADMIN_URL=admin
SENTRY_DSN=None
```
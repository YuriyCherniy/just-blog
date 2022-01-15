# Просто блог #
just-blog - блог с минималистичным дизайном и со всем необходимым инструментарием для комфортной работы. Посмотреть как это выглядит можно здесь: [there-is-a-bug.ru](http://there-is-a-bug.ru/) и здесь: [vzglad-iz-pod-ochkov.ru](http://vzglad-iz-pod-ochkov.ru/)
* Простой дизайн не отвлекает читателя от контента
* Встроен WYSIWYG редактор Django CKEditor
* Реалезована удобная работа с изображениями(загрузка, удаление, вставка в текст) из административного интерфейса Django без сторонних файловых менеджеров
* Для коммуникации с пользователями имеется старая добрая гостевая комната
* Счетчик сообщений в гостевой с уведомлениями для администратор
* Система тегов для групировки контента по тематикам
* Система рекомендаций других постов блого

## Запуск на локальном хосте ##
* Клонируем репозиторий ```(выполнить в консоли)```
```
git clone https://github.com/YuriyCherniy/just-blog.git
```
* Переходим в корневую папку проекта ```(выполнить в консоли)```
```
cd just-blog/
```
* Создаём виртуальное окружение ```(выполнить в консоли)```
```
python3 -m venv .venv
```
* Активируем виртуальное окружение ```(выполнить в консоли)```
```
source .venv/bin/activate
```
* Устанавливаем зависимости ```(выполнить в консоли)```
```
pip3 install -r requirements/dev.txt
```
* Создаём файл для хранения переменных ```(выполнить в консоли)```
```
touch .env
```
* Помещаем в файл .env следующее содержимое
```
SECRET_KEY=django-insecure-vvk8k^sc_65!yym6jq#ija-3j)nnvup)d4a7w1442scx2gj=_d
DEBUG=True
POSTGRES_DB=<db_name>
POSTGRES_USER=<postgres_user_name>
POSTGRES_USER_PASSWORD=<db_password>
RECAPTCHA_PRIVATE_KEY=None
RECAPTCHA_PUBLIC_KEY=None
SECRET_ADMIN_URL=admin
SENTRY_DSN=None
```
**Внимание! Перед запуском приложения необходимо создать и настроить базу данных PostgrSQL. Затем внести соответствующие данные в переменные ```POSTGRES_DB```, ```POSTGRES_USER``` и ```POSTGRES_USER_PASSWORD``` содержащиеся в файле .env Также в текущей конфигурации отключена Google reCAPTCHA v3, поэтому в гостевой комнате будет невозможно оставить сообщение через форму. Для правильной работы reCAPTCHA необходимо указать значения для переменных ```RECAPTCHA_PRIVATE_KEY``` и ```RECAPTCHA_PUBLIC_KEY```. Получить значения можно здесь: [Google reCAPTCHA v3](https://www.google.com/recaptcha/about/).**

* В модуле [settings.py](https://github.com/YuriyCherniy/just-blog/blob/532b61e5a780c78792084b70e7a1aeee30d0bb16/just_blog/settings.py#L53) изменяем значение переменной содержащей разрешённые хосты
```
ALLOWED_HOSTS = ['*']
```
* Применяем миграции ```(выполнить в консоли)```
```
./manage.py migrate
```
* Создаём суперюзера ```(выполнить в консоли)```
```
./manage.py createsuperuser
```
* Запускаем локальный сервер ```(выполнить в консоли)```
```
./manage.py runserver
```
* Переходим по адресу: http://127.0.0.1:8000/

# summer_practice
проект для прохождения летней практики
## Как разместить на сервере
Связка:
Ubuntu 18.04.4 LTS + nginx + gunicorn + postgresql + django
Установка по шагам:<br>
После успешной установки операционной системы необходимо выполнить ряд команд.
Необходимо создать нового пользователя и дать ему необходимые разрешения<br>
username - имя пользователя
venv - название виртуального окружения<br>
Шаг 1: Обновляем и устанавливаем всё необходимое<br>
```
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install python3 python3-pip
pip3 install virtualenv
sudo apt-get install postgresql
sudo apt install nginx
```
Шаг 2: Установка и настройка проекта django
```
cd /home/username
git clone https://github.com/oleggys/summer_practice
virtualenv venv
source venv/bin/activate
pip install gunicorn
pip install -r summer_practice/requirements.txt
```
В папке summer_practice/summer_practice необъодимо создать файл .env,
пример содержания файла располагается в файле .env.example<br>
Шаг 3: настройка gunicorn<br>
Редактируем файл gunicorn.socket
```
sudo nano /etc/systemd/system/gunicorn.socket
```

Записать в файл gunicorn.socket:
```
[Unit]
Description=gunicorn socket

[Socket]
ListenStream=/run/gunicorn.sock

[Install]
WantedBy=sockets.target
```
Редактируем файл gunicorn.service
```
sudo nano /etc/systemd/system/gunicorn.service
```
Записать в файл:
```
[Unit]
Description=gunicorn daemon
Requires=gunicorn.socket
After=network.target

[Service]
User=username
Group=www-data
WorkingDirectory=/home/username/summer_practice
ExecStart=/home/username/venv/bin/gunicorn \
          --access-logfile - \
          --workers 5 \
          --bind unix:/run/gunicorn.sock \
          summer_practice.wsgi:application

[Install]
WantedBy=multi-user.target
```
Запускаем gunicorn:
```
sudo systemctl start gunicorn.socket
```
Шаг 4: Создание базы данных<br>
Чтобы использовать интерфейс postgresql
```
psql
CREATE DATABASE database_name;
CREATE USER database_username WITH PASSWORD 'database_userpassword';
GRANT ALL PRIVILEGES ON DATABASE database_name to database_username;
```
Шаг 5: Настройка nginx
Необходимо открыть конфигурационный файл
```
sudo nano /etc/nginx/sites-available/default
```
и записать в него
```
server {
    listen 80;
    server_name server_domain_or_IP;

    location = /favicon.ico { access_log off; log_not_found off; }

    location / {
        include proxy_params;
        proxy_pass http://unix:/run/gunicorn.sock;
    }
}
```
Проверить на наличие ошибок и перезапустить nginx
```
sudo nginx -t
sudo systemctl restart nginx
```
Готово!

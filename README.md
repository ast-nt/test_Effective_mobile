# Как запустить проект

необходим запущенный демон docker

`systemctl start docker` для систем с systemd

выполнить следущие команды

```
git clone https://github.com/ast-nt/test_Effective_mobile
cd test_Effective_mobile
docker compose up -d
```

# Как проверить результат работы проекта

`curl http://localhost:80`

Команда должна вернуть строку "Hello from Effective Mobile!"

# Схема работы проекта

Nginx и backend приложение запускаются в отдельных контейнерах. Из контейнера Nginx на хост проброшен 80 порт. Nginx проксирует запросы на порт 8080 backend-а и возвращает ответ клиенту. Backend реализован на python с помощью библиотеки http.server

Список использованных технологий
 - Linux
 - Docker, docker-compose
 - Nginx reverse proxy
 - Python, http.server
 
# Как запустить проект

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

Nginx проксирует запросы с 80 порта во внутреннюю подсеть docker на порт 8080. Внутренняя подсеть docker недоступна снаружи напрямую

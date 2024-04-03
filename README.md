## Предварительная настройка приложения перед запуском
1. Заполнить в config/settings почту (EMAIL_HOST_USER) и пароль (EMAIL_HOST_PASSWORD);
2. Выполнить в терминале команды:
- "python3 manage.py csu" (создать супер пользователя); 
- "python3 manage.py loaddata data.json" (загрузить в базу данных группу "модератор").

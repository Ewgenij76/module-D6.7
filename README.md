Добавьте подписки на рассылки о новых материалах в категориях:
страница должна быть доступна по адресу https://127.0.0.1:8000/subscriptions/;
должна быть создана модель Subscriber для хранения подписок пользователей;
при публикации новости все подписчики должны получить сообщение на почту со ссылкой на страницу для прочтения новости (используйте для этого сигнал post_save).
Реализуйте отправку списка статей на почту подписчиков категорий каждую неделю на основе той же модели Subscriber:
подключите приложение django_apscheduler;
добавьте команду запуска периодических задач;
настройте периодическую задачу отправки списка статей каждую пятницу в 18:00;
составьте сообщение со ссылками на статьи;
сообщение должно содержать только статьи, которые появились с момента предыдущей рассылки.

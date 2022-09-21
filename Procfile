web: gunicorn -b "0.0.0.0:$PORT" -w 3 score_card.wsgi
release: python manage.py migrate

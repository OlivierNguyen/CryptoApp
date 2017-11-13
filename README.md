# CryptoApp
Little app using Django && Coinbase API


# Some commands to run in local
---
- Install dependencies : `pip install -r requirements.txt`
- Run the app: `python manage.py runserver`
- Run tasks: `celery -A alerts beat` && `celery -A alerts worker -l info`

# bitnob_faq

This an API that allows users perform CRUD actions on FAQs. 

To test Repo;
  1. Clone Repo.
  2. Create a `local.py` file in the inner bitnob_faq(right before `settings.py`)
  3. Add a `SECRET_KEY`, `DEBUG = True` and a `DATABASE`
  4. Run `python manage.py makemigrations` and `python manage.py migrate`
  5. Finally,run python manage.py runserver

`/faq` is to see all vquestions and to add more
`faq/<int:pk>/` is to check a particular question created, where `pk` is an id integer
`search/<str:keyword>/` is to search  for questions, where keyword is a word or sentence

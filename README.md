 37 cd .\webapp\
  38 clear
  39 python manage.py runserver
  40 clear
  41 ls
  42 clear
  43 python manage.py makemigrations
  44 python manage.py makemigrations
  45 python manage.py sqlmigrate firstApp 0001
  46 python manage.py migrate
  47 python manage.py sqlmigrate firstApp 0001
  48 python manage.py migrate
  49 clear
  50 python manage.py runserver
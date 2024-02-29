Uruchamianie projektu

Wykonanie polecenia:
python -m venv venv

Uruchamiania wirualnej zmiennej środowiskowej (venv)

.\venv\Scripts\activate(cmd? or powershell?)
lub
source venv/Scripts/activate (w GITbashu)

Instalacja Django:

pip install django

Instalacja Pillow:

pip install Pillow

Opcjonalnie, jeżeli jest pusta baza to:

python manage.py migrate

oraz stworzenie superusera:

python manage.py createsuperuser

Urochomienie serwera

python manage.py runserver
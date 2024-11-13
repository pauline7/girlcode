1. git clone https://github.com/pauline7/girlcode.git
2. python3.13 -m venv ./girlcodeEnv
3. source girlcodeEnv/bin/activate
4. cd into project folder
5. pip3 install -r requirements.txt

   - If error Failed building wheel for psycopg2: pip install psycopg2-binary

6. Create .env file in girlcode folder, base of app, same level as settings.py and fill them with your own passwords and api keys
   SECRET_KEY=
   DATABASE_NAME=
   DATABASE_USER=
   DATABASE_PASSWORD=
   DATABASE_HOST=
   EMAIL_HOST_USER=
   EMAIL_HOST_PASSWORD=
   GOOGLE_CLIENT_ID=
   GOOGLE_CLIENT_SECRET=
   GEMINI_API=
7. python3 manage.py makemigrations
8. python3 manage.py migrate
9. python3 manage.py createsuperuser (that you can use to login to admin)
10. python3 manage.py runserver
11. View app at http://127.0.0.1:8000/

Blog

To run:
Note: May have to run cmd as an admin or run MINGW32 and use source venv/Scripts/activate
-cd into root Blog folder
-Activate virtual environment using 'venv/Scripts/activate'
-Start server using python3 manage.py runserver

To quit venv: deactivate

Log In via: localhost/admin/

heroku pg:psql -a protected-beyond-71115 < newdb.dump

pg_dump -Fc --no-acl --no-owner -h localhost -U myuser -d mydb -f mydb.dump

pg_dump -U postgres --format=c -W -F t blog_db > mydb4.dump

pg_dump -U --format=c --compress=9 r postgres blog_db > mydb4.dump

pg_dump --format=c blog_db > db_dump_file.dump

pg_dump -Fc --no-acl --no-owner -h localhost -U postgres -d blog_db -f mydb4.dump


git push heroku master


Stack overflow
pg_dump --no-owner -U postgres blog_db > mydb3.dump
pg_dump -f mydb2.dump -Fc --no-acl -no-owner -h localhost -U postgres --schema=public blog_db 
pg_dump -Fc --no-acl --no-owner -h localhost -U postgres blog_db > blog_db.psql



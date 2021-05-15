<<<<<<< HEAD
#!/bin/sh

if [ "$DATABASE" = "budget" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if ["$FLASK_ENV" = 'development']
then
  echo "Creating the database tables..."
  python manage.py create_db
  echo "Tables created"
fi

exec "$@"
=======
#!/bin/sh

if [ "$DATABASE" = "budget" ]
then
    echo "Waiting for postgres..."

    while ! nc -z $SQL_HOST $SQL_PORT; do
      sleep 0.1
    done

    echo "PostgreSQL started"
fi

if ["$FLASK_ENV" = 'development']
then
  echo "Creating the database tables..."
  python manage.py create_db
  echo "Tables created"
fi

exec "$@"
>>>>>>> 2f2aac69e53574dd2f16f760be8d7f556185e654

# Personal Budget Manager

## Track your expences and analyze your personal data

## Installation
1. Clone the repository to your local machine
2.  Change the enviorment variables values as you wish (username, passwords, etc.)
3. Create the containers using the command

    `docker-compose -f docker-compose.prod.yml up -d --build`
4. Create the dbatabase using the command

    `docker-compose -f docker-compose.prod.yml exec web python manage.py create_db`
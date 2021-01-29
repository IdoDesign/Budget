from project.models import User, Category, User, Transaction

for row in Transaction.get_by_user('62215d2232864736b1a9aa0be99e21d8'):
    print(row.description)
from flask.cli import FlaskGroup
from project import app, db
from project.common import populateData
cli = FlaskGroup(app)


@cli.command("create_db")
def create_db():
    db.drop_all()
    db.create_all()
    populateData.populateCategories()
    db.session.commit()

@cli.command("seed_db")
def seed_db():
    populateData.create_user()
    populateData.populateTransactions()
    db.session.commit()

if __name__ == "__main__":
    cli()

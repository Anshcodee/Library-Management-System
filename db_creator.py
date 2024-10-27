
from app import app, db
from models.models import Admin

def init_db():
    with app.app_context():
        db.create_all()  # This will create the tables for the models

        if not Admin.query.filter_by(username='admin').first():
            # Create a default admin account
            admin = Admin(username='admin', password='admin123')
            db.session.add(admin)
            db.session.commit()
            print("Default admin account created (username: 'admin', password: 'admin123')")
        else:
            print("Admin account already exists")

    print("Database created.")

if __name__ == "__main__":
    init_db()

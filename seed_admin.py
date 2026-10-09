from app.database import SessionLocal
from app.models.models import User
from app.auth.security import hash_password

db=SessionLocal()
try:
    if db.query(User).filter(User.username=="admin").first():
        print("Admin already exists")
    else:
        db.add(User(username="admin",email="admin@example.com",password_hash=hash_password("Admin@12345"),role="Admin",is_active=True))
        db.commit()
        print("Created admin: username=admin password=Admin@12345")
finally:
    db.close()

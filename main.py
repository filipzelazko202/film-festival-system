from database.db import Base, engine


def create_db():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_db()
    print("Baza danych działa")
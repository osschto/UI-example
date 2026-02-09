from sqlmodel import SQLModel, Session, create_engine

engine = create_engine("sqlite:///src/db/database.db",
                        pool_size=25,
                        max_overflow=25)

def create_db():
    SQLModel.metadata.create_all(engine)

def get_session():
    with Session(engine) as session:
        try:
            yield session
        finally:
            session.close()
from src.models import Base


class LogSystem(Base):

    __tablename__ = 'log_system'
    __table_args__ = {'autoload': True}

    def save(self, session):
        try:
            session.add(self)
            session.commit()
        except Exception as e:
            print("ERRO AQUI", str(e))
            session.rollback()
            print("Unable to save exceptions into log_system table.")


class Warranty(Base):
    __tablename__ = 'warranty'
    __table_args__ = {'autoload': True}

    @classmethod
    def get_warranty_id(cls, session):
        return session.query(cls).filter(cls.url.like('%{{cookiecutter.project_name}}%')).first().id

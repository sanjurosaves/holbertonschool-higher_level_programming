#!/usr/bin/python3
""" deletes all State objects a name containing letter a from the database """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    theas = session.query(State).filter(State.name.contains('a'))
    theas.delete(synchronize_session=False)
    session.commit()
    session.close()

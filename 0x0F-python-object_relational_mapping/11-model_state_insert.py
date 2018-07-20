#!/usr/bin/python3
""" adds the State object “Louisiana” to the database """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    newstate = State(name="Louisiana")
    session.add(newstate)
    session.commit()
    print(newstate.id)
    session.close()

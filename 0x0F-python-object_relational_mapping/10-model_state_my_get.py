#!/usr/bin/python3
""" prints the State object with name passed as argument from the database """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    match = session.query(State).filter(State.name == argv[4]).all()
    if len(match) is 0:
        print("Not found")
    else:
        for state in match:
            print("{}".format(state.id))
    session.close()

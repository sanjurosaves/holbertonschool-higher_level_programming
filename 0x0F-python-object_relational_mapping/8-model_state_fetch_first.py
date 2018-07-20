#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """
from sys import argv
from model_state import Base, State
from sqlalchemy import (create_engine)
from sqlalchemy.orm import Session


if __name__ == "__main__":
    i = 0
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))
    Base.metadata.create_all(engine)

    session = Session(engine)
    for state in session.query(State).order_by(State.id).all():
        if (i == 0):
            if state.name is not None:
                print("{}: {}".format(state.id, state.name))
            else:
                print();
        i = i + 1
    session.close()

#!/usr/bin/python3
"""
Lists all State objects containing the letter 'a' from hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL via SQLAlchemy
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query states containing 'a' in the name
    states_with_a = session.query(State).filter(State.name.like('%a%'))\
        .order_by(State.id).all()

    for state in states_with_a:
        print("{}: {}".format(state.id, state.name))

    session.close()

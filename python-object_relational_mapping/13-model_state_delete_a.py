#!/usr/bin/python3
"""
Deletes all State objects containing the letter 'a' from the
database hbtn_0e_6_usa.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            user, passwd, db_name
        ),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all states containing 'a' and delete them
    states_to_delete = session.query(State).filter(
        State.name.like('%a%')
    ).all()
    for state in states_to_delete:
        session.delete(state)

    session.commit()
    session.close()

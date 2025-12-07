#!/usr/bin/python3
"""
Print all City objects from the database hbtn_0e_14_usa
in the format: <state name>: (<city id>) <city name>
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(user, passwd, db_name),
        pool_pre_ping=True
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Fetch cities joined with states, ordered by city.id
    cities = session.query(City, State).join(State).order_by(City.id).all()

    for city, state in cities:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()

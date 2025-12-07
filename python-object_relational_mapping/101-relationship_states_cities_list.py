#!/usr/bin/python3
"""List all State objects and their City objects"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: {} <user> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    user, password, db = sys.argv[1], sys.argv[2], sys.argv[3]

    engine = create_engine(
        f"mysql+mysqldb://{user}:{password}@localhost:3306/{db}"
    )
    Session = sessionmaker(bind=engine)
    session = Session()

    # Yalnız bir query: bütün states və cities gətirilir
    states = session.query(State).order_by(State.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:  # cities relationship istifadə olunur
            print(f"\t{city.id}: {city.name}")

    session.close()

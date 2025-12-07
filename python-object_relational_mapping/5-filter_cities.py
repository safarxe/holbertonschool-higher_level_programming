#!/usr/bin/python3
"""
Displays all cities of a given state from the database
hbtn_0e_4_usa. SQL injection safe.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    # Connect to MySQL
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )
    cur = conn.cursor()

    # Safe query using JOIN and parameterized input
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s "
             "ORDER BY cities.id ASC")

    cur.execute(query, (state_name,))
    rows = cur.fetchall()

    # Print cities separated by comma
    print(", ".join([row[0] for row in rows]))

    cur.close()
    conn.close()

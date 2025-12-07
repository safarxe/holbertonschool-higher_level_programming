#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL server
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )
    cur = conn.cursor()

    # Execute query to get all states ordered by id
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()

    # Print results
    for row in rows:
        print(row)

    # Close cursor and connection
    cur.close()
    conn.close()

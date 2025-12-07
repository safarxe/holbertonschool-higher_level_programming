#!/usr/bin/python3
"""
Displays all values in the states table where name
matches the argument (case-sensitive).
"""

import sys
import MySQLdb

if __name__ == "__main__":
    user = sys.argv[1]
    passwd = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=db_name
    )
    cur = conn.cursor()

    query = ("SELECT * FROM states WHERE name = '{}' "
             "COLLATE utf8mb4_bin ORDER BY id ASC"
             ).format(state_name)

    cur.execute(query)
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()

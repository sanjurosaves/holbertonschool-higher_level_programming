#!/usr/bin/python3
""" lists all states from the database hbtn_0e_0_usa """


import MySQLdb
from sys import argv

if __name__ == "__main__":
    db = MySQLdb.connect(user=argv[1], passwd=argv[2], db=argv[3])
    cur = db.cursor()
    cur.execute("SELECT * from states ORDER BY states.id")
    states = cur.fetchall()
    for state in states:
        print(state)
    cur.close()
    db.close()

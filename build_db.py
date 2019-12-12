#!/usr/bin/env python

import csv
import os
import sys
from config import db, app
from models import Play

csv.field_size_limit(sys.maxsize)


def read_csv(filename):
    """File format: ID Name Age Species Location"""
    with open(f"{filename}.csv", "r") as f:
        content = csv.reader(f)
        print(content)
        next(content)
        complete_works = list(content)
    return complete_works



def build_db(filename):
    """
    Create a new database from CSV
    1. Delete the database file
    2. Create the database structure
    3. Populate the database
    """
    if os.path.exists(f"{filename}.db"):
        os.remove(f"{filename}.db")

    db.create_all()
    complete_works = read_csv(f"{filename}")
    for play in complete_works:
        the_play = Play(
            play_id=play[0],
            title=play[1],
            text=play[2],
        )
        db.session.add(the_play)
#    db.session.commit()
    db.create_all()


def main():
    """Main function"""
    build_db("complete_works")

if __name__ == '__main__':
   app.run()

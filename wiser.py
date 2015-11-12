# coding UTF-8

import sys
import wikiload
import database

argvs = sys.argv
db_path = "wiki1m.db"

def add_document(title, body, category):
    database.db_add_document(db_path, title, body, category)

def main(path):
    wikiload.load_wikipedia_dump(path)

if __name__ == "__main__":
    if(len(argvs) == 2):
        main(argvs[1])

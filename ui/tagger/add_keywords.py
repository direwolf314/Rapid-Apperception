#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
import pymongo
import sys

#TODO: add case sensitivity boolean to keyword

def print_usage_and_die():
    print 'Usage: %s input_file' % sys.argv[0]
    print '\tinput_file: An input file containing lines with space delineated: extension keyword tag'
    sys.exit(1)

def add_keywords():
    config_name = 'tagger.conf'

    config = ConfigParser.SafeConfigParser()
    config.read(config_name)

    # Set up the database connection
    db_name = config.get('Database', 'name')
    db_host = config.get('Database', 'host')
    db_port = config.getint('Database', 'port')

    client = pymongo.MongoClient(db_host, db_port)
    db = client[db_name]

    records = []
    for line in open(sys.argv[1]).readlines():
        # skip commented or new lines
        if line[0] == '#' or len(line) < 5:
            continue

        spl = line.split(' ')
        ext = spl[0].strip()
        if ext[0] != '.':
            ext = '.' + ext

        kw = spl[1].strip()
        tag = spl[2].strip()

        rec = {'ext' : ext,
               'keyword': kw,
               'tag_name' : tag}

        records.append(rec)
        print 'Adding record: %s' % str(rec)

    db.Keywords.insert(records)
    print 'All records inserted into db'

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage_and_die()

    add_keywords()

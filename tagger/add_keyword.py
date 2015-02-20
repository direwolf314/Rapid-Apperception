#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
import pymongo
import sys


def print_usage_and_die():
    print 'Usage: %s extention keyword tag_name' % sys.argv[0]
    print '\textension: extension of the file this should be associated with'
    print '\tkeyword: keyword to add'
    print '\ttag_name: tag associated with keyword'
    sys.exit(1)


def add_keyword():
    config_name = 'tagger.conf'

    config = ConfigParser.SafeConfigParser()
    config.read(config_name)

    # Set up the database connection
    db_name = config.get('Database', 'name')
    db_host = config.get('Database', 'host')
    db_port = config.getint('Database', 'port')

    client = pymongo.MongoClient(db_host, db_port)
    db = client[db_name]

    ext = sys.argv[1]
    if ext[0] != '.':
        ext = '.' + ext

    kw = sys.argv[2]
    tag = sys.argv[3]

    rec = {'ext' : ext,
           'keyword': kw,
           'tag_name' : tag}

    db.Keywords.insert(rec)

    print 'Added record: %s' % str(rec)

if __name__ == '__main__':
    if len(sys.argv) != 4:
        print_usage_and_die()

    add_keyword()

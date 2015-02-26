#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
import pymongo
import sys


def print_usage_and_die():
    print 'Usage: %s tag_name' % sys.argv[0]
    print '\ttag_name: tag name to search for'
    sys.exit(1)


def tag_query():
    config_name = 'tagger.conf'

    config = ConfigParser.SafeConfigParser()
    config.read(config_name)

    # Set up the database connection
    db_name = config.get('Database', 'name')
    db_host = config.get('Database', 'host')
    db_port = config.getint('Database', 'port')

    client = pymongo.MongoClient(db_host, db_port)
    db = client[db_name]

    tag = sys.argv[1]

    # TODO: expand this to check for
    rec = {'tag_name' : tag}

    curs = db.Keywords.find(rec)

    reg = '|'.join(rec['keyword'] for rec in curs)

    print '%s' % reg
    #sys.stdout.write('%s' % reg)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage_and_die()

    tag_query()

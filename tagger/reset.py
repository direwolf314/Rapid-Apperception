#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
import pymongo


def reset():
    config_name = 'tagger.conf'

    config = ConfigParser.SafeConfigParser()
    config.read(config_name)

    # Set up the database connection
    db_name = config.get('Database', 'name')
    db_host = config.get('Database', 'host')
    db_port = config.getint('Database', 'port')

    client = pymongo.MongoClient(db_host, db_port)
    db = client[db_name]

    db.drop_collection('TaggingInfo')
    print 'Dropped collection: TaggingInfo'


if __name__ == '__main__':
    reset()

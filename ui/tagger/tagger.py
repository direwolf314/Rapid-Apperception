'''
A Tagger parses a file or directory and adds any tags it finds to the db.
'''

import pymongo
import os
import sys


class Tagger(object):

    ''' The primary implementation of a tagger. '''

    def __init__(self, target_path, config, log):
        """Initializes a tagger object.

        :target_path: The path to the target, either file or directory
        :config: A ConfigParser to get additional information from
        :log: An instantiated log to use

        """
        self._target_path = target_path
        self._config = config
        self._log = log

        # Set up the database connection
        db_name = self._config.get('Database', 'name')
        db_host = self._config.get('Database', 'host')
        db_port = self._config.getint('Database', 'port')

        client = pymongo.MongoClient(db_host, db_port)
        self._db = client[db_name]

        self.supported_exts = self.get_supported_extensions()

    def get_supported_extensions(self):
        """Queries the database to fetch a list of extensions with existing keywords.

        :returns: A set of strings representing supported file extensions.

        """
        exts = set()

        curs = self._db.Keywords.find()
        for rec in curs:
            exts.add(rec['ext'])

        return exts

    def parse(self, file_path):
        """Parses a single file and adds tags to the database.

        :file_path: The path to the file to be parsed
        :returns: None

        """
        print 'Parsing: %s' % file_path
        #self._log.debug('Parsing: %s' % file_path)

        _, ext = os.path.splitext(file_path)

        if ext not in self.supported_exts:
            return

        #self._log.debug('Found a %s file: ' % ext + file_path)

        ti_col = self._db.TaggingInfo
        # Make sure records don't already exist
        #if ti_col.find_one({'file_path': file_path}) is not None:
            #self._log.debug('DB records for this file already exist')
            #return

        # Get tags that apply to this extension
        keywords = {}
        for rec in self._db.Keywords.find({'ext': ext}):
            keywords[rec['keyword']] = rec['tag_name']

        #self._log.debug('Keywords are: %s', str(keywords))
        print 'Keywords are: %s', str(keywords)

        # Look through the file
        content_lines = open(file_path, 'r').readlines()

        for line_num, line in enumerate(content_lines):
            for k in keywords:
                position = line.find(k)
                if position != -1:
                    new_record = {'file_path': file_path.replace('\\','/'),
                                  'ext': ext,
                                  # Add 1 because most IDE's start at 1
                                  'line_num': line_num + 1,
                                  'line_offset': position + 1,
                                  'key_match': k,
                                  'tag_name': keywords[k]}
                    ti_col.update(new_record, new_record, upsert=True);
                    print 'Found match! Added: %s' % new_record
                    #self._log.debug('Found match! Added: %s' % new_record)

    def dir_parse(self, dir_path):
        """Walks a directory and parses every file it contains.

        :dir_path: The path to the directory to be parsed
        :returns: None

        """
        #self._log.debug('Recursively parsing: %s' % dir_path)
        print 'Recursively parsing: %s' % dir_path
        for dirpath, dirnames, filenames in os.walk(dir_path):
            print 'Walking dir: %s' % dirpath
            #self._log.debug('Walking dir: %s' % dirpath)

            for f in filenames:
                self.parse(os.path.join(dirpath, f))

    def run(self):
        """Runs the tagger against the target path

        :returns: None

        """
        print 'Running...'
        if os.path.isdir(self._target_path):
            self.dir_parse(self._target_path)
        elif os.path.isfile(self._target_path):
            self.parse(self._target_path)
        else:
            #self._log.error('Target was neither file nor directory! Exiting.')
            print 'Target was neither file nor directory! Exiting.'
            sys.exit(1)

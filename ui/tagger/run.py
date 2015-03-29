#!/usr/bin/env python
# encoding: utf-8

import ConfigParser
import logging
import sys
import os

from tagger import Tagger


def print_usage_and_die():
    print 'Usage: %s target_path' % sys.argv[0]
    print '\ttarget_path : file or directory to parse and tag'
    sys.exit(1)

def initialize_log(config):
    return None
    log_name = config.get('General', 'log_name')
    print "got log name"
    logging.basicConfig(level=logging.DEBUG,
                        format=('%(asctime)s - %(name)s - '
                                '%(levelname)s - %(message)s'),
                        filename=log_name,
                        filemode='w')
    print "finished"


def run(target_path):
    print "Running run.py"
    config_name = 'tagger.conf'

    config = ConfigParser.SafeConfigParser()
    config.read(config_name)
    initialize_log(config)
    print "initted log"

    log = logging.getLogger(__name__)
    #log.debug('Log initialized!')
    print 'Log initialized to None for now'

    print "tagger"
    t = Tagger(target_path, config, log)
    t.run()


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print_usage_and_die()

    if not os.path.exists(sys.argv[1]):
        print_usage_and_die()

    run(sys.argv[1])

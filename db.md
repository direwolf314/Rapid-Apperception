Database
=========

This document details the internal structure of the database.

For our purposes, we use MongoDB.

Database: RapidApperception

Collections:

Keywords - 
    _id         : bson_objectid
    ext         : string // A file extension
    keyword     : string // The keyword text
    tag_name    : string // The tag that the keyword belongs to
    // TODO: give the ability to sub-type tags - ex. each tag has a parent_tag

TaggingInfo
    _id         : bson_objectid
    file_path   : string // full path to the file
    ext         : string // The file extension
    line_num    : int
    line_offset : int // position of the tag within the line
    key_match   : string // the keyword that was matched at this location
    tag_name    : string // the name of the tag we matched
    

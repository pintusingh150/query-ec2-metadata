#!/usr/bin/env python3
import argparse
from get_metadata import *

parser = argparse.ArgumentParser(description='To Get the top level EC2 metadata dont pass any arguments')
parser.add_argument('-path', metavar='<path>', help='To query metadata to get specific value, pass the path, eg. /tags/instance')
args = parser.parse_args()

if args.path is None:
    metadata_json_dumps(None)
else:
    metadata_json_dumps(args.path)
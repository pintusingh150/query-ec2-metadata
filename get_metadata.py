import requests
import json
from config import *


def get_metadata(path):
    if path is None:
        print('Path is empty so getting top level EC2 metadata.')
        response = requests.get(aws_ec2_metadata_url)
        top_level_metadata = json.loads(response.text)
        if is_json_valid(top_level_metadata):
            json_metadata = top_level_metadata
    else:
        if is_string(path):
            url = aws_ec2_metadata_url + path
            response = requests.get(url)
            metadata = json.loads(response.text)
            if is_json_valid(top_level_metadata):
                json_metadata =  metadata
        else:
            print('{1} is not a valid path to query the metadata.'.format(path))
            exit
    return json_metadata

def is_string(value):
    return isinstance(value, str)

def is_json_valid(json_val):
    try:
        json.loads(json_val)
    except ValueError:
        return False
    return True

def metadata_json_dumps(path):
    json_metadata = get_metadata(path)
    json_metadata = json.dumps(json_metadata, indent=2, sort_keys=True)
    return json_metadata
            



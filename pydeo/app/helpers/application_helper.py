import json
from mimetypes import guess_type
from logging import warning
from os import (
    listdir,
    path
)
from sqlalchemy.ext.declarative import DeclarativeMeta


class AlchemyEncoder(json.JSONEncoder):
    """
    Extend JSONENcoder class in order to be able to convert objects gotten from
    SQLAlchemy requests to JSON.
    """
    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            fields = {}
            attrs = [x for x in obj.__dict__.keys() if not x.startswith('_')]
            for field in attrs:
                data = obj.__getattribute__(field)
                if hasattr(data, 'isoformat'):
                    data = data.isoformat()
                json.dumps(data)
                fields[field] = data
            return fields

        return json.JSONEncoder.default(self, obj)


def to_list(l=[]):
    """
    Return l if it is a list or an empty list if the parameter is an instance
    of an other type. This helper is a workaround for a broken API (imdbpie toi
    name it).
    """
    if type(l) is list:
        return l
    else:
        return []


def bytes2human(n, format="%(value)i%(symbol)s"):
    """
    >>> bytes2human(10000)
    '9K'
    >>> bytes2human(100001221)
    '95M'
    """
    symbols = ('B', 'K', 'M', 'G', 'T', 'P', 'E', 'Z', 'Y')
    prefix = {}
    for i, s in enumerate(symbols[1:]):
        prefix[s] = 1 << (i+1)*10
    for symbol in reversed(symbols[1:]):
        if n >= prefix[symbol]:
            value = float(n) / prefix[symbol]
            return format % locals()
    return format % dict(symbol=symbols[0], value=n)


def is_video(file):
    """
    Try to determine if the given file is a movie or not.
    Return true if it is one, false otherwise.
    """
    if not path.isfile(file):
        return False
    try:
        filetype = guess_type(file)[0]
        if filetype[:5] == 'video':
            return True
        else:
            return False
    except:
        warning('Unable to detect file type: \"%s\"', file)
        return False


def list_videos(dir):
    """
    Return a list with the path to all files of type video found in the
    directory dir.
    """
    l = []
    for f in listdir(dir):
        file_path = dir + f
        if not is_video(file_path):
            continue
        l.append(file_path)
    return l

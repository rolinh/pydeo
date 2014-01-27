from sqlalchemy.ext.declarative import DeclarativeMeta
import json


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


def gen_clean_name(filename):
    """
    Take a file name and generate a clean name from it.
    For instance:
    'BatmanBegins_2005_HDRip' => 'Batman Begins'
    'The Lone Ranger 2013 TS XVID UNiQUE' => 'The Lone Ranger'
    'Iron.Man.3.2013.R6.HDScr.LINE.NoSUBS.NoBLURS.XVID.AC3.HQ' => 'Iron Man 3'
    """
    # TODO
    pass


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

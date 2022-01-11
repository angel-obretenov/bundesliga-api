import json

from suds.sudsobject import asdict

"""
# This was needed in order to serialize them, but after that I decided to not actually do DRF here
# and only return directly from Django.
"""

def recursive_asdict(d):
    """Convert Suds object into serializable format."""
    out = {}
    for k, v in asdict(d).items():
        if hasattr(v, '__keylist__'):
            out[k] = recursive_asdict(v)
        elif isinstance(v, list):
            out[k] = []
            for item in v:
                if hasattr(item, '__keylist__'):
                    out[k].append(recursive_asdict(item))
                else:
                    out[k].append(item)
        else:
            out[k] = v
    return out


def suds_to_dict(data):
    try:
        return recursive_asdict(data)
    except:
        """ I know I should not except without a class, but really don't know what to expect here """
        return []


def suds_to_json(data):
    return json.dumps(recursive_asdict(data))

import datetime


def parse_dates(record):
    parsed = record.copy()
    for k, v in record.items():
        if isinstance(v, datetime.datetime):
            parsed[k] = v.isoformat()
    return parsed


def handle_object(obj):
    return parse_dates(obj.to_dict())


class FakeBody(object):
    def __init__(self, page_number=1, page_size=100):
        self.page_number = page_number
        self.page_size = page_size

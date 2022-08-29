import datetime
import pytz
import singer
from typing import List, Optional
from tap_purecloud.util import parse_dates, handle_object, FakeBody

# import PureCloudPlatformApiSdk
# import PureCloudPlatformClientV2

from singer.utils import strptime_to_utc, strftime as singer_strftime


LOGGER = singer.get_logger()


class Stream():
    name: Optional[str] = None
    stream = {}
    key_properties: List[str] = None
    datetime_fields: List[str] = None
    url: Optional[str] = None

    replication_method: Optional[str] = None
    replication_key: Optional[str] = None
    results_key: Optional[str] = None

    def __init__(self, client, sdk, config: dict, stream):
        # TODO
        self.client = client
        self.sdk = sdk
        self.config = config
        self.stream = stream
        return

    def update_bookmark(self, state, value):
        current_bookmark = singer.get_bookmark(state, self.name, self.replication_key)
        if value and value > current_bookmark:
            singer.write_bookmark(state, self.name, self.replication_key, value)


    def transform_value(self, key, value):
        if key in self.datetime_fields and value:
            value = strptime_to_utc(value)
            # reformat to use RFC3339 format
            value = singer_strftime(value)

        return value


class Users(Stream):
    name = 'users'
    replication_method = 'FULL_TABLE'
    key_properties = ['id']
    body = FakeBody()

    def sync(self, state, config):
        from . import fetch_all_records
        api_instance = self.sdk.UsersApi()
        gen_users = fetch_all_records(
            api_instance.get_users, 'entities', self.body, {'expand': ['locations']}
        )
        for page in gen_users:
            yield page

# TODO Migrate other streams from schemas.py

STREAMS = {
    "users": Users
}

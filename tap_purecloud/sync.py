import singer
import singer.metrics as metrics
from singer import metadata

from tap_purecloud.util import handle_object


LOGGER = singer.get_logger()

def stream_results(generator, transform_record, record_name, schema, primary_key, write_schema):
    all_records = []
    if write_schema:
        singer.write_schema(record_name, schema, primary_key)
    for page in generator:
        if isinstance(page, dict):
            records = [transform_record(k, v) for (k,v) in page.items()]
        else:
            records = [transform_record(record) for record in page]
        valid_records = [r for r in records if r is not None]
        singer.write_records(record_name, valid_records)
        all_records.extend(valid_records)
    return all_records


def stream_results_list(generator, transform_record, record_name, schema, primary_key, write_schema):
    if write_schema:
        singer.write_schema(record_name, schema, primary_key)

    for page in generator:
        records_list = [transform_record(record) for record in page]
        for records in records_list:
            singer.write_records(record_name, records)


def sync_stream(state, start_date, instance):
    stream = instance.stream

    # If we have a bookmark, use it; otherwise use start_date & update bookmark with it
    if (instance.replication_method == 'INCREMENTAL' and
            not state.get('bookmarks', {}).get(stream.tap_stream_id, {}).get(instance.replication_key)):
        singer.write_bookmark(state,
                              stream.tap_stream_id,
                              instance.replication_key,
                              start_date)

    parent_stream = stream
    with metrics.record_counter(stream.tap_stream_id) as counter:
        for page in instance.sync(state, instance.config):

            # Perform our transformation function handle_object?
            if isinstance(page, dict):
                records = [handle_object(k, v) for k, v in page.items()]
            else:
                records = [handle_object(record) for record in page]

            # NB: Only count parent records in the case of sub-streams
            if stream.tap_stream_id == parent_stream.tap_stream_id:
                counter.increment(amount=len(records))

            # with singer.Transformer() as transformer:
            #     rec = transformer.transform(record, stream.schema.to_dict(), metadata=metadata.to_map(mdata))

            # A deviation from the standard implementation is that we
            # use the write_records method instead of write_record as we fetch multiple records by page
            singer.write_records(stream.tap_stream_id, records)


            # NB: We will only write state at the end of a stream's sync:
            #  We may find out that there exists a sync that takes too long and can never emit a bookmark
            #  but we don't know if we can guarentee the order of emitted records.

        return counter.value

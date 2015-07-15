# KVStoreClient

A small client library for interfacing with Splunk KVStores within Splunk apps or generally with the Splunk Python SDK.

## Installation

Include it with an existing Splunk app and import it. Requires Splunk python sdk (splunklib). You must have an existing collection with a kvstore lookup in your transforms.conf file.

`from KVStoreClient import KVStoreClient`

## Usage

If running inside a search command (StreamingCommand, GeneratingCommand, ReportingCommand, etc):

`kv = KVStoreClient(appname,colleciton,lookup, self.service)`

If running separately:

`kv = KVStoreClient(appname,collection,lookup, splunklib.Client(...))`

### Get
`kv.get_all()`

Returns a list of all records in KV.

`kv.get_by_field(field, value)`

Returns a list of all records where field=value

`kv.get_by_key(key)`

Returns a single record (dict) where _key=key

### Delete
`kv.delete_by_field(field, value)`

Deletes all records where field=value. Returns deleted records.

`kv.delete_key(key)`

Deletes the record for specified key.

### Add & Update
`kv.add(content)`

Adds new record with data equal to content, where content is of type dict. Returns new key.

`kv.add(key, content)`

Updates existing entry for key with new content, where content is of type dict. Does not return.

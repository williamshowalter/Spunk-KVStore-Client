# KVStoreClient

A small client library for interfacing with Splunk KVStores within Splunk apps or generally with the Splunk Python SDK.

## Installation

Include it with an existing Splunk app and import it. Requires Splunk python sdk (splunklib). You must have an existing collection with a kvstore lookup in your transforms.conf file.

`from KVStoreClient import KVStoreClient`

## Usage

If running inside a search command (StreamingCommand, GeneratingCommand, ReportingCommand, etc):

`kv = KVStoreClient(appname,colleciton,lookup, self.service)`

If running separately:

`kv = KVStoreClient(appname,collection,lookup, splunklib.client.connect(...))`

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

## License
Licensed under the Apache License, Version 2.0 (the "License"): you may
not use this file except in compliance with the License. You may obtain
a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
License for the specific language governing permissions and limitations
under the License.
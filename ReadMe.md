# KVStoreClient

A small client library for interfacing with Splunk KVStores within Splunk apps or generally with the Splunk Python SDK.

[![License](https://img.shields.io/:License-MIT-blue.svg)](http://dotlog.mit-license.org)


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
The MIT License (MIT)
Copyright © 2015

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
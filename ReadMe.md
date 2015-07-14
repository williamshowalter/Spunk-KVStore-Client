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
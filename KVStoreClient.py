from splunklib.results import ResultsReader
import json

class KVStoreClient:
    def __init__(self, APPNAME, COLLECTION, LOOKUP, service):
        self.APPNAME = APPNAME
        self.COLLECTION = COLLECTION
        self.LOOKUP = LOOKUP
        self.service = service
        self.path = "storage/collections/data/%s" % (self.COLLECTION)
        self.headers = [('content-type','application/json')]

    def get_all(self, key = None):
        rData = self.service.request(self.path, method="GET", headers=self.headers, owner='nobody', app=self.APPNAME)
        rData = json.loads(rData['body'].read())

        return rData

    def get_by_field(self, field, value):
        records = []

        allByField = self.service.jobs.create("|inputlookup %s | search %s=%s" % (self.LOOKUP, field, str(value)), **{"exec_mode":"blocking"})
        allByField = allByField.results(count=0)

        for record in ResultsReader(allByField):
            if isinstance (record,dict):
                records.append(record)

        return records

    def get_by_key(self, key):
        allByKey = self.service.jobs.create("|inputlookup %s | rename _key AS key | search key=%s" % (self.LOOKUP, key),**{"exec_mode":"blocking"})
        allByKey = allByKey.results(count=0)

        return next((record for record in allByKey), None)

    def delete_by_field(self, field, value):
        records = self.get_by_field(field, value)

        for record in records:
            self.delete_key(record['_key'])

        return records

    def delete_key(self, key):
        self.service.request(self.path+'/'+key, method='DELETE', headers=self.headers, owner='nobody',app=self.APPNAME)

    def add(self,content):
        newKey = self.service.request(self.path, method='POST', headers=self.headers, \
            owner='nobody',app=self.APPNAME, body=json.dumps(content))
        return json.loads(newKey['body'].read())['_key']

    def update(self, key, content):
        updated = self.service.request(self.path + "/%s" % (key), method='POST', headers=self.headers, \
            owner='nobody', app=self.APPNAME, body=json.jumps(content))
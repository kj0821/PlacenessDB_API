# -*- coding: utf-8 -*-

import urllib2
import json

class firebase:
    def __init__(self, url) :
        self.root = url 

    def push(self, node, data):
        request = urllib2.Request(self.root+node+".json", data, {'Content-Type': 'application/json'})
        urlop = urllib2.urlopen(request)
        res = json.load(urlop)['name']
        return res
    
    def put(self, node, data):
        request = urllib2.Request(self.root+node+".json", data, {'Content-Type': 'application/json'})
        request.get_method = lambda: 'PUT'
        urlop = urllib2.urlopen(request)
    
    def get(self, node):
        request = urllib2.Request(self.root+node+".json")
        urlop = urllib2.urlopen(request)
        res = json.load(urlop)
        return res


#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib, urllib, urllib2
import json
import codecs
import pdb

def uploadData(dataJson):
    print "Will upload data"
    value = {
        "name" : "serverall",
        "opt":"put",
        "data":dataJson
    }

    enData = urllib.urlencode(dict([k, v.encode('utf-8')] for k,v in value.items())) 
    print "En Data:" 
    print enData

    gUrl= "http://210.51.17.76:1218/"+"?"+enData
    print gUrl 

    resp = urllib2.urlopen(gUrl)
    print "Save date"
    print resp.getcode()
    print resp.read()
    print resp.info()

    #sync

    print "SYNC"
    sUrl = "http://122.70.151.106:8099/api/collection/get.php"
    print "will open"
    sResp = urllib2.urlopen(sUrl)
    print "have opend"
    print "Sync data:" 
    print sResp.getcode()
    print sResp.read()
    print sResp.info()


if __name__ == '__main__':
    itemDict = {}
    itemDict['dateline'] = ''
    itemDict['viewnum'] = '1'
    itemDict['cid'] = '44'
    itemDict['catid'] = '44'
    itemDict['name'] = 'admin'
    itemDict['username'] = 'admin'
    itemDict['title'] = 'test1' 
    itemDict['summary'] = 'sumtest'
    itemDict['content'] = "我们" 

    value = json.dumps(dict(itemDict),ensure_ascii=False)+'\n'
    print value
    uploadData(value)
    

#!/usr/bin/env python
# -*- coding: utf-8 -*-

import httplib, urllib, urllib2
import json
import codecs
import pdb

def uploadData(dataJson):
    #hclient = httplib.HTTPConnection("210.51.17.76", 1218, False)
    
    #getUrl = '/'
#    getBody = '?name=serverall&opt=put&data='+data
    #dataDict = data
#    params = urllib.urlencode(data)
#    getParams = '?name=serverall&opt=put&data='+params
    print "Will upload data"
    value = {
        "name" : "serverall",
        "opt":"put",
        "data":dataJson
    }

    #enData = urllib.urlencode(value) 
    enData = urllib.urlencode(dict([k, v.encode('utf-8')] for k,v in value.items())) 
    print "En Data:" 
    print enData
    #print enData 

    #hclient.request('get',getUrl,getParams)

    #resp = hclient.getresponse()

    #print resp.status
    #print resp.reason
    #print resp.read()
    #hclient.close()

    gUrl= "http://210.51.17.76:1218/"+"?"+enData
    #gUrl= "http://210.51.17.76:1218/?name=serverall&opt=put"
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
    #pdb.set_trace()
    print sUrl
    sResp = urllib2.urlopen(sUrl)
    print "have opend"
    print "Sync data:" 
    print sResp.getcode()
    print sResp.read()
    print sResp.info()
    #hclient = httplib.HTTPConnection('122.70.151.106', 8099, False)
    
    #getUrl = '/api/collection/get.php'

    #hclient.request('get',getUrl)

    #resp = hclient.getresponse()

    #print resp.status
    #print resp.reason
    #print resp.read()
    #hclient.close()


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
    

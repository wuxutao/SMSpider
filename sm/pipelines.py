# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#dell :20
#hp:   19
#ibm:  18
import json
import codecs
from sm.items import SmItem
from sm.serverall import uploadData

class SmPipeline(object):
    def process_item(self, item, spider):
        print "\n\n\n\n\n"
        print "I AM PIPLELINE"
        
        itemDict = {}
        itemDict['dateline'] = ''
        itemDict['viewnum'] = '1'
        itemDict['cid'] = '20'
        itemDict['catid'] = '20'
        itemDict['name'] = 'admin'
        itemDict['username'] = 'admin'
        itemDict['title'] = item['smTitle']
        itemDict['summary'] = ''
        itemDict['content'] = item['smContent']

        value = json.dumps(dict(itemDict),ensure_ascii=False)+'\n'
        #print value
        uploadData(value)
        return item
        #raise DropItem("Missing t")

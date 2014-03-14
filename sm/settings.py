# Scrapy settings for sm project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'sm'

SPIDER_MODULES = ['sm.spiders']
NEWSPIDER_MODULE = 'sm.spiders'
ITEM_PIPELINES = ['sm.pipelines.SmPipeline']
# Crawl responsibly by identifying yourself (and your website) on the user-agent
#USER_AGENT = 'sm (+http://www.yourdomain.com)'

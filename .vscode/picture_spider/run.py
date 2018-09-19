from scrapy import cmdline
name='picture_spider'
cmd='scrapy crawl {0}'.format(name)
cmd=cmd.split()
cmdline.execute(cmd)
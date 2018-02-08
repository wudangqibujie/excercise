from DataOutput import DataOutput
from HtmlDownloader import HtmlDownloader
from HTMLParser import HtmlParser
from UrlManager import UrlManager
class SpiderMan(object):
    def __init__(self):
        self.manager = UrlManager()
        self.downloader = HtmlDownloader()
        self.parser = HtmlParser()
        self.output = DataOutput()
    def crawl(self,root_url):
        self.manager.add_new_url(root_url)
        # print("---")
        # print(self.manager.new_urls)
        # print(self.manager.has_new_url())
        # print(self.manager.new_url_size())
        # print(self.manager.old_url_size())
        # print(self.manager.get_new_url())
        # print("------")
        while(self.manager.has_new_url() and self.manager.old_url_size()<2):
            try:
                new_url = self.manager.get_new_url()
                print(new_url)
                html = self.downloader.download(new_url)
                new_urls,data = self.parser.parser(new_url,html)
                print(new_urls)
                print(data)
                self.manager.add_new_urls(new_urls)

                self.output.store_data(data)
                print("已经抓取%s个链接"%self.manager.old_url_size())
            except:
                print("crawl failed")
        self.output.output_txt()

if __name__ == "__main__":
    spider_man = SpiderMan()
    spider_man.crawl("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB")



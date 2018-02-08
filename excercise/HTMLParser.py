import  re
import urllib.parse
from bs4 import BeautifulSoup
from lxml import etree

class HtmlParser(object):
    def parser(self,page_url,html_cont):
        if page_url is None or html_cont is None:
            return
        soup = BeautifulSoup(html_cont,'lxml')
        new_urls = self._get_new_urls(page_url,soup)
        new_data = self._get_new_data(page_url,soup)
        return new_urls,new_data
        # print(new_urls)
        # print(new_data)
    def _get_new_urls(self,page_url,soup):
        new_urls = set()
        links = soup.find_all('a',href=re.compile(r'/item/.*?'))
        for link in links:
            new_url = link['href']
            new_full_url = urllib.parse.urljoin(page_url,new_url)
            new_urls.add(new_full_url)
        return new_urls
    def _get_new_data(self,page_url,soup):
        data= {}
        data['url'] = page_url
        title = soup.find("dd",class_="lemmaWgt-lemmaTitle-title").find("h1")
        data['title'] = title.get_text()
        summary = soup.find('div',class_='lemma-summary')
        data['summary'] = summary.get_text()
        return data


if __name__ == "__main__":
    import requests
    user_agent = "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36"
    headers = {'User-Agent':user_agent}
    r = requests.get("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB",headers=headers)
    r.encoding = "utf-8"
    a = HtmlParser()
    a.parser("https://baike.baidu.com/item/%E7%BD%91%E7%BB%9C%E7%88%AC%E8%99%AB",r.text)




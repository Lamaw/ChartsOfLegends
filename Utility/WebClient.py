__author__ = 'amahouix'

import urllib2

class WebClient():

    def __init__(self, base_adress, proxy):
        self.base_adress = base_adress
        if proxy is not None:
            proxy_support = urllib2.ProxyHandler({"http":proxy})
            opener = urllib2.build_opener(proxy_support)
            urllib2.install_opener(opener)

    def get_main_page(self):
        return urllib2.urlopen(self.base_adress)


    def get_web_page(self, url_complement):
        url = self.base_adress + "/" + url_complement
        return urllib2.urlopen(url)
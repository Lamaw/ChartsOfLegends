from Utility.WebClient import WebClient
from Utility import xmlParser
from Utility import PageAnalyzer

#PageAnalyzer Instanciation

config = xmlParser.ParsedConfig()
client = WebClient("http://leagueoflegends.wikia.com/wiki","http://proxy-jf.intel.com:911")
analyzer = PageAnalyzer.PageAnalyzer(config.config)

response = client.get_web_page("champions")

page = response.read()

champ_list = analyzer.extract_champ_list(page)
for champ in champ_list:
    print champ
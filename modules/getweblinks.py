import urllib.request 
import modules.bcolors
import bs4

"""Get all onion links from the website"""
def getLinks(soup):
    _soup_instance = bs4.BeautifulSoup
    extensions = ['.onion','.onion/']
    if isinstance(type(soup), type(_soup_instance)):
        websites = []
        for link in soup.find_all('a'):
            web_link = link.get('href')
            if web_link != None:
                if 'http' in web_link:
                    for extension in extensions:
                        if web_link.endswith(extension):
                            websites.append(web_link)
            else:
                pass
        """Pretty print output as below"""
        print ('') 
        print ('Websites Found - '+str(len(websites)))
        print ('-------------------------------')
        for web in websites:
            if (urllib.request.urlopen(web).getcode() == 200):
                print (web)
            else :
                print(bcolors.On_Red+web +bcolors.ENDC)    
        return websites
    else:
        raise('Method parameter is not of instance bs4.BeautifulSoup')

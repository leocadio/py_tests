from urllib.request import urlopen
from bs4 import BeautifulSoup
import re



def start_page_links(start_page):
    '''input: site main page url, link to external site
    output: list of internal links
        
    '''
    try:
        html = urlopen(start_page)
        bsObj = BeautifulSoup(html)#, 'lxml')
        bshref = bsObj.find_all('a', href = True)
        main_page_links = []
        main_page_links.append(start_page)
        for line in bshref:
            a=line.get('href')
            if len(a)>4 and a[:4]!='http' and start_page+'/'+a not in main_page_links:
                main_page_links.append(start_page+'/'+a)
        return main_page_links
    except:
        print ('startPage is invalid url\nTry another call of fuction mainPageLinks')





def page_links(start_page, external_link_part):
    '''input: site main page url, link to external site
    output: list of internal links        
    '''
    html = urlopen(start_page)
    bsObj = BeautifulSoup(html, 'lxml')
    bshref = bsObj.find_all('a', href = True)
    main_page_links = []
    main_page_links.append(start_page)
    for line in bshref:
        a=line.get('href')
        if len(a)>4 and a[:4]!='http' and start_page+'/'+a not in main_page_links:
            main_page_links.append(start_page+'/'+a)
            
    external_links = []     
    for url in main_page_links:
        html = urlopen(url)
        bsObj = BeautifulSoup(html, 'lxml')
        bshref = bsObj.find_all('a', href = True)
        for line in bshref:
            external_link=line.get('href')
            if (external_link[:4]=='http') and (re.search(external_link_part, external_link)) and (external_link not in external_links):
                    external_links.append(external_link)
    return external_links


def list_to_file(name_of_list, file_name):
    """ in: name of list you want to write; path_to_file you want to write.csv
        out: read.csv """
    file = open (file_name, 'w')
    for line in name_of_list:
        file.write(line+'\n')
    file.close()
    
    '''    
    except:
        print ('startPage is invalid url\nTry another call of fuction mainPageLinks')
'''

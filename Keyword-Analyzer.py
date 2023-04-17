import requests 
from bs4 import BeautifulSoup

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'
}
 
def make_request(url,headers):
    try:
        r = requests.get(url, headers=headers)
    except requests.exceptions.RequestException as e: 
        raise SystemExit(e)
    return r
 

url = input("what is your Keyword: ")
Search_voulme = input("what is Keyword search voulme: ")

search_url1 = f'https://www.google.com/search?q=allintitle%3A'+url+'&oq=all&aqs=chrome.1.69i57j69i59l3j69i65j69i60l3.2231j0j1&sourceid=chrome&ie=UTF-8'
search_url2 = f'https://www.google.com/search?q=%22'+url+'%22&sxsrf=APwXEdd0F6Cvu-EXVJMGTHtyhb5fIp-AqA%3A1681756998578&ei=RpM9ZNrxIsSHkdUP8fSRuAI&ved=0ahUKEwjarP6DybH-AhXEQ6QEHXF6BCcQ4dUDCA8&uact=5&oq=%22how+to+become+a+soft+skills+trainer%22&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIFCAAQgAQyBggAEBYQHjIGCAAQFhAeMgYIABAWEB4yBggAEBYQHjIICAAQigUQhgM6CggAEEcQ1gQQsAM6CggAEIoFELADEENKBAhBGABQogpY8hpgvR1oAXABeACAAaUBiAGyA5IBAzAuM5gBAKABAaABAsgBCsABAQ&sclient=gws-wiz-serp'

def keyword_analyzer():
    #All in title
    r = make_request(search_url2,headers)
    soup = BeautifulSoup(r.text, "html.parser")
    index = soup.find('div',{'id':'result-stats'})
    result = []
    result.append(index.text.split())
    final = result[0][1]
    all_in_content = float(final.replace(',', '').replace('%', ''))
    
    #KGR
    r = make_request(search_url1,headers)
    soup = BeautifulSoup(r.text, "html.parser")
    index = soup.find('div',{'id':'result-stats'})
    result = []
    result.append(index.text.split())
    final = result[0][1]
    f_final = float(final.replace(',', '').replace('%', '')) 
    KGR = f_final / float(Search_voulme)
    
    #Final Analyzer
    if KGR <= .25 and all_in_content <=100:
        print("All in content = "+str(all_in_content))
        print("KGR = "+str(KGR))
        print("Your keywords is very easy to rank!")
    elif KGR <= .25  and all_in_content >100:
        print("All in content = "+str(all_in_content))
        print("KGR = "+str(KGR))
        print("Your Keyword is not difficult but it takes more work, Because it has a large number of all in content.")
    elif KGR >=.251 and  KGR<= 1  and all_in_content >100:
        print("All in content = "+str(all_in_content))
        print("KGR = "+str(KGR))
        print("Your Keyword is not difficult but it takes more work, Because it has a large number of all in content.")
    elif KGR  >=.251 and  KGR<= 1 and all_in_content <=100:
        print("All in content = "+str(all_in_content))
        print("KGR = "+str(KGR))
        print("Your Keyword is not difficult but it takes more work, Because it has a large KGR ratio.")
    else:
        print("All in content = "+str(all_in_content))
        print("KGR = "+str(KGR))
        print("Your Keyword is difficult, And you may need a number of backlinks.") 

keyword_analyzer()

import requests
from bs4 import BeautifulSoup
import json
import time

KAKAO_TOKEN = "arzBUbHsQQ4gQ-XslN4KEEVMLcF683fGdrMBcAopb1QAAAFx47mMEQ"
keyword = "ipad"

'''
curl -v -X POST "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    -H "Authorization: Bearer arzBUbHsQQ4gQ-XslN4KEEVMLcF683fGdrMBcAopb1QAAAFx47mMEQ"
    -d 'template_object = {
        "object_type":"text",
        "text" : "텍스트 영역입니다. 최대 200자 표시 가능합니다.",
        "link" : {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url":"https://developers.kakao.com"
        },
        "button_title":"바로 확인"
    }'
    
    
'''
def send_kakao(text):
    header = {"Authorization" : "Bearer "+KAKAO_TOKEN}
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"
    post = {
        "object_type":"text",
            "text" : text,
            "link" : {
                "web_url": "https://developers.kakao.com",
                "mobile_web_url":"https://developers.kakao.com"
            },
            "button_title":"바로 확인"
    }

    data = {"template_object" : json.dumps(post)}
    r = requests.post(url,headers=header,data=data)
    print(r.text)


def get_hotdeal(keyword):
    url = "https://slickdeals.net/newsearch.php?src=SearchBarV2&q={}&searcharea=deals&searchin=first".format(keyword)


    r = requests.get(url)
    bs = BeautifulSoup(r.text,"lxml")
    rows = bs.select("div.resultRow")

    result = []

    for r in rows:
        link = r.select("a.dealTitle")[0]
        href = link.get("href")
        if href is None : 
            continue
        
        href = "https://slickdeals.net/"+href
        title = link.text
        price = r.select("span.price")[0].text.replace("$" , "").replace("from" ,"").replace("Free","").strip()
        if price.find("/") >= 0 or price == "":
            continue

        price = float(price)
        hot = len(r.select("span.icon-fire"))
        result.append((title,href,price,hot))
        #print(result)
    return result


send_lists = []
        
def main():
    keword = "ipad"
    max_price = 300.0
    while True : 
        results = get_hotdeal(keword)
        if results is not None:
            for r in results:
                title,href,price,hot = r
                if price < max_price:
                    if title not in send_lists :
                        msg = "{} {} {} {}".format(title,price,hot,href)
                        send_kakao(msg)
                        send_lists.append(title)
        time.sleep(60*5)
        


main()
from selenium import webdriver
import time
import json

def scrapData():
    option = webdriver.ChromeOptions()
    option.add_argument('headless') 
    option.add_argument("--log-level=3")
    jsonmain = []
    browser = webdriver.Chrome('chromedriver',options=option)
    URL = "https://www.bovada.lv/sports/esports"
    browser.get(URL)
    time.sleep(7) # Let the user actually see something!
    headers  = browser.find_elements_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div[*]/h4');
    exp_coll = browser.find_elements_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div[*]/h4/i')
    for ex_co in exp_coll:
        if "icon-plus" in ex_co.get_attribute("className"):
            ex_co.click()
    for i,header in enumerate(headers):
        # timestamps = browser.find_elements_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon/sp-multi-markets/section/section/sp-score-coupon/span')
        # teams = browser.find_elements_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon/sp-multi-markets/section/section/header/sp-competitor-coupon');
        print ("-------------------------------------------------------")
        headTitle = header.get_attribute("innerText")
        print("*****HEADER*****\n", headTitle)
        jsondict = {}
        jsondict['header'] = headTitle
        length = header.get_attribute("innerText").split('(')[1].replace(')','')
        matches = []
        for j in range(int(length)):
            match = {}
            timestamp = browser.find_element_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon['+str(j+1)+']/sp-multi-markets/section/section/sp-score-coupon/span').get_attribute('innerText')
            teams = browser.find_element_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon['+str(j+1)+']/sp-multi-markets/section/section/header/sp-competitor-coupon').get_attribute('innerText')
            spread = browser.find_element_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon['+str(j+1)+']/sp-multi-markets/section/section/sp-outcomes/sp-two-way-vertical[1]').get_attribute('innerText')
            win = browser.find_element_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon['+str(j+1)+']/sp-multi-markets/section/section/sp-outcomes/sp-two-way-vertical[2]').get_attribute('innerText')
            total = browser.find_element_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon['+str(j+1)+']/sp-multi-markets/section/section/sp-outcomes/sp-two-way-vertical[3]').get_attribute('innerText')
            print("*****Date Time*****\n"+timestamp)
            print("*****Competitors Teams*****\n"+teams)
            print("*****Spread*****\n"+spread)
            print("*****WIN*****\n"+win)
            print("*****TOTAL*****\n"+total)
            match['timestamp'] = timestamp
            match['teams'] = teams
            match['spread'] = spread
            match['win'] = win
            match['total'] = total
            matches.append(match)
        print ("-------------------------------------------------------")
        jsondict['matches'] = matches
        jsonmain.append(jsondict)
    # browser.quit;
    with open("sample.json","w") as outfile:
        json.dump(jsonmain, outfile, indent=4)

    with open("sample.json") as readfile:
        data = json.load(readfile)
        print(data)
    print('END')

scrapData()
    

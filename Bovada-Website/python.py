from selenium import webdriver
import time

if __name__ == '__main__':
    # option = webdriver.ChromeOptions()
    # option.add_argument('headless') 
    browser = webdriver.Chrome('chromedriver')
    URL = "https://www.bovada.lv/sports/esports"
    browser.get(URL)
    time.sleep(7) # Let the user actually see something!
    headers  = browser.find_elements_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div[*]/h4');
    for i,header in enumerate(headers):
        # timestamps = browser.find_elements_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon/sp-multi-markets/section/section/sp-score-coupon/span')
        # teams = browser.find_elements_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon/sp-multi-markets/section/section/header/sp-competitor-coupon');
        print ("-------------------------------------------------------")
        print("*****HEADER*****\n",header.get_attribute("innerText"))
        length = header.get_attribute("innerText").split('(')[1].replace(')','')
        for j in range(int(length)):
            timestamp = browser.find_element_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon['+str(j+1)+']/sp-multi-markets/section/section/sp-score-coupon/span')
            teams = browser.find_element_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon['+str(j+1)+']/sp-multi-markets/section/section/header/sp-competitor-coupon')
            spread = browser.find_element_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon['+str(j+1)+']/sp-multi-markets/section/section/sp-outcomes/sp-two-way-vertical[1]')
            win = browser.find_element_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon['+str(j+1)+']/sp-multi-markets/section/section/sp-outcomes/sp-two-way-vertical[2]')
            total = browser.find_element_by_xpath('/html/body/bx-site/ng-component/div/sp-sports-ui/div/main/div/section/main/sp-path-event/div/sp-next-events/div/div/div[2]/div['+str(i+1)+']/sp-coupon['+str(j+1)+']/sp-multi-markets/section/section/sp-outcomes/sp-two-way-vertical[3]')
            print("*****Date Time*****\n"+timestamp.get_attribute("innerText"))
            print("*****Competitors Teams*****\n"+teams.get_attribute("innerText"))
            print("*****Spread*****\n"+spread.get_attribute("innerText"))
            print("*****WIN*****\n"+win.get_attribute("innerText"))
            print("*****TOTAL*****\n"+total.get_attribute("innerText"))
        print ("-------------------------------------------------------")
    # browser.quit;
    print('END')
    

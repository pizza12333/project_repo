import re
import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from urllib.request import urlopen

def get_access(Id, pw, query):
    
    driver = webdriver.Chrome()

    driver.get('https://www.bigdatahub.co.kr/login.do')
    # sk datahub id 와 password를 Id, pw에 할당한다.
    Id = Id
    pw = pw

    Id_input = driver.find_element_by_class_name('id_field')
    Id_input = Id_input.find_element_by_name('login_id')
    Id_input.send_keys(Id)

    pw_input = driver.find_element_by_class_name('pw_field')
    pw_input = pw_input.find_element_by_name('password')
    pw_input.send_keys(pw, Keys.ENTER)
    time.sleep(1)

    driver.get('https://www.bigdatahub.co.kr/product/list.do?event_type=TPREMIUM')
    time.sleep(1)

    driver.find_element_by_name('search_title').clear()
    driver.find_element_by_name('search_title').send_keys(query, Keys.ENTER)
    driver.find_element_by_id('search_btn').click()
    time.sleep(3)

    pages = driver.find_elements_by_class_name("num_box")

    pid_num = []
    pid_num_link_all = []
    for page_num in range(1,len(pages)+2):
        print(page_num)
        try:
            driver.execute_script('goPage({0})'.format(page_num))
            time.sleep(1)
        except:
            alert = driver.switch_to_alert()
            alert.accept()
            time.sleep(1)
        time.sleep(2)
        table = driver.find_element_by_xpath('//*[@id="tRs"]')
        a_tag = table.find_elements_by_tag_name('a')
        pid_num_link = []
        for num, a in enumerate(a_tag):
            pid_num_link.append(a.get_attribute('href'))
        x = pd.Series(pid_num_link)
        idx = x.apply(lambda x: x[:5])[x.apply(lambda x: x[:5]) == 'https'].index
        x = x[idx]
        x.reset_index(drop = True ,inplace =True)  
        pid_num_link = []
        for num, i in enumerate(x):
            if num % 3 == 0:
                pid_num_link_all.append(x[num])
                pid_num_link.append(x[num])
                pid_num.append(x[num][-7:])
        
        for num_link, link in enumerate(pid_num_link):
            print(link)
            
            try:
                driver.get(link)
                time.sleep(1)
            except:
                alert = driver.switch_to_alert()
                alert.accept()
                time.sleep(1)
            try:
                driver.find_elements_by_class_name('size02')[1].click()
                time.sleep(1)
                driver.switch_to_frame(driver.find_element_by_id("smartPop_frame"))
                driver.find_element_by_id('data_opt01').click()
                time.sleep(1)
                driver.find_elements_by_class_name('size02')[0].click()
                time.sleep(1)
            except:
                alert = driver.switch_to_alert()
                alert.accept()
                time.sleep(1)
                
            if (num_link == len(pid_num_link)-1):
                try:
                    driver.get('https://www.bigdatahub.co.kr/product/list.do?event_type=TPREMIUM')
                    time.sleep(1)
                    driver.find_element_by_name('search_title').clear()
                    driver.find_element_by_name('search_title').send_keys('치킨', Keys.ENTER)
                    driver.find_element_by_id('search_btn').click()
                    time.sleep(1)
                except:
                    alert = driver.switch_to_alert()
                    alert.accept()
                    time.sleep(1)
    return pid_num
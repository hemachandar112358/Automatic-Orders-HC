from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import random
import time
from warnings import catch_warnings
from datetime import datetime
import smtplib


def orders():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--incognito")


    chrome_options.add_argument('--ignore-certificate-errors')

    browser = webdriver.Chrome(executable_path='C:/Users/Hemachandar/Downloads/chromedriver.exe', chrome_options=chrome_options);
    browser.maximize_window()

    browser.get("https://www.horchow.com/")
# print(len(browser.find_elements_by_class_name("bx-button")))
# if(length(browser.find_elements_by_class_name("bx-button")))
# browser.find_elements_by_class_name("bx-close-xsvg")[1].click()
# browser.switch_to_frame()
    cookie = {'name':'WPG', 'value':'true', 'domain':'www.horchow.com'}
    browser.add_cookie(cookie)
    search = browser.find_element_by_id("searchInput")
    search.send_keys("bowls")
    search.send_keys(Keys.ENTER)

    products = browser.find_elements_by_class_name("product-thumbnail-image")

    if(len(products)):
        random.choice(products).click()
    else:
        print("something is wrong")

    addToCartBtn = browser.find_elements_by_class_name("topAddToCartButton")
    addToCartBtn[0].click()
    time.sleep(3)
    browser.find_element_by_id("lbl_easycarheader_top").click()

    email = browser.find_element_by_class_name("emailAddField")
    password = browser.find_element_by_id("i-login-pass")

    email.send_keys("ops@nmtest.info")
    password.send_keys("Infy123+")
    browser.find_element_by_id("full-reg-checkout_msk").click()

    try:
        browser.find_element_by_id("mergeNo").click()

    except:
        print("No session include items")

    try:
        browser.find_element_by_id("logged-in-checkout_msk").click()

    except:
        print("No resume checkout")

    try:
        browser.find_element_by_id("i-del-phone0").send_keys("1234567890")

    except:
        print("No delivery number")

    cvv = browser.find_element_by_id("secCode")
    cvv.send_keys("123")

    browser.find_element_by_class_name("placeorderBtn").click()
    time.sleep(5)
    try:
        browser.find_element_by_id("btn_UseSelectedAddress").click()
    except:
        print("no select address")
    time.sleep(5)
    order = browser.find_elements_by_class_name("OneLinkNoTx")
    hcOrder = order[0].text
    print(order[0].text)
    browser.close()
    '''element=browser.find_element_by_class_name("modal-close-x")
    ac = ActionChains(browser)
    ac.move_to_element(element[0]).move_by_offset(50, 50).click().perform()
    '''
    timePresent = datetime.now()
    timePresent = timePresent.strftime("%m/%d/%Y %H:%M")

    s = smtplib.SMTP('smtp.gmail.com', 587)

    s.starttls() 
    s.login("hemachandarpalaparthi@gmail.com", "asdf.123") 
    message = """From: Hemachandar <hemachandarpalaparthi@gmail.com>
    To: Bhargava <Bhargava_Akula@infosys.com>
    Subject: Test horchow order

    Order Number <""" + hcOrder + """>placed at """ + timePresent + """
    """
    s.sendmail("hemachandarpalaparthi@gmail.com", "Bhargava_Akula@infosys.com", message) 
    s.quit() 

t=0
while(t<52):
    print(t)
    t+=1
    orders()
    time.sleep(600)
    


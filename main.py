import time

from bs4 import BeautifulSoup
from selenium import webdriver
import helper_surname

driver = webdriver.Firefox()
driver.implicitly_wait(30)

login = input("Логин: ")
password = input("Пароль: ")

try:
    SCROLL_PAUSE_TIME = 2

    driver.get('https://account.ycombinator.com/?continue=https%3A%2F%2Fwww.startupschool.org%2Fusers%2Fsign_in')    
    print('sing_in page opened')
    driver.find_element_by_id('ycid-input').send_keys(login)
    print('entered login')
    driver.find_element_by_id('password-input').send_keys(password)
    print('entered password')
    driver.find_element_by_class_name('sign-in-button').click()
    print('pressed LOG IN button')
    time.sleep(10)
    driver.find_element_by_xpath('/html/body/div[2]/div[2]/div/div[1]/section[2]/div[1]/a[1]').click()
    time.sleep(10)
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(SCROLL_PAUSE_TIME)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            break
        last_height = new_height

    soup = BeautifulSoup(driver.page_source, "html.parser")


    count = 0
    with open("result.html", "w", encoding="utf-8") as file:
        file.write('<link rel="stylesheet" href="https://www.startupschool.org/packs/css/application-b8935dc9.css">')
        for company in soup(class_='directory-company-profile'):
            for founder in company.find_all(class_ ='founder'):
                done = False
                founder_name = founder.find(class_='name')
                print('Founder: ' + founder_name.text.rstrip())
                if helper_surname.check(founder_name.text):
                    for link in company.find_all('a', href=True):
                        link['href'] = 'https://www.startupschool.org' + str(link['href'])
                    file.write(company.prettify())
                    count = count + 1
                    done = True
                    break
                if done:
                    break
        print("Totall companies: " + str(count))
        file.close()
finally:
    driver.quit()
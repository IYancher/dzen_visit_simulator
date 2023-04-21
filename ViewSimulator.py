import os, random, time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains


FILE_LINKS = os.path.join(os.path.dirname(__file__), "links.txt")
FILE_ACCOUNTS = os.path.join(os.path.dirname(__file__), "accounts.csv")


with open(FILE_LINKS) as f:
    links_list = f.readlines()
    for i in range(len(links_list)):
        links_list[i] = links_list[i].strip()
    
    
def random_account():
    with open(FILE_ACCOUNTS) as f:
        accounts_list = f.readlines()
    
    account = accounts_list[random.randint(0,len(accounts_list)-1)].strip().split(",")
    login = account[0]
    password = account[1]

    return login, password


def view_post(link, recursion = False):
    time.sleep(5)
    browser.get(link)
    
    for i in range(random.randint(7,12)):
        time.sleep(random.randint(5,15))
        ActionChains(browser).scroll_by_amount(50, random.randint(100,700)).perform()
    pass

    # go to the comments
    comments = browser.find_element(By.CLASS_NAME, "zen-comments")
    ActionChains(browser).move_to_element(comments).perform()

    if recursion == False:
        try:
            post_link = browser.find_element(By.CLASS_NAME, "article-link").get_attribute("href")
            if post_link in links_list:
                view_post(post_link, recursion=True)
            else:
                #print("Link found, but it's not in links_list")
                #print(post_link)
                pass
        except:
            #print("Links not found")
            pass



while True:
    # Open browser
    browser = webdriver.Firefox()
    browser.get('https://dzen.ru/')
    
    # Remove download browser suggestion    
    try:
        time.sleep(5)
        browser.find_element(By.TAG_NAME, "polygon").click()
        pass
    except:
        pass

    # Go to the login form
    time.sleep(5)
    browser.find_element(By.CLASS_NAME, "base-button__regular--M").click()
    time.sleep(5)
    browser.find_element(By.CLASS_NAME, "login-content__yaButton-2A").click()


    current_login, current_password = random_account()

    # Input login
    try:
        time.sleep(5)
        browser.find_element(By.CLASS_NAME, "Textinput-Control").send_keys(current_login)
        browser.find_element(By.ID, "passp:sign-in").click()
    except:
        pass

    # Input password
    try:
        time.sleep(5)
        browser.find_element(By.ID, "passp-field-passwd").send_keys(current_password)
        browser.find_element(By.ID, "passp:sign-in").click()
    except:
        pass

    # Close greetings page
    try:
        time.sleep(5)
        browser.find_element(By.CLASS_NAME, "Button2_view_pseudo").click()
    except:
        pass


    # Go to the random post
    view_post(links_list[random.randint(0, len(links_list))-1])

    # logout
    time.sleep(random.randint(15, 60))
    browser.get('https://dzen.ru/api/auth/web/logout?retpath=https%3A%2F%2Fdzen.ru')

    # close browser
    browser.close()

    




from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import getpass
import time


def configure():
    brave_path = "/usr/bin/brave-browser"
    options = webdriver.ChromeOptions()
    options.binary_location = brave_path
    driver = webdriver.Chrome(options=options)
    return driver


def login(driver):
    login_link = driver.find_element(By.XPATH, "//a[@class='account' and contains(text(), 'Login')]")
    login_link.click()

    #sending userid & password
    send_dat = driver.find_element(By.ID, "nick")
    user_id = input("enter user id : ").strip()
    send_dat.send_keys(user_id)
    passw = driver.find_element(By.NAME, "pass")
    password1 = getpass.getpass("Enter your password: ")
    passw.send_keys(password1)
    submit_button = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Submit']")
    submit_button.click()


def t_delay(t):
    time.sleep(t)

def Print_result(driver):
    table = driver.find_element(By.CSS_SELECTOR, "table[class='summary-table left-align narrow']")
    rows = table.find_elements(By.XPATH, './/tr')
    for row in rows:
        # Extract the label and value from each row
        label = row.find_element(By.XPATH, './/td[1]').text
        value_element = row.find_element(By.XPATH, './/td[2]')
        if label == 'Status:':
            value = value_element.find_element(By.ID, 'status').text
        else:
            value = value_element.text
        print(f"{label.strip()} {value.strip()}")

def submit_sloution(problem_id, driver):
    taskid = "//a[@href='/problemset/task/" + problem_id + "']"
    problem1 = driver.find_element(By.XPATH, taskid)
    problem1.click()
    submit_id = "//a[@href='/problemset/submit/" + problem_id +  "/']"
    submit_button = driver.find_element(By.XPATH, submit_id)
    submit_button.click()
    find_button = driver.find_element(By.CSS_SELECTOR, "input[type='file'][name='file']")
    file_path = input("enter file path of the solution => ").strip()
    find_button.send_keys(file_path)
    submit_button = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Submit']")
    submit_button.click()


def simulate(driver):
    driver.get("https://cses.fi/problemset/")
    login(driver)
    problem_id = input("enter problem id =>").strip()
    submit_sloution(problem_id, driver)
    #delay 5 second
    t_delay(5)
    Print_result(driver)
    driver.close()


def main():
    try:
        driver = configure()
        simulate(driver)
        print("processed successfully")
    except:
        print("Error occured")
        driver.close()

main()



#driver.close()
#uncomment the above line if you do not want to see the submission detail
#/home/zeeshan/programming/python/cses_sol/solution1.cpp
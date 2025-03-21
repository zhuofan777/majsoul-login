import sys
from time import sleep
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

acccounts = int(len(sys.argv[1:]) / 2)
print(f'Config {acccounts} accounts')
for i in range(acccounts):
    email = sys.argv[1 + i]
    passwd = sys.argv[1 + i + acccounts]
    print('----------------------------')

    # 1. Open browser
    options = webdriver.ChromeOptions()
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.set_window_size(1000, 720)
    driver.get("https://game.maj-soul.net/1/")
    print(f'Account {i + 1} loading game...')
    sleep(20)

    # 2. Input email
    screen = driver.find_element(By.ID, 'layaCanvas')
    ActionChains(driver) \
        .move_to_element_with_offset(screen, 250, -100) \
        .click() \
        .perform()
    driver.find_element(By.NAME, 'input').send_keys(email)
    print('Input email successfully')

    # 3. Input password
    ActionChains(driver) \
        .move_to_element_with_offset(screen, 250, -50) \
        .click() \
        .perform()
    driver.find_element(By.NAME, 'input_password').send_keys(passwd)
    print('Input password successfully')

    # 4. Login
    ActionChains(driver) \
        .move_to_element_with_offset(screen, 250, 50) \
        .click() \
        .perform()
    print('Entering game...')
    sleep(20)  # Loading...

    # 5. Check if login is successful
    success = False  # Default to failed
    try:
        # Example: Check if a specific element exists after login
        driver.find_element(By.ID, 'logged_in_element')  # Replace with actual element
        success = True
        print('Login success')
    except Exception as e:
        print(f'Login failed: {e}')

    # 6. Log the result
    current_time = time.ctime()
    with open("log.txt", "a", encoding="utf-8") as log_file:
        log_file.write(f"{current_time}-{'Success' if success else 'Failed'}\n")

    driver.quit()

import sys  
import os
from time import sleep, time  
from datetime import datetime  
from selenium import webdriver  
from selenium.webdriver import ActionChains  
from selenium.webdriver.common.by import By  

# 定义日志文件路径  
log_path = os.path.join(os.getcwd(), "log.txt")  

# 记录代码开始执行的时间  
start_time = time()  

try:  
    acccounts = int(len(sys.argv[1:]) / 2)  
    print(f'Config {acccounts} accounts')  
    for i in range(acccounts):  
        email = sys.argv[1 + i]  
        passwd = sys.argv[1 + i + acccounts]  
        print('----------------------------')  

        # 1. 打开浏览器并加载游戏页面  
        options = webdriver.ChromeOptions()  
        options.add_argument("--headless=new")  
        driver = webdriver.Chrome(options=options)  
        driver.set_window_size(1000, 720)  
        driver.get("https://game.maj-soul.net/1/")  
        print(f'Account {i + 1} loading game...')  
        sleep(20)  

        # 2. 输入邮箱  
        screen = driver.find_element(By.ID, 'layaCanvas')  
        ActionChains(driver) \
            .move_to_element_with_offset(screen, 250, -100) \
            .click() \
            .perform()  
        driver.find_element(By.NAME, 'input').send_keys(email)  
        print('Input email successfully')  

        # 3. 输入密码  
        ActionChains(driver) \
            .move_to_element_with_offset(screen, 250, -50) \
            .click() \
            .perform()  
        driver.find_element(By.NAME, 'input_password').send_keys(passwd)  
        print('Input password successfully')  

        # 4. 点击登录按钮  
        ActionChains(driver) \
            .move_to_element_with_offset(screen, 250, 50) \
            .click() \
            .perform()  
        print('Entering game...')  
        sleep(20)  # 等待登录完成  
        print('Login success')  
        driver.quit()  

    # 如果未发生异常，执行成功  
    success = True  

except Exception as e:  
    # 如果发生异常，执行失败  
    success = False  
    print(f'Error occurred: {e}')  

finally:  
    # 记录代码结束执行的时间  
    end_time = time()  
    # 计算执行全部代码用时（单位：秒）  
    execution_time = end_time - start_time  
    # 获取当前时间  
    current_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  

    # 将记录写入 log.txt 文件的最后一行  
    with open("log.txt", "a", encoding="utf-8") as log_file:  
        log_file.write(f"{current_time}-{'Success' if success else 'Failed'}-{execution_time:.2f}s\n")

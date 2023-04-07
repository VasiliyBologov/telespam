from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import pyautogui


service = Service(executable_path="./selenium/chromedriver")
chrome_options = Options()
chrome_options.add_experimental_option("prefs", {'protocol_handler.excluded_schemes.hcp': False})
driver = webdriver.Chrome(service=service, chrome_options=chrome_options)

ph_list = [
    # "+37379755195",
    # "+79023909904",
    # "+37368690016",
    "+79109137406",
    "+37378228638",
    # "+37378229627",
    "+37378229628",
    # "+37378229629", - живо    й
    # "+37378229630",
    # "+37378229631",
    # "+37378229632",
    # "+37378229633",
    # "+37378229634",
]

if __name__ == '__main__':
    driver.get("https://web.telegram.org/z/")
    # driver.maximize_window()
    print("Залогинься -> нажми y")
    param = 'n'
    while not param == "y":
         param = input()

    time.sleep(2)

    for num in ph_list:

        print(f"Try find {num}")
        start_url = f"https://t.me/{num}"
        driver.get(start_url)
        time.sleep(2)
        actions = ActionChains(driver)
        pyautogui.press('enter')
        # https://web.telegram.org/z/#?tgaddr=tg://resolve?phone=37378228638
        # tg://resolve?phone=37378228638
        time.sleep(3)

        open_web_btn = driver.find_element(by=By.CLASS_NAME, value="tgme_action_web_button")
        print("open_web_btn: ", open_web_btn)
        open_web_btn.click()

        i = 1
        while driver.current_url == start_url and i < 15:
            i += 1
            time.sleep(2)

        if driver.current_url == start_url:
            print("Чтото с кнопкой!!!")
            continue
        time.sleep(3)

        print("current_url: ", driver.current_url)
        current_url = driver.current_url

        chat_id = current_url.split("#")
        print(chat_id)
        if len(chat_id) > 1:
            chat_id = chat_id[-1]
        else:
            chat_id = None
        if chat_id:
            print("chat_id: ", chat_id)
            input = driver.find_element(by=By.ID, value="editable-message-text")
            input.send_keys("Тест тест тест")
            pyautogui.press('enter')
            input.send_keys(Keys.ENTER)
        else:
            print("no user with phone: ", num)

        time.sleep(5)
        print("-----------------------")
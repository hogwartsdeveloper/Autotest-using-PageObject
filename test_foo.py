from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium import webdriver
import math




def solve_quiz_and_get_code():
    browser = webdriver.Chrome()
    browser.get("http://selenium1py.pythonanywhere.com/ru/catalogue/the-shellcoders-handbook_209/?promo=newYear")
    browser.implicitly_wait(10)
    add_to_the_basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    add_to_the_basket.click()

    alert = browser.switch_to.alert
    x = alert.text.split(" ")[2]
    answer = str(math.log(abs((12 * math.sin(float(x))))))
    alert.send_keys(answer)
    alert.accept()
    try:
        alert = browser.switch_to.alert
        alert_text = alert.text
        print(answer)
        print(f"Your code: {alert_text}")
        alert.accept()
    except NoAlertPresentException:
        print("No second alert presented")


solve_quiz_and_get_code()
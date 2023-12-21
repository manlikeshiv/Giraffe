from selenium import webdriver
from selenium.webdriver.common.by import By
from amazoncaptcha import AmazonCaptcha


BROWSERLESS_API_KEY = '2b23c0fa-76a9-49f2-bdc6-89a13d2a0926'

chrome_options = webdriver.ChromeOptions()
chrome_options.set_capability('browserless:token', BROWSERLESS_API_KEY)
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--window-size=1920,1080")

try:
    driver = webdriver.Remote(
        command_executor='https://chrome.browserless.io/webdriver',
        options=chrome_options
    )
    driver.get("https://www.amazon.co.uk/dp/B07PJBC9QL")
    #driver.save_screenshot('test.png')
    driver.implicitly_wait(2)

    captcha = AmazonCaptcha.fromdriver(driver)
    solution = captcha.solve(keep_logs=True)

    price = driver.find_element(By.XPATH, "//span[contains(@class,'a-price-whole')]").text
    print(price)

except Exception as error:
    print("There was an error: %s" % error)
finally:
    driver.quit()
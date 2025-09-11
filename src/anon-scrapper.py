import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def get_default_chrome_options():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--headless")

    return options


def handler(event, context):
    options = get_default_chrome_options()
    driver = webdriver.Chrome(options=options)

    driver.get("https://insta-stories-viewer.com/es/cristiano/")

    for i in range(5):  # repeat 5 times
        story_thingy = driver.find_element(By.CLASS_NAME, "profile__stories-counter")
        print(f"Iteration {i+1} story count {story_thingy.text} ---")
        # do something here
        time.sleep(2)  # wait 3 seconds

    driver.quit()

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": 'Hello from AWS Lambda using Python' + sys.version + '!'
    }

    return response





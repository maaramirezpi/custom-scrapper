import sys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import time
from tempfile import mkdtemp
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-dev-tools")
    options.add_argument("--no-zygote")
    options.add_argument("--headless=new")
    options.add_argument("--single-process")
    options.add_argument(f"--user-data-dir={mkdtemp()}")
    options.add_argument(f"--data-path={mkdtemp()}")
    options.add_argument(f"--disk-cache-dir={mkdtemp()}")
    options.add_argument("--remote-debugging-pipe")
    options.add_argument("--verbose")
    options.add_argument("--log-path=/tmp")

    options.binary_location = "/opt/chrome/chrome-linux64/chrome"

    service = Service(
        executable_path="/opt/chrome-driver/chromedriver-linux64/chromedriver",
        service_log_path="/tmp/chromedriver.log"
    )

    driver = webdriver.Chrome(
        service=service,
        options=options
    )

    return driver


def handler(event, context):
    driver = get_driver()

    driver.get("https://insta-stories-viewer.com/es/cristiano/")

    story_count = ""
    for i in range(5):  # repeat 5 times
        story_thingy = driver.find_element(By.CLASS_NAME, "profile__stories-counter")
        logger.info(f"Iteration {i+1} story count {story_thingy.text} ---")
        story_count = story_thingy.text
        # do something here
        time.sleep(2)  # wait 3 seconds

    driver.quit()

    response = {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": f"Hello from AWS Lambda using Python {sys.version}! Story count is {story_count}"
    }

    return response





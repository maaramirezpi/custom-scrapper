from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from tempfile import mkdtemp
import logging

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def get_default_chrome_options():
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
	#options.add_argument("--disable-gpu")

	return options

options = get_default_chrome_options()
driver = webdriver.Chrome(options=options)

driver.get("https://insta-stories-viewer.com/es/angeee.makeup/")


for i in range(5):  # repeat 5 times
	story_thingy = driver.find_element(By.CLASS_NAME, "profile__stories-counter")
	logger.info(f"Iteration {i+1} story count {story_thingy.text} --- am")
	# do something here
	time.sleep(2)  # wait 3 seconds

driver.quit()


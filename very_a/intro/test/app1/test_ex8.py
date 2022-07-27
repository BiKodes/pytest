import os
import time

from django.http import request

import pytest
from selenium import webdriver

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options as ChromeOptions

from selenium.webdriver.firefox.service import Service as FireFoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FireFoxOptions

def take_screenshot(driver, name):
    time.sleep(1)
    os.makedirs(os.path.join("screenshot", os.path.dirname(name)), exist_ok=True)
    driver.save_screenshot(os.path.join("screenshot", name))

# def test_example(live_server):
#     options = Options()
#     options.add_argument("--headless")
#     options.add_argument("--window-size=1920,1080")
#     chrome_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
#     chrome_driver.get(("%s%s" % (live_server.url, "/admin/")))
#     take_screenshot(chrome_driver, "admin/admin.png")

@pytest.fixture(params=["chrome1920", "chrome411", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome1920":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=1920,1080")
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        request.cls.browser = "Chrome1920*1080"
    if request.param == "chrome411":
        options = ChromeOptions()
        options.add_argument("--headless")
        options.add_argument("--window-size=411,823")
        web_driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        request.cls.browser = "Chrome411*823"
    if request.param == "firefox":
        options = FireFoxOptions()
        options.add_argument("--headless")
        web_driver = webdriver.Firefox(service=FireFoxService(executable_path=GeckoDriverManager().install()))
        request.cls.browser = "Firefox"
    request.cls.driver = web_driver
    yield
    web_driver.close()

@pytest.mark.usefixtures("driver_init")
class Screenshot:
    def screenshot_admin(self, live_server):
        self.driver.get(("%s%s" % (live_server.url, "/admin/")))
        take_screenshot(self.driver, "admin/" + "admin" + self.browser + ".png")
        assert "Log in | Django site admin" in self.driver.title


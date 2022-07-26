from lib2to3.pgen2 import driver
import pytest
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.service import Service as FIreFoxService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

from selenium.webdriver.chrome.options import Options

# @pytest.mark.usefixtures("chrome_driver_init")
# class Test_URL_Chrome(LiveServerTestCase):
#     def test_open_url(self):
#         self.driver.get(("%s%s" % (self.live_server_url, "/admin/")))
#         assert "Log in | Django site admin" in self.driver.title

@pytest.mark.usefixtures("driver_init")
class Test_URL_Chrome:
    def test_open_url(self, live_server):
        self.driver.get(("%s%s" % (live_server.url, "/admin/")))
        assert "Log in | Django site admin" in self.driver.title
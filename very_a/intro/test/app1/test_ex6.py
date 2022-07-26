from lib2to3.pgen2 import driver
import pytest
from django.test import LiveServerTestCase

from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.chrome.options import Options

class TestBrowser1(LiveServerTestCase):
    def test_example(self):
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
        driver.get(("%s%s" % (self.live_server_url, "/admin/")))
        assert "Log in | Django site admin" in driver.title

class TestBrowser2(LiveServerTestCase):
    def test_example2(self):
        driver = webdriver.Chrome("./chromedriver")
        driver.get(("%s%s" % (self.live_server_url, "/admin/")))
        assert "Log in | Django site admin" in driver.title

class TestBrowser3(LiveServerTestCase):
    def test_example(self):
        options = Options()
        options.add_argument("--headless")
        driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()), options=options)
        driver.get(("%s%s" % (self.live_server_url, "/admin/")))
        assert "Log in | Django site admin" in driver.title





     
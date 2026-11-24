"""Selenium yaşam döngüsü çatısı; henüz test metodu yoktur.

İlk tarayıcı testinizi bu sınıfa test_ ile başlayan bir metot olarak ekleyiniz.
Metot yalnızca self alır; pytest fixture parametresi eklemeyiniz.
Sunucuyu ayrı terminalde başlatınız. pytest sunucuyu kendiliğinden açmaz.
"""
import os
import unittest

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait


@pytest.mark.browser
class StudentSearchFunctionalTests(unittest.TestCase):
    def setUp(self):
        options = webdriver.ChromeOptions()
        if os.environ.get("HEADLESS", "1") == "1":
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1280,900")
        options.add_argument("--disable-dev-shm-usage")
        if os.environ.get("CHROME_NO_SANDBOX") == "1":
            options.add_argument("--no-sandbox")
        if os.environ.get("CHROME_BINARY"):
            options.binary_location = os.environ["CHROME_BINARY"]
        service = (
            Service(executable_path=os.environ["CHROMEDRIVER"])
            if os.environ.get("CHROMEDRIVER")
            else Service()
        )
        self.browser = webdriver.Chrome(service=service, options=options)
        self.browser.set_page_load_timeout(10)
        self.wait = WebDriverWait(self.browser, 5)
        self.base_url = os.environ.get("BASE_URL", "http://127.0.0.1:8000")

    def tearDown(self):
        if hasattr(self, "browser"):
            self.browser.quit()

    # TODO: S1 için ilk test metodunuzu ekleyiniz; sonra akışları genişletiniz.
    # self.browser, self.wait ve self.base_url hazırlıkta tanımlanır.

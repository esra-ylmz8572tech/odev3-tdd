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
from selenium.webdriver.common.by import By
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

    def test_s1_initial_page(self):
        self.browser.get(f"{self.base_url}/")

        heading = self.browser.find_element(By.TAG_NAME, "h1")
        self.assertIn("Öğrenci Sorgulama", heading.text)

        student_input = self.browser.find_element(By.ID, "student-no")
        self.assertEqual(student_input.get_attribute("name"), "student_no")
        self.assertEqual(student_input.get_attribute("type"), "text")
        self.assertIsNone(student_input.get_attribute("required"))

        self.browser.find_element(By.ID, "search-button")

        message = self.browser.find_element(By.ID, "search-message")
        self.assertEqual(message.text.strip(), "Öğrenci numarası giriniz.")

        result_cards = self.browser.find_elements(By.ID, "student-result")
        self.assertEqual(len(result_cards), 0)

    def test_s2_search_ada_deniz_flow(self):
        self.browser.get(f"{self.base_url}/")

        student_input = self.browser.find_element(By.ID, "student-no")
        student_input.clear()
        student_input.send_keys("20260001")
        self.browser.find_element(By.ID, "search-button").click()

        self.wait.until(lambda d: "student_no=20260001" in d.current_url)

        message = self.browser.find_element(By.ID, "search-message")
        self.assertEqual(message.text.strip(), "Öğrenci bulundu.")

        self.browser.find_element(By.ID, "student-result")
        result_no = self.browser.find_element(By.ID, "result-student-no")
        result_name = self.browser.find_element(By.ID, "result-full-name")
        self.assertEqual(result_no.text.strip(), "20260001")
        self.assertEqual(result_name.text.strip(), "Ada Deniz")
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


@pytest.fixture
def browser():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_demoqa_form_corrected(browser):
    browser.get("https://demoqa.com/text-box")

    # Llenar campos
    browser.find_element(By.ID, "userName").send_keys("Alejandro QA")
    browser.find_element(By.ID, "userEmail").send_keys("alejandro@example.com")
    browser.find_element(By.ID, "currentAddress").send_keys("Costa Rica")
    browser.find_element(By.ID, "permanentAddress").send_keys("Test Address")

    # Esperar hasta que el botón sea clicable antes de hacer clic
    wait = WebDriverWait(browser, 10)  # Espera un máximo de 10 segundos
    submit_button = wait.until(EC.element_to_be_clickable((By.ID, "submit")))
    submit_button.click()

    # Validar resultado
    output_element = browser.find_element(By.ID, "output")
    output_text = output_element.text

    assert "Alejandro QA" in output_text
    assert "alejandro@example.com" in output_text
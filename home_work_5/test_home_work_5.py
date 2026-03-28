from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


def test_iframe(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/iframes.html")

    wait.until(EC.frame_to_be_available_and_switch_to_it((By.ID, "my-iframe")))
    expected_text = "semper posuere integer et senectus justo curabitur."
    wait.until(EC.text_to_be_present_in_element((By.TAG_NAME, "body"), expected_text))
    body=driver.find_element(By.TAG_NAME, "body")
    assert expected_text in body.text, "Text not found in iframe"


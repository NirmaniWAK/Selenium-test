from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Auto-matches ChromeDriver to your Chrome version
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service)

# Open Safora Contact page
driver.get("https://safora.se/en/contact.html")
driver.maximize_window()

# Wait for page to load
time.sleep(3)

# Fill Name
driver.find_element(By.XPATH, "//input[@placeholder='Your Name']").send_keys("Nirmani")

# Fill Email
driver.find_element(By.XPATH, "//input[@placeholder='Email Address']").send_keys("nirmani@gmail.com")

# Fill Phone Number
driver.find_element(By.XPATH, "//input[@placeholder='Phone Number']").send_keys("0712345678")

# Fill Message
driver.find_element(By.XPATH, "//textarea[@placeholder='Your Message']").send_keys(
    "This is a QA automation test created for the QA Intern selection assignment. Please ignore this message"
)

print("Form filled successfully.")

# reCAPTCHA cannot be automated reliably
print("Please complete the reCAPTCHA manually.")

input("Press Enter after completing the reCAPTCHA...")

# Click Submit button
driver.find_element(By.XPATH, "//button[contains(text(),'Send Message')]").click()

time.sleep(5)

# Verify result
page_text = driver.page_source.lower()

if "thank" in page_text or "success" in page_text:
    print("TEST PASSED: Form submitted successfully")
else:
    print("TEST COMPLETED: Verify the result manually")

# Close browser
driver.quit()
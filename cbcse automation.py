from selenium import webdriver
from selenium.webdriver.common.by import By
import time  # For adding delay between iterations
from selenium.webdriver.support.ui import Select  

# Create a new instance of the browser
driver = webdriver.Chrome()  # Ensure you have the ChromeDriver installed and in PATH

# Open the login page of the website
driver.get("https://cbseit.in/cbse/web/regn/login.aspx")

# Find the user ID and password fields and enter the credentials
user_id_field = driver.find_element(By.ID, "MainContent_affno")  
password_field = driver.find_element(By.ID, "MainContent_pwd")

# Enter the credentials
user_id_field.send_keys("2750121")
password_field.send_keys("Newqadipur@555")

# Wait for the user to fill in the CAPTCHA and press Enter
input("Please complete the CAPTCHA and press Enter to continue...")

# Navigate to the next page after CAPTCHA
driver.get("https://cbseit.in/cbse/web/regn/regaddc.aspx")

# Find the text box by its ID where you want to enter values
# text_box = driver.find_element(By.ID, "MainContent_slno2")

# submit_button = driver.find_element(By.ID, "MainContent_btnFind")  # Adjust the button ID

# Loop to enter values in the text box
for i in range(124,185):  # Change the range as per your requirement
    submit_button = driver.find_element(By.ID, "MainContent_btnFind")  # Adjust the button ID
    text_box = driver.find_element(By.ID, "MainContent_slno2")
    # Clear the previous value (if any)
    text_box.clear()
    
    # Enter the next value (e.g., a number)
    text_box.send_keys('00'+str(i))  # You can customize the values here
    
    # Optional: Add a small delay to observe the changes (remove if not needed)
    time.sleep(1)  # 1-second delay to see the value being entered
    
    # Click the button after entering the number
    submit_button.click()

    
    # Optional: Add a delay after clicking (if the next step requires loading)
    time.sleep(2)  #

    dropdown = Select(driver.find_element(By.ID, "MainContent_sub6"))  # Replace with the actual ID of the dropdown
    
    # Select an option from the dropdown
    dropdown.select_by_index(0)  # Change index as needed, or use select_by_visible_text or select_by_value

    dropdown = Select(driver.find_element(By.ID, "MainContent_med6"))  # Replace with the actual ID of the dropdown
    
    # Select an option from the dropdown
    dropdown.select_by_index(2)  # Change index as need
    
    # Optional: Add a delay to observe the dropdown selection
    time.sleep(1)  # 1-second delay to see the dropdown selection
    update_button = driver.find_element(By.ID, "MainContent_btnSave")  # Adjust the button ID
    update_button.click()
    time.sleep(1)

    driver.get("https://cbseit.in/cbse/web/regn/regaddc.aspx")
    time.sleep(1)

    #MainContent_btnSave

# Keep the browser open for further actions
input("Press Enter to close the browser when done...")

# Close the browser manually when ready
driver.quit()

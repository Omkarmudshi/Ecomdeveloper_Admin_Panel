#login page
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service


class Loginpage:
    textbox_username_id="input-username"
    textbox_password_id = "input-password"
    button_login_XPATH="//button[normalize-space()='Login']"
    link_logout_XPATH="//span[normalize-space()='Logout']"

    def __init__(self,driver):
        self.driver=driver

    def setUserName(self,username):
        self.driver.find_element(By.ID, self.textbox_username_id).clear()
        self.driver.find_element(By.ID,self.textbox_username_id).send_keys(username)

    def setPassword(self,password):
        self.driver.find_element(By.ID, self.textbox_password_id).clear()
        self.driver.find_element(By.ID,self.textbox_password_id).send_keys(password)

    def clickLoginbtn(self):
        self.driver.find_element(By.XPATH,self.button_login_XPATH).click()

    def clickLogoutlink(self):
        self.driver.find_element(By.XPATH,self.link_logout_XPATH).click()

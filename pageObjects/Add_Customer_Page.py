#Add customer page
from selenium.webdriver.common.by import By
import time
class AddCustomer:
    lnkCustomer_manu_xpath="//a[@class='parent collapsed'][normalize-space()='Customers']"
    linCustomer_sub_menu_xpath="//ul[@id='collapse9']//a[contains(text(),'Customers')]"
    addcustomer_btn_xpath="//div[@class='pull-right']//a[@class='btn btn-primary']"
    drop_customerGroup_select_xpath="//select[@id='input-customer-group']"
    drop_customerGroup_select_item_whole_xpath="//option[text()='Wholesaler']"
    txt_firstname_xpath="//input[@id='input-firstname']"
    txt_lastname_xpath="//input[@id='input-lastname']"
    txt_email_xpath="//input[@id='input-email']"
    txt_talephone_xpath="//input[@id='input-telephone']"
    txt_password_xpath="//input[@id='input-password']"
    txt_confirm_pass_xpath="//input[@id='input-confirm']"
    drop_newslatter_select_xpath="//select[@id='input-newsletter']"
    drop_newslatter_select_item_enb_xpath="//select[@id='input-newsletter']/option[text()='Enabled']"
    drop_newslatter_select_item_dis_xpath="//select[@id='input-newsletter']/option[text()='Disabled']"
    drop_status_select_xpath="//select[@id='input-status']"
    drop_status_select_item_enb_xpath="//select[@id='input-status']/option[text()='Enabled']"
    drop_status_select_item_dis_xpath="//select[@id='input-status']/option[text()='Disabled']"
    drop_safe_select_xpath="//select[@id='input-safe']"
    drop_safe_select_item_no_xpath="//select[@id='input-safe']/option[text()='No']"
    drop_safe_select_item_yes_xpath="//select[@id='input-safe']/option[text()='Yes']"
    btn_save_xpath="//button[@type='submit']"

    def __init__(self,driver):
        self.driver=driver

    def clickOnCustomerMenu(self):
        self.driver.find_element(By.XPATH,self.lnkCustomer_manu_xpath).click()

    def clickOnCustomerMenuItem(self):
        self.driver.find_element(By.XPATH,self.linCustomer_sub_menu_xpath).click()

    def addNewCustomer(self):
        self.driver.find_element(By.XPATH,self.addcustomer_btn_xpath).click()

    def setCustomerGrp(self,group):
        self.driver.find_element(By.XPATH,self.drop_customerGroup_select_xpath).click()
        time.sleep(2)
        if group == "Default":
            pass
        else:
            self.driver.find_element(By.XPATH,self.drop_customerGroup_select_item_whole_xpath).click()

    def firstName(self,firstname):
        self.driver.find_element(By.XPATH,self.txt_firstname_xpath).send_keys(firstname)
    
    def lastName(self,lastname):
        self.driver.find_element(By.XPATH,self.txt_lastname_xpath).send_keys(lastname)

    def userEmail(self,email):
        self.driver.find_element(By.XPATH,self.txt_email_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_email_xpath).send_keys(email)

    def userTelephone(self,telephone):
        self.driver.find_element(By.XPATH,self.txt_talephone_xpath).send_keys(telephone)

    def userPassword(self,password):
        self.driver.find_element(By.XPATH,self.txt_password_xpath).clear()
        self.driver.find_element(By.XPATH,self.txt_password_xpath).send_keys(password)

    def confirmPassword(self,confPassword):
        self.driver.find_element(By.XPATH,self.txt_confirm_pass_xpath).send_keys(confPassword)

    def newslatter(self,option):
        self.driver.find_element(By.XPATH,self.drop_newslatter_select_xpath).click()
        time.sleep(1)
        if option == "Enabled":
            self.driver.find_element(By.XPATH,self.drop_newslatter_select_item_enb_xpath).click()
        elif option == "Disabled":
            self.driver.find_element(By.XPATH,self.drop_newslatter_select_item_dis_xpath).click()
    
    def userStatus(self,status):
        self.driver.find_element(By.XPATH,self.drop_status_select_xpath).click()
        time.sleep(1)
        if status == "Enabled":
            self.driver.find_element(By.XPATH,self.drop_status_select_item_enb_xpath).click()
        elif status == "Disabled":
            self.driver.find_element(By.XPATH,self.drop_status_select_item_dis_xpath).click()

    def userSafe(self,option):
        self.driver.find_element(By.XPATH,self.drop_safe_select_xpath).click()
        time.sleep(1)
        if option == "Yes":
            self.driver.find_element(By.XPATH,self.drop_safe_select_item_yes_xpath).click()
        elif option == "No":
            self.driver.find_element(By.XPATH,self.drop_safe_select_item_no_xpath).click()

    def savebtn(self):
        self.driver.find_element(By.XPATH,self.btn_save_xpath).click()

        
    
    
    
    



import pytest
from selenium import webdriver
from Configurations.conftest import setup
from pageObjects.Add_Customer_Page import AddCustomer
from pageObjects.Login_page import Loginpage
from utilities.readProperties import ReadConfig
import time
from utilities.customLogger import LogGen
import random
import string
from selenium .webdriver.common.by import By

class Test_003__addcustomer:

    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()
    logger=LogGen.logger()
    
    @pytest.mark.sanity
    def test_add_customer(self,setup):
        self.logger.info("****************** Test_003_Add_Customer **********************")
        self.driver=setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginbtn()
        self.logger.info("****************** Login Sucesfull **********************")
        self.addcust=AddCustomer(self.driver)
        self.addcust.clickOnCustomerMenu()
        time.sleep(2)
        self.addcust.clickOnCustomerMenuItem()
        self.addcust.addNewCustomer()
        self.addcust.setCustomerGrp("Wholesaler")
        self.addcust.firstName("Omkar")
        self.addcust.lastName("Mudshi")

        self.email= random_generator() + "@gmail.com"
        self.addcust.userEmail(self.email)

        self.addcust.userTelephone("1234567890")

        self.addcust.userPassword("abcd@1234")
        self.addcust.confirmPassword("abcd@1234")
        self.addcust.newslatter("Enabled")
        self.addcust.userStatus("Enabled")
        self.addcust.userSafe("Yes")

        time.sleep(5)
        self.addcust.savebtn()
        self.msg=self.driver.find_element(By.TAG_NAME,"body").text
        print(self.msg)
        if 'Warning: You do not have permission to modify customers!' in self.msg:
            self.logger.info("****************** Add_Customer_Sucessfull The test is passed **********************")
            assert True == True
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_addcustomer.png")
            assert True == False
            ("****************** Add_Customer_Failed The test is Failed **********************")

        self.driver.quit()

def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
        return ''.join(random.choice(chars) for x in range(size))




    

        
    # def random_tel_gen(size=10, chars=str.digits):
    #     return random.choice(chars) for x in range(size)




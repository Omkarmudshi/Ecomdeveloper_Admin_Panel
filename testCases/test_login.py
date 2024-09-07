#creating test case for login page

import pytest
from selenium import  webdriver

from Configurations.conftest import setup
from pageObjects.Login_page import Loginpage
from utilities.readProperties import ReadConfig
import time
from utilities.customLogger import LogGen
class Test_001_login:

    baseURL=ReadConfig.getApplicationURL()
    username=ReadConfig.getUsername()
    password=ReadConfig.getPassword()

    logger=LogGen.logger()

    @pytest.mark.regression
    def test_homePageTitle(self,setup):

        self.logger.info("********** Varifying Home Page title************")
        self.driver=setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Administration":
            assert True
            self.driver.close()
            self.logger.info("********** Home Page titile Test is pass ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_homePageTitle.png")
            self.driver.close()
            self.logger.error("********** Home Page titile Test is failed ************")
            assert False

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_login(self,setup):
        self.logger.info("********** Test_002_Login************")
        self.logger.info("********** Varifying Login Test ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Loginpage(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLoginbtn()
        act_title=self.driver.title
        if act_title=="Dashboard":
            assert True
            self.driver.close()
            self.logger.info("********** login Test is pass ************")
        else:
            self.driver.save_screenshot(".\\Screenshots\\"+"test_login.png")
            self.driver.close()
            self.logger.error("********** login Test is failed ************")
            assert False



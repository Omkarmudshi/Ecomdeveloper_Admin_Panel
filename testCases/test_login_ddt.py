#creating test case for login page

import pytest
from selenium import  webdriver

from Configurations.conftest import setup
from pageObjects.Login_page import Loginpage
from utilities.readProperties import ReadConfig
import time
from utilities.customLogger import LogGen
from utilities import XLU

class Test_002_DDT_login:

    baseURL=ReadConfig.getApplicationURL()
    path=".//TestData/LoginData.xlsx"

    logger=LogGen.logger()

    
    @pytest.mark.regression
    def test_login_ddt(self,setup):
        self.logger.info("********** Test_002_DDT_Login************")
        self.logger.info("********** Varifying Login DDt Test ************")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.driver.maximize_window()

        self.lp=Loginpage(self.driver)

        self.rows=XLU.getRowCount(self.path,"Sheet1")
        print("no of row in excel",self.rows)
        lst_status=[]
        for r in range(2,self.rows+2):

            self.user=XLU.readData(self.path,"Sheet1",r,1)
            self.password=XLU.readData(self.path,"Sheet1",r,2)
            self.exp=XLU.readData(self.path,"Sheet1",r,3)

            self.lp.setUserName(self.user)
            self.lp.setPassword(self.password)
            self.lp.clickLoginbtn()
            time.sleep(3)

            act_title=self.driver.title
            exp_title="Dashboard"

            if act_title==exp_title:
                if self.exp=="pass":
                    self.logger.info("Test Is Pass")
                    self.lp.clickLogoutlink()
                    lst_status.append("Pass")
                elif self.exp=="fail":
                    self.logger.info("Test Is Failed")
                    self.lp.clickLogoutlink()
                    lst_status.append("Fail")
            elif act_title != exp_title:
                if self.exp=="pass":
                    self.logger.info("Test Is Failed")
                    lst_status.append("Fail")
                elif self.exp=="fail":
                    self.logger.info("Test is Passed")
                    lst_status.append("pass")

        if "fail" not in lst_status:
            self.logger.info("Login DDT Test is Passed")
            self.driver.close()
            assert True
        else:
            self.logger.info("Login DDT Test is Failed")
            self.driver.close()
            assert False




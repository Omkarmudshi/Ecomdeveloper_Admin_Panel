from urllib import request
import pytest
from selenium import webdriver
# import undetected_chromedriver as uc
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service as FS
from selenium.webdriver.edge.service import Service as ES



@pytest.fixture()
def setup():
    chrome_options=Options()
    chrome_options.add_experimental_option("detach",True)
    serv_obj=Service(r"C:\Test_Drivers\chromedriver-win32\chromedriver-win32\chromedriver.exe")
    driver=webdriver.Chrome(service=serv_obj,options=chrome_options)
    return driver

#it is hook for adding enviroment into html report

# Hook to configure the pytest environment
def pytest_configure(config):
    if config.pluginmanager.hasplugin('html'):
        # Only modify metadata if the pytest-html plugin is loaded
        config._metadata = getattr(config, '_metadata', {})
        config._metadata['Project_Name'] = "e-commerce site admin panel"
        config._metadata['Module'] = "customer"
        config._metadata['Tester'] = 'Omkar Mudshi'

# Remove specific environment information from the report
@pytest.hookimpl(tryfirst=True)
def pytest_metadata(metadata):
    metadata.pop("JAVA_HOME", None)
    metadata.pop("Plugins", None)



# @pytest.fixture()
# def setup(browser):
#     if browser == "c":
#         chrome_options=Options()
#         chrome_options.add_experimental_option("detach",True)
#         serv_obj=Service(r"C:\Test_Drivers\chromedriver-win32\chromedriver-win32\chromedriver.exe")
#         driver=webdriver.Chrome(service=serv_obj,options=chrome_options)
        
#     elif browser == "f":
#         # firefox_options=FO()
#         # firefox_options.add_argument("--headless")
#         serv_obj=FS(r"C:\Test_Drivers\geckodriver-v0.35.0-win64\geckodriver.exe")
#         driver=webdriver.Firefox(service=serv_obj)
        
#     else:
#         # serv_obj=ES(r"C:\Test_Drivers\edgedriver_win64\msedgedriver.exe")
#         # driver=webdriver.Edge(service=serv_obj)
#         # return driver
#         driver=webdriver.Ie()
#     return driver

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")

# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")

# def pytest_addoption(parser):
#     parser.addoption("--browser", action="store", default="chrome", help="Browser to run tests")

# @pytest.fixture()
# def browser(request):
#     return request.config.getoption("--browser")



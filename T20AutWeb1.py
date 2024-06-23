from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver import ActionChains, Keys
from time import sleep
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.firefox.options import Options

#setting browser preference to download files without any popups
ff_options = Options()
ff_profile = webdriver.FirefoxProfile()

ff_profile.set_preference("browser.download.folderList", 2)
ff_profile.set_preference("browser.download.manager.showWhenStarting", False)
ff_profile.set_preference("browser.download.dir", "D:\\VinoLearning\\PySelProject")
ff_profile.set_preference("browser.helperApps.neverAsk.saveToDisk", "application/pdf")
ff_profile.set_preference("pdfjs.disabled", True)
ff_options.profile = ff_profile

class labour:
    #locators for web elements needed for the task
    documents_locator = "/html/body/nav/div/div/div/ul/li[7]/a"
    month_report_locator = "//a[text()='Monthly Progress Report']"
    download_link_locator = "//div//table[@role = 'Presentation']/tbody/tr[2]/td[2]/a[text()='Download(139.61 KB)']"
    #download_button_locator = "//button[@id='download']"
    download_button_locator = "//*[@id='download']"
    def __init__(self,url):
        self.url = url
        # initializing driver with firefox options
        self.driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),options=ff_options)
    # method to launch home page
    def pageLaunch(self):
        try:
            self.driver.maximize_window()
            self.driver.get(self.url)
            sleep(3)
            homePage_Handle = self.driver.current_window_handle
            print("Homepage window handle is: ",homePage_Handle)
            print(self.driver.current_url)
            return True
        except:
            print("Error launching the page")
            return False
    #method to hover over documents link
    def menuAccess(self):
        try:
            doc_element = self.driver.find_element(by=By.XPATH,value=self.documents_locator)
            actions = ActionChains(self.driver)
            actions.move_to_element(doc_element).perform()
            sleep(2)
            return True
        except:
            print("Error launching the page")
            return False

    #method to click monthly reports link
    def monthlyReportPage(self):
        try:
            self.driver.find_element(by=By.XPATH,value=self.month_report_locator).click()
            sleep(2)
            return True
        except:
            print("Error launching the page")
            return False

    #method to click download link of the respective report
    def access_monthly_report(self):
        try:
            self.driver.find_element(by=By.XPATH,value=self.download_link_locator).click()
            sleep(2)
            alert = Alert(self.driver)
            print(alert.text)
            alert.accept()
            sleep(2)
            return True
        except:
            print("Error launching the page")
            return False

     #method to download monthly report
    def download_report(self):
        try:
            homePage_handle = self.driver.current_window_handle
            all_window_handle = self.driver.window_handles
            for windows in all_window_handle:
                if windows != homePage_handle:
                    self.driver.switch_to.window(windows)
                    sleep(2)
                    self.driver.find_element(by=By.XPATH, value=self.download_button_locator).click()
                    break
            return True
        except:
            print("Error launching the page")
            return False

    def shutdown(self):
        try:
            self.driver.quit()
            return None
        except:
            print("Error")
            return False

if __name__ == "__main__":
    lg = labour("https://labour.gov.in/")
    lg.pageLaunch()
    lg.menuAccess()
    lg.monthlyReportPage()
    lg.access_monthly_report()
    lg.download_report()
    lg.shutdown()
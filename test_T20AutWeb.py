from T20AutWeb import coWin
import pytest

url = "https://www.cowin.gov.in/"
cwPage = coWin(url)

def test_webPageLaunch():
    assert cwPage.PagesLaunch() == True
    print("Able to access the web pages successfully")

def test_driver_quit():
    assert cwPage.shutdown() == None
    print("Web page automation is completed")
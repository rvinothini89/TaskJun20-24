from T20AutWeb1 import labour
import pytest

url = "https://labour.gov.in"
lgPage = labour(url)

def test_homePage():
    assert lgPage.pageLaunch() == True
    print("Homepage launched successfully")

def test_docOption_hover():
    assert lgPage.menuAccess() == True
    print("Hovered over documents link successfully")

def test_monthlyReport_Access():
    assert lgPage.monthlyReportPage() == True
    print("Monthly report page is clicked")

def test_download_link():
    assert lgPage.access_monthly_report() == True
    print("Download link of document is clicked successfully")

def test_download_file():
    assert lgPage.download_report() == True
    print("File is downloaded successfully")

def test_shutdown():
    assert lgPage.shutdown() == None
    print("Web automation completed successfully")
# Separate file for class with instance methods
# That will be responsible for filtration

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class EbayFiltration:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def format(self, *format_category):
        format_rect_ul = self.driver.find_element(By.XPATH, '//*[@id="x-refine__group_1__0"]/ul')
        for category in format_category:
            format_child_elements = format_rect_ul.find_elements(By.XPATH, f'//*[@aria-label="{category}"]')
            if len(format_child_elements) > 0:
                format_child_elements[0].click()
                format_rect_ul = self.driver.find_element(By.XPATH, '//*[@id="x-refine__group_1__0"]/ul')
    """
    Without re-finding the format_rect_ul element so basically code like this:
    
    def format(self, *format_category):
    format_rect_ul = self.driver.find_element(By.XPATH, '//*[@id="x-refine__group_1__0"]/ul')
    for category in format_category:
        format_child_element = format_rect_ul.find_element(By.XPATH, f'//span[input[@aria-label="{format_category}"]]')
        format_child_element.click()
        
    Compiler throws 'StaleElementReferenceException':
    selenium.common.exceptions.StaleElementReferenceException:
    Message: stale element reference: element is not attached to the page document 
        
    The 'StaleElementReferenceException' usually occurs when the DOM changes on a page and the previously 
    found element becomes stale. In your case, this could be happening because the page is refreshing or
    changing after clicking the first checkbox.

    To solve this issue, try re-finding the format_rect_ul element after each click. 
    """

    def condition(self, *condition_category):
        format_rect_ul = self.driver.find_element(By.XPATH, '//*[@id="x-refine__group__2"]/ul')
        for category in condition_category:
            format_child_elements = format_rect_ul.find_elements(By.XPATH, f'//*[@aria-label="{category}"]')
            if len(format_child_elements) > 0:
                format_child_elements[0].click()
                format_rect_ul = self.driver.find_element(By.XPATH, '//*[@id="x-refine__group__2"]/ul')






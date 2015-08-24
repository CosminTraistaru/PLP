from selenium import webdriver

URL = 'http://www.entrepreneur.com/'
links = []
driver = webdriver.PhantomJS()

driver.get(URL)
elements = driver.find_elements_by_css_selector('a')

for e in elements:
    links.append(e.get_attribute('href'))

driver.quit()

print links
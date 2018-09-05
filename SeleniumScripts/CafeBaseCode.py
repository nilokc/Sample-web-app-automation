import time, datetime,unittest,logging
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from SeleniumScripts.list_elements import references
from selenium.webdriver.common.keys import Keys


class App_Otomasyon(unittest.TestCase):


        logger = logging.getLogger('Keep Logs')
        logger.setLevel(logging.DEBUG)

        ch = logging.StreamHandler()
        ch.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        ch.setFormatter(formatter)
        logger.addHandler(ch)
        logging.basicConfig(filename='kayitlar.log', filemode='w', level=logging.DEBUG)

        logger.debug('debug message')
        logger.info('info message')
        logger.warn('warn message')
        logger.error('error message')
        logger.critical('critical message')

        def setUp(self):
            self.driver = self.browser("firefox")
            self.driver.set_page_load_timeout(30)
            self.driver.maximize_window()
            self.driver.implicitly_wait(30)

        def browser(self,browser):
            if browser == 'chrome':
                return webdriver.Chrome()
            elif browser == 'firefox':
                return webdriver.Firefox()
            elif browser == 'ie':
                return webdriver.Ie()
            elif browser == 'safari':
                return webdriver.Safari()
            elif browser == 'opera':
                return webdriver.Opera()
            elif browser == 'edge':
                return webdriver.Edge()

        def value(self,reference):
            return references[reference][0]

        def find_element(self, xpath):
            xpath_value = self.value(xpath)
            return self.driver.find_element_by_xpath(xpath_value)

        def login(self):
            self.driver.get(self.value("login_page"))
            self.find_element("password_textbox").send_keys(self.value("password"))
            self.find_element("Username_textbox").send_keys(self.value("username"))
            self.find_element("login_button").click()
            self.driver.get_screenshot_as_file("ss.png")

        def get_text(self,element):
                        return self.driver.find_element_by_xpath(element).text

        def double_click(self,element):
            action = ActionChains(self.driver)
            action.double_click(self.find_element(element)).perform()

        def display_users(self):
                self.login()
                WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.value("user_to_display"))))
                self.double_click("user_to_display")
                WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.XPATH, self.value("back_button"))))
                disp_firstname = self.find_element("firstname_textbox").get_attribute('value')
                disp_lastname = self.find_element("lastname_textbox").get_attribute('value')
                references["disp_full_name"]=disp_firstname+" "+disp_lastname
                self.find_element("back_button").click()

        def add_new_user(self):
            self.login()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH,self.value("create_button"))))
            self.find_element("create_button").click()
            self.find_element("firstname_textbox").send_keys(self.value("new_firstname"))
            self.find_element("lastname_textbox").send_keys(self.value("new_lastname"))
            self.find_element("start_day_textbox").send_keys(self.value("new_date"))
            self.find_element("email_textbox").send_keys(self.value("new_email"))
            self.find_element("add_button").click()
            references["new_full_name"] = self.value("new_firstname") + " " + self.value("new_lastname")

        def match_employee(self,employee_name):
            time.sleep(5)
            return(employee_name in self.get_text(self.value("employee_list")))

        def edit_user(self):
            self.login()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.value("user_to_edit"))))
            self.find_element("user_to_edit").click()
            self.find_element("edit_button").click()
            self.find_element("firstname_textbox").send_keys(Keys.CONTROL+"a")
            self.find_element("firstname_textbox").send_keys(self.value("edit_name"))
            self.find_element("lastname_textbox").send_keys(Keys.CONTROL + "a")
            self.find_element("lastname_textbox").send_keys(self.value("edit_surname"))
            references["edit_full_name"] = self.value("edit_name")+" "+self.value("edit_surname")
            self.find_element("update_button").click()

        def delete_user(self):
            self.login()
            WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, self.value("user_to_delete"))))
            references["delete_full_name"]=self.get_text(self.value("user_to_delete"))
            self.find_element("user_to_delete").click()
            self.find_element("delete_from_form_table").click()
            self.driver.switch_to.alert.accept()

        def logout(self):
            self.login()
            time.sleep(5)
            self.find_element("logout_button").click()
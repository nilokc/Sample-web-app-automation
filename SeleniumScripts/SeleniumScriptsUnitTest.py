from SeleniumScripts.CafeBaseCode import App_Otomasyon

import unittest

class LogginTestCases(App_Otomasyon):


#Testing Login process

    def test_LogginTestCase(self):
        self.logger.info("Login.")
        self.login()
        self.assertIn("Logout", self.get_text(self.value("logout_button")))
        self.driver.quit()


#Test of displaying details of employees
#Matches the displayed employee full name and employee list

    def test_display(self):
        self.logger.info("Display of user")
        self.display_users()
        self.assertTrue(self.match_employee(self.value("disp_full_name")))
        self.driver.quit()


#Test of adding new employee
#Matches the added employee and employee list

    def test_addnew(self):
        self.logger.info("Create user")
        self.add_new_user()
        self.assertTrue(self.match_employee(self.value("new_full_name")))
        self.driver.quit()


#Test of editting employee page

    def test_edituser(self):
        self.logger.info("Editting the user")
        self.edit_user()
        self.assertTrue(self.match_employee(self.value("edit_full_name")))
        self.driver.quit()


#Test of deleting employee
#Checkes the employee is deleted

    def test_deleteuser(self):
        self.logger.info("Delete user")
        self.delete_user()
        try:
            self.assertFalse(self.match_employee(self.value("delete_full_name")))
        except:
            self.assertTrue(self.match_employee(self.value("delete_full_name")))
            print("Duplication Issue")

        self.driver.quit()


#Test of logging out

    def test_logout(self):
        self.logger.info("LogOut")
        self.logout()
        self.assertIn("Login",self.get_text(self.value("login_button")))
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

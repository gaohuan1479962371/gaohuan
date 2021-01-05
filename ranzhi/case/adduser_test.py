from page.adduser_page import AddUser
from base.util import BoxDriver

class AddUserTest:

    def test(self):
        driver = BoxDriver()
        # LoginPage(driver).login()
        # AddUser(driver).add_user()
        add = AddUser(driver)
        add.login()
        add.add_user()
        

if __name__ == "__main__":
    AddUserTest().test()
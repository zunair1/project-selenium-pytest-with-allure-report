import allure


from Tests.test_base import basetest
from pages.SignUpPage import SignUpPageClass
from config.config import TestData
@allure.severity(allure.severity_level.MINOR)
@allure.feature("this is login test")
class Test_doSignUpTest(basetest):
    @allure.step("this login")
    def test_do_SignUp(self):
        driver = self.driver

        SignUpPageObj = SignUpPageClass(driver)
        SignUpPageObj.clickSignUpButtonOnHomePage()
        SignUpPageObj.setSignUpUserEmail(TestData.signUpEmail)
        SignUpPageObj.setSignUpPassword(TestData.SIGN_UP_PASSWORD)
        SignUpPageObj.setSignUpConfirmPassword(TestData.SIGN_UP_CONFIRM_PASSWORD)
        SignUpPageObj.clickSignUp()


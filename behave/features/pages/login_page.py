from behave.features.utils.constants import *

class LoginPage():

    USERNAME_FIELD = "[data-test=\"username\"]"
    PASSWORD_FIELD = "[data-test=\"password\"]"
    LOGIN_BUTTON = "[data-test=\"login-button\"]"
    def login_standard_user(self, context):
        try:
            # Fill username field
            page = context.page
            page.locator("textbox", name=self.USERNAME_FIELD).click
            page.locator("textbox", name=self.USERNAME_FIELD).fill(self.STANDARD_USER)
            # Fill password field
            page = context.page
            page.locator("textbox", name=self.PASSWORD_FIELD).click
            page.locator("textbox", name=self.PASSWORD_FIELD).fill(self.MASTER_PASSWORD)
            # Press login button
            page.locator("button", name=self.LOGIN_BUTTON).click()

        except Exception as e:
            print(f"login failed for {self.STANDARD_USER} --> {e}")

    def login_locked_user(self, context):
        try:
            # Fill username field
            page = context.page
            page.locator("textbox", name=self.USERNAME_FIELD).click
            page.locator("textbox", name=self.USERNAME_FIELD).fill(self.LOCKED_OUT_USER)
            # Fill password field
            page = context.page
            page.locator("textbox", name=self.PASSWORD_FIELD).click
            page.locator("textbox", name=self.PASSWORD_FIELD).fill(self.MASTER_PASSWORD)
            # Press login button
            page.locator("button", name=self.LOGIN_BUTTON).click()

        except Exception as e:
            print(f"login failed for {self.LOCKED_OUT_USER} --> {e}")

    def login_problem_user(self, context):
        try:
            # Fill username field
            page = context.page
            page.locator("textbox", name=self.USERNAME_FIELD).click
            page.locator("textbox", name=self.USERNAME_FIELD).fill(self.PROBLEM_USER)
            # Fill password field
            page = context.page
            page.locator("textbox", name=self.PASSWORD_FIELD).click
            page.locator("textbox", name=self.PASSWORD_FIELD).fill(self.MASTER_PASSWORD)
            # Press login button
            page.locator("button", name=self.LOGIN_BUTTON).click()

        except Exception as e:
            print(f"login failed for {self.PROBLEM_USER} --> {e}")

    def login_performance_glitch_user(self, context):
        try:
            # Fill username field
            page = context.page
            page.locator("textbox", name=self.USERNAME_FIELD).click
            page.locator("textbox", name=self.USERNAME_FIELD).fill(self.PERFORMANCE_GLITCH_USER)
            # Fill password field
            page = context.page
            page.locator("textbox", name=self.PASSWORD_FIELD).click
            page.locator("textbox", name=self.PASSWORD_FIELD).fill(self.MASTER_PASSWORD)
            # Press login button
            page.locator("button", name=self.LOGIN_BUTTON).click()

        except Exception as e:
            print(f"login failed for {self.PERFORMANCE_GLITCH_USER} --> {e}")

    def login_error_user(self, context):
        try:
            # Fill username field
            page = context.page
            page.locator("textbox", name=self.USERNAME_FIELD).click
            page.locator("textbox", name=self.USERNAME_FIELD).fill(self.ERROR_USER)
            # Fill password field
            page = context.page
            page.locator("textbox", name=self.PASSWORD_FIELD).click
            page.locator("textbox", name=self.PASSWORD_FIELD).fill(self.MASTER_PASSWORD)
            # Press login button
            page.locator("button", name=self.LOGIN_BUTTON).click()

        except Exception as e:
            print(f"login failed for {self.ERROR_USER} --> {e}")

    def login_visual_user(self, context):
        try:
            # Fill username field
            page = context.page
            page.locator("textbox", name=self.USERNAME_FIELD).click
            page.locator("textbox", name=self.USERNAME_FIELD).fill(self.VISUAL_USER)
            # Fill password field
            page = context.page
            page.locator("textbox", name=self.PASSWORD_FIELD).click
            page.locator("textbox", name=self.PASSWORD_FIELD).fill(self.MASTER_PASSWORD)
            # Press login button
            page.locator("button", name=self.LOGIN_BUTTON).click()

        except Exception as e:
            print(f"login failed for {self.VISUAL_USER} --> {e}")
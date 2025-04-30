# ========================================================================================== Imports ====================================================================================================
import requests
from behave import given, when, then
import re
from playwright.sync_api import expect
# ====================================================================================== Gherkin & Playwright Functions ================================================================================

@given('Insert username "{username}"')
@when('Insert username "{username}"')
@then('Insert username "{username}"')
def step(context, username):
    try:
        context.page.get_by_role("textbox", name="Username or email").fill(username)
    except Exception as e:
        print("\t\t[DEBUG] Exception: " + str(e))
        assert False, f"Failed to insert username '{username}': {str(e)}"

@given('Insert password "{password}"')
@when('Insert password "{password}"')
@then('Insert password "{password}"')
def step(context, password):
    try:
        context.page.get_by_role("textbox", name="Password").fill(password)
    except Exception as e:
        print("\t\t[DEBUG] Exception: " + str(e))
        assert False, f"Failed to insert password '{password}': {str(e)}"

@when('User logs in')	
@given('User logs in')	
@then('User logs in')	
def step(context):	#@DuplicatedSignature
	try:
		context.page.get_by_role("button", name="Sign In").click()
	except Exception as e:
		print("\t\t[DEBUG] Exception: " + str(e))
		assert False, "Invalid password field or not found."


@given('User logs out')
@when('User logs out')
@then('User logs out')
def step(context):
    try:
        context.page.get_by_role("banner").locator("i").first.click()
        context.page.get_by_role("button", name="Logout").click()
        print("\t\t[DEBUG] User successfully logged out.")
    except Exception as e:
        print("\t\t[DEBUG] Exception: " + str(e))
        assert False, "Expecting user to be logged out."

@given('User is logged out and should display login page')
@when('User is logged out and should display login page')
@then('User is logged out and should display login page')
def step(context):
    try:
        expect(context.page.locator("#kc-header-wrapper")).to_contain_text("AcromCloudNetwork")
        print("\t\t[DEBUG] Login page is displayed correctly.")
    except Exception as e:
        print("\t\t[DEBUG] Exception: " + str(e))
        assert False, "Login page not displayed as expected."

@given(u'User is logged in')
@when(u'User is logged in')
@then(u'User is logged in')
def step(context):  # @DuplicatedSignature
	print("\t\t[DEBUG] DEBUG POINT 1")
	try:
		sidebar = context.page.locator(".v-navigation-drawer__content")
		sidebar.wait_for(state="visible", timeout=5000)
		print("\t\t[DEBUG] User is already logged in.")
		return
	except Exception as e:
		print("\t\t[DEBUG] Exception (Not logged in yet): " + str(e))

	# If the test above fails, the next try/except block will run.
	try:
		context.page.get_by_role("textbox", name="Username or email").fill(context.TestUsername)
		context.page.get_by_role("textbox", name="Password").fill(context.TestPassword)
		context.page.get_by_role("button", name="Sign In").click()
		print("\t\t[DEBUG] DEBUG POINT 4")
		sidebar = context.page.locator(".v-navigation-drawer__content")
		sidebar.wait_for(state="visible", timeout=10000)  # Așteptăm mai mult după login
		print("\t\t[DEBUG] DEBUG POINT 5")
	except Exception as e:
		print("\t\t[DEBUG] Exception (Login failed): " + str(e))
		assert False, "Expecting user to be logged in, but login failed."

@then('Should display main page')
def step(context):
	page_title = context.page.title()
	assert page_title == "IPulse", f"Expected page title 'IPulse', but got '{page_title}'"
	print("\t\t[DEBUG] Page title is correct: IPulse")
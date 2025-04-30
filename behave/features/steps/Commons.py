# ========================================================================================== Imports ====================================================================================================
import time
from datetime import datetime, date, timedelta
from behave import given, when, then
from playwright.sync_api import expect
# ====================================================================================== Gherkin & Playwright Functions ================================================================================

@given('Select the field "{fieldType}" and type "{textType}"')
@then('Select the field "{fieldType}" and type "{textType}"')
@when('Select the field "{fieldType}" and type "{textType}"')
def step(context, fieldType, textType):
   pass

@given('Select dropdown "{fieldType}" and select "{textType}"')
@then('Select dropdown "{fieldType}" and select "{textType}"')
@when('Select dropdown "{fieldType}" and select "{textType}"')
def step(context, fieldType, textType):
    pass


@given('Select option "{textType}"')
@then('Select option "{textType}"')
@when('Select option "{textType}"')
def step(context, textType):
    pass

@given('Provide input password "{password}"')
@then('Provide input password "{password}"')
@when('Provide input password "{password}"')
def step(context, password):
    pass

@given('Select checkbox "{checkbox}"')
@when('Select checkbox "{checkbox}"')
@then('Select checkbox "{checkbox}"')
def step(context, checkbox):
    pass

@given('Page contains text "{text}"')
@when('Page contains text "{text}"')
@then('Page contains text "{text}"')
def step(context, text):
    try:
        expect(context.page.locator("#input-error")).to_contain_text(text)
        print(f"\t\t[DEBUG] Found expected text: '{text}'")
    except Exception as e:
        print(f"\t\t[DEBUG] Exception: {str(e)}")
        assert False, f"'{text}' was not found on the page!"

@given('From list displayed select "{displayedName}"')
@when('From list displayed select "{displayedName}"')
@then('From list displayed select "{displayedName}"')
def step(context, displayedName):
    pass

@given('Object "{objectName}" does not appear in the list')
@when('Object "{objectName}" does not appear in the list')
@then('Object "{objectName}" does not appear in the list')
def step(context, objectName):
    pass

@given('Button "{objectName}" is not accessible')
@when('Button "{objectName}" is not accessible')
@then('Button "{objectName}" is not accessible')
def step(context, objectName):
    pass

@given('Select "{testName}" and click "{actionButton}"')
@when('Select "{testName}" and click "{actionButton}"')
@then('Select "{testName}" and click "{actionButton}"')
def step(context, testName, actionButton):
    pass

@given('Select "{modelName}" with "{hostName}"')
@when('Select "{modelName}" with "{hostName}"')
@then('Select "{modelName}" with "{hostName}"')
def step(context, modelName, hostName):
    pass


@given('Field contains "{fieldText}" with "{textValue}"')
@when('Field contains "{fieldText}" with "{textValue}"')
@then('Field contains "{fieldText}" with "{textValue}"')
def step(context, fieldText, textValue):
    pass

@given('From lab "{appName}" with date today select "{actionButton}"')
@when('From lab "{appName}" with date today select "{actionButton}"')
@then('From lab "{appName}" with date today select "{actionButton}"')
def step(context, appName, actionButton):
    today = date.today().strftime("%Y%m%d")
    xpath_list = [
        f'//td[contains(., "{appName}")]//..//td[contains(., "{today}")]//..//i[contains(@title, "{actionButton}")]'
    ]
    framework.find_and_click_element_with_xpaths(context, xpath_list)
    pass

@given(u'Select menu "{menuName}"')
@when(u'Select menu "{menuName}"')
@then(u'Select menu "{menuName}"')
def step(context, menuName):
    xpath_list = [
        '//div[contains(text(), "' + menuName + '")]/../div[contains(@class, "menu_item")]',
        '//span[contains(@class,"tab_title") and text()="' + menuName + '"]'
    ]
    framework.find_and_click_element_with_xpaths(context, xpath_list, total_timeout=80)


@given('Checkbox "{enableImage}" is unchecked')
@when('Checkbox "{enableImage}" is unchecked')
@then('Checkbox "{enableImage}" is unchecked')
def step(context, enableImage):
    xpath_list = [
        f'//div[contains(@class, "v-selection-control v-selection-control--density-default v-checkbox-btn")][contains(., "{enableImage}")]'
    ]
    framework.element_found_with_xpaths(context, xpath_list, total_timeout=80, retry_interval=0.5, max_retries=3)

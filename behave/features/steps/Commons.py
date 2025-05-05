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
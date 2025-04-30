# ========================================================================================== Imports ====================================================================================================
import requests
import re
import os
from behave import given, when, then
# ====================================================================================== Gherkin & Playwright Functions ================================================================================
@given('Get software version and write target.version file')
@when('Get software version and write target.version file')
@then('Get software version and write target.version file')
def step(context):
    # Get software version using Playwright's locator
    swVersionElement = context.page.locator('//div[contains(@class,"version_info")]')
    swVersion = swVersionElement.text_content()
    print(f"SW Version: {str(swVersion)}")
    if not swVersion:
        assert False, "Unable to determine software version from AcromCloudNetwork DOM"
    # Format swVersion: remove multiple empty spaces and replace spaces with dashes
    swVersion = re.sub(' ', '-', swVersion)
    print(f"Formatted SW Version: {str(swVersion)}")
    # Write to target.version file
    with open(context.TargetVersionFilePath, "w") as f:
        f.write(swVersion)
    # Verify
    with open(context.TargetVersionFilePath, "r") as f:
        tsv = f.read()
        print("target.version: " + tsv)
        if swVersion != tsv:
            assert False, f"Unable to load swVersion or wrong swVersion written to '{os.path.abspath(context.TargetVersionFilePath)}' file"

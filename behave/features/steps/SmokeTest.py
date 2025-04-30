import requests
import time
import re
from behave import given, when, then


@when('Accessing AcromCloudNetwork Nightly instance')
def step(context):
	print("Accessing AcromCloudNetwork Nightly instance")
	
@then('Should return HTTP 200')
def step(context):
	try:
		response = context.request_context.get(context.ACN_url)
		assert response.status == 200, f"AcromCloudNetwork is offline and returned {response.status}"
	except Exception as e:
		assert False, f"Failed to connect to AcromCloudNetwork ({context.ACN_url}): {e}"

@given('Application is online')
def step(context):
	try:
		response = context.request_context.get(context.ACN_url)
		assert response.status == 200, f"AcromCloudNetwork is offline and returned {response.status}"
	except Exception as e:
		assert False, f"Failed to connect to AcromCloudNetwork ({context.ACN_url}): {e}"
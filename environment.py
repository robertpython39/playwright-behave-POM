import os
import subprocess
import sys
from aqualab.aqualab import AquaLab
from playwright.sync_api import sync_playwright			# Support for Microsoft PlayWright Testing Framework


def before_all(context):
    # Mandatory import for AquaLab hook
	context.aqualab = AquaLab(context)
	context.aqualab.before_all(context)
 
	# Configure variables
	context.TargetVersionFilePath = "./../target.version." + context.config.userdata.get("client") + "." + context.config.userdata.get("featureset") + ".tmp"
	context.ACN_url = "https://acn.test.acrom.io"
	context.TestUsername = "aqua-qa"
	context.TestPassword = "test1234!!"

	# Opțiuni pentru browser
	playwright_browser_options = {
		"headless": False if os.getenv("AQUA_RUNNER_ENVIRONMENT") != "True" else True,
		"args": [
			'--allow-running-insecure-content',
			'--ignore-certificate-errors',
			'--disable-dev-shm-usage',
   			'--window-size=1920,1080',
			'--start-maximized',
			'--no-sandbox',
			'--disable-features=StrictOriginIsolation,NetworkService,NetworkServiceInProcess'
		]
	}

	# Start PlayWright
	context.playwright = sync_playwright().start()

	# Start Browser
	context.browser = context.playwright.chromium.launch(**playwright_browser_options)
	context.browser = context.browser.new_context(no_viewport=True)	 # Remove any viewport restrictions to enable full-screen
	context.page = context.browser.new_page()
	context.page.goto(context.ACN_url)

	context.request_context = context.playwright.request.new_context()

	context.aqualab.register_playwright_session(context.browser, context.page)

 
def before_scenario(context, scenario):
    context.aqualab.before_scenario(context, scenario)
 
def before_step(context, step):
    context.aqualab.before_step(context, step)	
 
def after_step(context, step):
    context.aqualab.after_step(context, step)	
    
def after_scenario(context, scenario):
	context.aqualab.after_scenario(context, scenario)

def after_all(context):
    context.aqualab.after_all(context)

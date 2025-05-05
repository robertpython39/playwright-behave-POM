import os
from datetime import datetime
from playwright.sync_api import sync_playwright
from behave.features.utils.constants import *


def before_all(context):
	# Configure variables
	context.TargetVersionFilePath = "./../target.version." + context.config.userdata.get("client") + "." + context.config.userdata.get("featureset") + ".tmp"
	context.website_url = BASE_URL
	context.standard_user = STANDARD_USER
	context.locked_out_user = LOCKED_OUT_USER
	context.problem_user = PROBLEM_USER
	context.performance_glitch_user = PERFORMANCE_GLITCH_USER
	context.error_user = ERROR_USER
	context.visual_user = VISUAL_USER
	context.password = MASTER_PASSWORD

	# Global timeout for playwright
	context.page.set_default_timeout(DEFAULT_TIMEOUT)  # 10 sec

	# Opțiuni pentru browser
	playwright_browser_options = {
		"headless": False,
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
	context.page.goto(context.website_url)

	context.request_context = context.playwright.request.new_context()

	print("Browser launched and navigating to:", context.website_url)

def after_all(context, scenario):
	if scenario.status == "failed":
		timestamp = datetime.now().strftime("%Y%m%d_%H%M%S") # EU standard timezone
		scenario_name = scenario.name.replace(" ", "_").replace("/", "_")
		screenshot_dir = "reports/screenshots"
		os.makedirs(screenshot_dir, exist_ok=True)

		path = os.path.join(screenshot_dir, f"{scenario_name}_{timestamp}.png")
		context.page.screenshot(path=path, full_page=True)
		print(f"Screenshot saved to: {path}")
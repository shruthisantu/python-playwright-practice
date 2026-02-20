import re
from playwright.sync_api import Playwright, sync_playwright, expect


def run(playwright: Playwright) -> None:
    browser = playwright.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page1 = context.new_page()
    page1.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page1.get_by_role("textbox", name="Username:").click()
    page1.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page1.get_by_role("textbox", name="Password:").click()
    page1.get_by_role("textbox", name="Password:").fill("Learning@830$mK2")
    page1.get_by_role("combobox").select_option("teach")
    page1.get_by_role("checkbox", name="I Agree to the terms and").check()
    page1.get_by_role("button", name="Sign In").click()
    page1.get_by_role("textbox", name="Password:").click()
    expect(page1.get_by_role("button", name="Sign In")).to_be_visible()
    page1.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(5000)
    page1.get_by_text("Incorrect username/password.").click()
    expect(page1.get_by_text("Incorrect")).to_be_visible()
    page.wait_for_timeout(5000)

    # ---------------------
    context.close()
    browser.close()


with sync_playwright() as playwright:
    run(playwright)

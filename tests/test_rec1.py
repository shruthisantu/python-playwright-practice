import re
from playwright.sync_api import Page, expect


def test_example(page: Page) -> None:
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    page.get_by_role("textbox", name="Password:").click()
    page.get_by_role("textbox", name="Password:").fill("Learning@830$3mK2")
    page.get_by_role("textbox", name="Username:").click()
    page.get_by_role("textbox", name="Username:").fill("rahulshettyacademy")
    page.get_by_role("checkbox", name="I Agree to the terms and").check()
    page.get_by_role("button", name="Sign In").click()
    page.get_by_text("Shop Name Category 1 Category").click()
    page.get_by_text("Checkout ( 0 ) (current)").click()
    page.get_by_role("button", name="Continue Shopping").click()
    page.locator(
        "app-card").filter(has_text="Nokia Edge $24.99 Lorem ipsum").get_by_role("button").click()

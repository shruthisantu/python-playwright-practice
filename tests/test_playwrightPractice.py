from playwright.sync_api import Page, expect


def test_playwightPractice(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # page.wait_for_timeout(10000)
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()  # css selector
    # page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    page.wait_for_timeout(5000)
    page.close()

    # To write using ccs selectors, below is the way
    """
    To use with id,should start with #
    For ex: #id or #terms
    To use with class, should start with .
    For ex: .class or .text-info
    """


def test_negativeTest(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # page.wait_for_timeout(10000)
    page.get_by_label("Username:").fill("rahulshettyacademy")
    # here we are giving wrong password to check the error message
    page.get_by_label("Password:").fill("Learning@830$3mK2111")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()  # css selector
    # page.get_by_role("link", name="terms and conditions").click()
    page.get_by_role("button", name="Sign In").click()
    # page.wait_for_timeout(10000)
    expect(page.get_by_text("Incorrect username/password.")).to_be_visible()
    page.wait_for_timeout(10000)
    page.close()

from playwright.sync_api import Page, expect


def test_UiValidationScript(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")
    # page.wait_for_timeout(10000)
    page.get_by_label("Username:").fill("rahulshettyacademy")
    page.get_by_label("Password:").fill("Learning@830$3mK2")
    page.get_by_role("combobox").select_option("teach")
    page.locator("#terms").check()  # css selector
    page.get_by_role("button", name="Sign In").click()
    # adding below 2 products to cart
    iphone_page = page.locator("app-card").filter(has_text="iphone X")
    iphone_page.get_by_role("button").click()
    nokia_page = page.locator("app-card").filter(has_text="Nokia Edge")
    nokia_page.get_by_role("button").click()
    page.get_by_text("Checkout").click()
    # validating whether 2 products are visible after clicking checkout
    locatorToFindItems = page.locator(".media-body")
    expect(locatorToFindItems).to_have_count(2)


def test_newChildWindow(page: Page):
    page.goto("https://rahulshettyacademy.com/loginpagePractise/")

    with page.expect_popup() as newPage_info:
        page.locator(".blinkingText").click()  # new page
        childPage = newPage_info.value
        childPage.wait_for_load_state()
        text = childPage.locator(".red").text_content()
        print(text)
        words = text.split("at")
        print(words)
        email = words[1].strip().split(" ")[0]
        print(email)
        assert email == "mentor@rahulshettyacademy.com"

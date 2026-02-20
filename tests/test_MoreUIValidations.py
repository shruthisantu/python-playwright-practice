from playwright.sync_api import Page, expect

"""
In this function we are checking placeholder like Hide and Show
on clicking Hide, placeholder box should be hidden
"""


def test_UIChecks(page: Page):
    """
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    placeholder = page.get_by_placeholder("Hide/Show Example")
    expect(placeholder).to_be_visible()
    # placeholder.get_by_role("button", name="Hide").click() 
    #or we can also write using css locators like below
    placeholder.locator("#hide-textbox").click()
    """

# or
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    page.wait_for_timeout(5000)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()


"""
In this below function we are checking placeholder like Hide and Show
on clicking Show, placeholder box should be visible
"""


def test_UIChecks1(page: Page):
    # Hide and show placeholder handling
    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()
    page.locator("#hide-textbox").click()
    page.wait_for_timeout(5000)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_hidden()
    page.get_by_role("button", name="Show").click()
    page.wait_for_timeout(5000)
    expect(page.get_by_placeholder("Hide/Show Example")).to_be_visible()

    # To Handle ALert boxes or dailog boxes
    """
    To handle Alert boxes, we have to declare that we might expect Alert box when clicked something and 
    we have to accept that alert box
    syntax- 
    page.on(event, lambda function)
    """
    page.on("dailog", lambda dailog: dailog.accept())
    page.get_by_role("button", name="Confirm").click()

    # to mouse hover on an element
    page.locator("#mousehover").hover()
    page.wait_for_timeout(5000)
    page.get_by_role("link", name="Top").click()


def test_HandleIframe(page: Page):

    # Frame Handling: Like handling page inside a page(we call it as Frames)

    page.goto("https://rahulshettyacademy.com/AutomationPractice/")
    # page.locator("iframe[name=\"iframe-name\"]").content_frame.get_by_role("link", name="NEW All Access plan").click() #using codegen tool
    pageFrame = page.frame_locator("#courses-iframe")
    pageFrame.get_by_role("link", name="All Access plan").click()
    expect(pageFrame.locator("body")).to_contain_text("Happy Subscibers!")


"""
To check the price of rice is equal to 37.
To randomly identify rows and columns in a web table
"""
# To handle dynamic web page


def test_webTableHandling(page: Page):
    page.goto("https://rahulshettyacademy.com/seleniumPractise/#/offers")

    # identify price column
    locatorsColumn = page.locator("th")
    # locatorsColumn = page.locator("th").count() #there are 3 columns in web table, so it will return 3
    for index in range(locatorsColumn.count()):
        priceColumn = locatorsColumn.nth(index).filter(has_text="Price")
        if priceColumn.count() > 0:
            priceColValue = index
            # it returns index value = 1 as price is located in 2nd column
            print(f"column value is {priceColValue}")
            break

    # identify rice row
    riceRow = page.locator("tr").filter(has_text="Rice")

    # To get the value from row column Rice ,what value it has in (index) column ie 2nd column
    # this returns 3 td s' from page (excplicitely from riceRow locator)

    riceValue = riceRow.locator("td").nth(priceColValue)
    value = riceRow.locator("td").nth(priceColValue).inner_text()
    print(
        f"rice value is {value} ")
    # or
    expect(riceValue).to_have_text("37")


def test_web_api(playwright: Playwright):
    request_context = playwright.request.new_context()
    request_context.

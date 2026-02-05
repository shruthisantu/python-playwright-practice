# Simple beginner test - just copy this whole block
from playwright.sync_api import Page, expect


def test_check_page_title(page: Page):
    """Test 1: Check if page title is correct"""
    page.goto("https://demo.playwright.dev/todomvc/")

    # Check page title
    title = page.title()
    print(f"📄 Page title is: {title}")
    page.wait_for_timeout(5000)

    # Verify title matches expected
    assert title == "React • TodoMVC", f"Expected 'TodoMVC' but got '{title}'"
    print("✅ Test 1 passed!")


def test_add_todo_item(page: Page):
    """Test 2: Add a todo item"""
    page.goto("https://demo.playwright.dev/todomvc/")

    # Find input box and type
    input_box = page.locator(".new-todo")
    input_box.fill("Practice Azure DevOps")
    input_box.press("Enter", timeout=5000)
    # Check if todo was added
    todo_count = page.locator(".todo-list li").count()
    print(f"📝 Number of todos: {todo_count}")

    assert todo_count == 1, f"Expected 1 todo but found {todo_count}"
    print("✅ Test 2 passed!")


def test_github_homepage(page: Page):
    """Test 3: Simple GitHub page test"""
    page.goto("https://github.com")

    # Check if page loaded
    expect(page).to_have_title(
        "GitHub · Change is constant. GitHub keeps you ahead. · GitHub")
    page.wait_for_timeout(7000)
    print("🌐 GitHub page loaded successfully!")
    print("✅ Test 3 passed!")

from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # przechodzimy do strony logowania
    page.goto("https://practicetestautomation.com/practice-test-login/")
    # wprowadzenie username
    page.fill("#username","student1")
    # wprowadzenie password
    page.fill("#password","Password123")
    # klikniecie przycisku Submit
    page.click("#submit")
    

    # 1 test - sprawdzenie aktualnego URL
    current_url = page.url
    print(f"Aktualny URL: {current_url}")
    assert "practice-test-login" in current_url

    # 2 test - sprawdzenie pojawienia się komunikatu błędu
    error_text = page.text_content("text=Your username is invalid!")
    print(f"Komunikat błędu:", error_text)
    assert error_text == "Your username is invalid!"

    browser.close()
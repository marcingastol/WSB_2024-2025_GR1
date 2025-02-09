from playwright.async_api import sync_playwright

with sync_playwright() as p:
    # startujemy przegladarke
    browser = p.chromium.launch(headless=False)
    # otwieramy nowa karte/strone w przegladarce
    page = browser.new_page()
    # przechodzimy na strone 
    page.goto("http://onet.pl")
    # pobieramy tytul strony
    page_title = page.title()
    # drukujemy na konsole tytul strony
    print(f"Tytul strony to {page_title}")

    # sprawdzamy czy tytul strony zawiera oczekiwany tekst
    assert "Onet – Jesteś na bieżąco" in page_title
    
    # zamykamy przegladarke
    browser.close()
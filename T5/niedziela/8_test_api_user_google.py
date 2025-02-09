from playwright.sync_api import sync_playwright

# połączenie do JSON PlaceHolder
with sync_playwright() as p:
    # utworzyć kontekst API - inny niż przeglądarki
    request_context = p.request.new_context()
    # wysyłamy żądanie GET do API
    response = request_context.get("https://jsonplaceholder.typicode.com/users/1")
    # sprawdzamy status odpowiedzi
    status = response.status

    print("Status odpowiedzi:", status)
    assert status == 200

    # pobranie odpowiedzi z zapytania GET jako json
    result = response.json()
    name = result["name"] # zapisanie nazwy uzytkownika do zmiennej
    print("Użytkownik nazywa się:",name)

# połączenie do Google
with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    # przechodzimy do strony logowania
    page.goto("https://www.google.pl/")

    # PopUp - kliknij Zaakceptuj wszystko
    page.click("button:has-text('Zaakceptuj wszystko')")

    # wpisanie name to pola wyszukania
    page.locator("textarea").first.fill(name)
    # Szukaj w Google
    page.click("input[value='Szukaj w Google']")

    page.wait_for_timeout(10000)
    browser.close()
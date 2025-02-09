from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # utworzyć kontekst API - inny niż przeglądarki
    request_context = p.request.new_context()
    # wysyłamy żądanie GET do API
    response = request_context.get("https://jsonplaceholder.typicode.com/posts")
    # sprawdzamy status odpowiedzi
    status = response.status

    print("Status odpowiedzi:", status)
    assert status == 200

    posts = response.json()
    assert isinstance(posts, list)

    if len(posts) > 0:
        print(f"W aplikacji znajduje sie {len(posts)} postów")

        print("Sprawdzenie czy w aplikacji znajduje się 100 postów...")
        assert len(posts) == 100
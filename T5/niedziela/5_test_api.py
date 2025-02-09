from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # utworzyć kontekst API - inny niż przeglądarki
    request_context = p.request.new_context()
    # wysyłamy żądanie GET do API
    response = request_context.get("https://jsonplaceholder.typicode.com/posts/1")
    # sprawdzamy status odpowiedzi
    status = response.status

    print("Status odpowiedzi:", status)
    assert status == 200

    body = response.json()
    print(body)

    id = body["id"] # spodziewamy się 1
    userid = body["userId"] # spodziewamy się 1
    print("Id to:", id)
    print("UserId to:", userid)

    assert id == 1
    assert userid == 1

    title = body["title"]
    print("Typ title to string:",isinstance(title, str))
    assert isinstance(title, str)
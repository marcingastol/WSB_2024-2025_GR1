from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    # utworzyć kontekst API - inny niż przeglądarki
    request_context = p.request.new_context()
    # przygotowanie danych do wyslania
    userId = 9
    new_post = {"userId": userId, "title": "title sample", "body": "body sample"}
    print("Wysyłamy nowy post:",new_post)
    # wysyłamy żądanie POST do API aby utworzyć nowy post
    response = request_context.post("https://jsonplaceholder.typicode.com/posts",data=new_post)

    status = response.status
    print("Status:",status)
    assert status == 201

    result = response.json()
    print(result)

    assert result["userId"] == userId
    assert result["title"] == new_post["title"]
    assert result["body"] == "body sample"
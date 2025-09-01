import requests

BASE = "http://127.0.0.1:5000"

def p(label, resp):
    try:
        print(label, resp.status_code, resp.json())
    except Exception:
        print(label, resp.status_code, resp.text)

p("GET (missing)", requests.get(f"{BASE}/video/1"))

p("POST (create)", requests.post(f"{BASE}/video/1", json={
    "name": "My First Video",
    "likes": 10,
    "views": 100
}))

p("GET (found)", requests.get(f"{BASE}/video/1"))

p("PUT (update likes)", requests.put(f"{BASE}/video/1", json={"likes": 20}))

p("GET /videos", requests.get(f"{BASE}/videos"))

p("DELETE", requests.delete(f"{BASE}/video/1"))

p("GET after delete", requests.get(f"{BASE}/video/1"))

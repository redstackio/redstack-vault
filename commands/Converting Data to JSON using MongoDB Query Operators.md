---
id: 7955435c-7b58-4bd2-975c-1023aa70ec1c
name: Converting Data to JSON using MongoDB Query Operators
type: command
executor: bash
data: '{"username": {"$ne": null}, "password": {"$ne": null}}

  {"username": {"$ne": "foo"}, "password": {"$ne": "bar"}}

  {"username": {"$gt": undefined}, "password": {"$gt": undefined}}

  {"username": {"$gt":""}, "password": {"$gt":""}}'
output: null
created_at: '2023-04-06T03:56:31.415064+00:00'
updated_at: '2023-04-10T20:23:01.283847+00:00'
---

# Converting Data to JSON using MongoDB Query Operators

```bash
{"username": {"$ne": null}, "password": {"$ne": null}}
{"username": {"$ne": "foo"}, "password": {"$ne": "bar"}}
{"username": {"$gt": undefined}, "password": {"$gt": undefined}}
{"username": {"$gt":""}, "password": {"$gt":""}}
```

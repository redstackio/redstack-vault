---
id: b92aa5ab-daa3-4da8-bb28-785f8c91dfc9
type: code
language: json
verified: false
created_at: '2023-04-06T03:55:58.926511+00:00'
updated_at: '2023-04-10T20:22:24.025152+00:00'
---

# Code Snippet b92aa5ab

**Language**: json

```json
{
  doctors(
    options: "{\"limit\": 1, \"patients.ssn\" :1}", 
    search: "{ \"patients.ssn\": { \"$regex\": \".*\"}, \"lastName\":\"Admin\" }")
    {
      firstName lastName id patients{ssn}
    }
}
```

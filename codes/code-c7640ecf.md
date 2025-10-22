---
id: c7640ecf-372c-4249-9e99-2a07cff42e2c
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:51.173425+00:00'
updated_at: '2023-04-10T20:21:07.519483+00:00'
---

# Code Snippet c7640ecf

**Language**: Powershell

```powershell
curl --request PUT \
  --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings \
  --header 'content-type: application/json' \
  --header 'x-algolia-api-key: <example-key>' \
  --header 'x-algolia-application-id: <example-application-id>' \
  --data '{"highlightPreTag": "<script>alert(1);</script>"}'
```

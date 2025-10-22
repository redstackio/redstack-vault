---
id: fa076f7d-e0d5-4ead-b409-191dfe004f30
type: code
language: Powershell
verified: false
created_at: '2023-04-06T03:55:52.119026+00:00'
updated_at: '2023-04-06T03:55:52.127617+00:00'
---

# Code Snippet fa076f7d

**Language**: Powershell

```powershell
curl --request PUT \
  --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings \
  --header 'content-type: application/json' \
  --header 'x-algolia-api-key: <example-key>' \
  --header 'x-algolia-application-id: <example-application-id>' \
  --data '{"highlightPreTag": "<script>alert(1);</script>"}'
```

---
id: ab2c7ff3-af83-4077-98f9-aa5868e9f484
name: Set Highlight Pre-Tag
type: command
executor: bash
data: "curl --request PUT \\\n  --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings\
  \ \\\n  --header 'content-type: application/json' \\\n  --header 'x-algolia-api-key:\
  \ <example-key>' \\\n  --header 'x-algolia-application-id: <example-application-id>'\
  \ \\\n  --data '{\"highlightPreTag\": \"<script>alert(1);</script>\"}'"
output: null
created_at: '2023-04-06T03:55:53.045060+00:00'
updated_at: '2023-04-06T03:55:53.052668+00:00'
---

# Set Highlight Pre-Tag

```bash
curl --request PUT \
  --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings \
  --header 'content-type: application/json' \
  --header 'x-algolia-api-key: <example-key>' \
  --header 'x-algolia-application-id: <example-application-id>' \
  --data '{"highlightPreTag": "<script>alert(1);</script>"}'
```

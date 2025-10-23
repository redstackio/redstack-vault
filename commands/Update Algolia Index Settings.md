---
id: 56b8dc3d-6ed6-4092-aea9-d624d85ac25f
name: Update Algolia Index Settings
type: command
executor: bash
data: "curl --request PUT \\\n  --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings\
  \ \\\n  --header 'content-type: application/json' \\\n  --header 'x-algolia-api-key:\
  \ <example-key>' \\\n  --header 'x-algolia-application-id: <example-application-id>'\
  \ \\\n  --data '{\"highlightPreTag\": \"<script>alert(1);</script>\"}'"
output: null
created_at: '2023-04-06T03:55:51.173098+00:00'
updated_at: '2023-04-10T20:21:07.517806+00:00'
---

# Update Algolia Index Settings

```bash
curl --request PUT \
  --url https://<application-id>-1.algolianet.com/1/indexes/<example-index>/settings \
  --header 'content-type: application/json' \
  --header 'x-algolia-api-key: <example-key>' \
  --header 'x-algolia-application-id: <example-application-id>' \
  --data '{"highlightPreTag": "<script>alert(1);</script>"}'
```



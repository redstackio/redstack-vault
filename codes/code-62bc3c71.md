---
id: 62bc3c71-6c9b-410d-9e2a-c07683c760ae
type: code
language: Bash
verified: false
created_at: '2023-05-25T03:23:29.834845+00:00'
updated_at: '2023-05-25T03:23:29.850067+00:00'
---

# Code Snippet 62bc3c71

**Language**: Bash

```bash
# Send a request to the persistent webhook to create a new user
curl -d '{"RequestBody":{"Username":"NewAzureOwnerAccount","Password":"Password123"}}' -H "Content-Type: application/json" -X POST https://s15events.azure-automation.net/webhooks?token=<YOUR_WEBHOOK_TOKEN>
```



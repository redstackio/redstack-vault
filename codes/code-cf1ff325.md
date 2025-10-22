---
id: cf1ff325-74ea-4a9c-ac38-239701b363c2
type: code
language: Bash
verified: false
created_at: '2023-05-25T03:20:33.953351+00:00'
updated_at: '2023-05-25T03:23:08.782768+00:00'
---

# Code Snippet cf1ff325

**Language**: Bash

```bash
curl -d '{"RequestBody":{"Username":"NewAzureOwnerAccount","Password":"Password123"}}' -H "Content-Type: application/json" -X POST https://s15events.azure-automation.net/webhooks?token=<YOUR_WEBHOOK_TOKEN>

```

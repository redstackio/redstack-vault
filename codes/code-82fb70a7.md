---
id: 82fb70a7-9de3-4213-b8e3-8e7664d14c59
type: code
language: ''
verified: false
created_at: '2023-06-06T03:12:18.071536+00:00'
updated_at: '2023-06-06T03:12:44.566956+00:00'
---

# Code Snippet 82fb70a7

```
except OSError:
  let client = newHttpClient()
  client.headers = newHttpHeaders({ "Content-Type": "application/json", "Content-MD5": Outp_shell_md5_string,"x-event-id": $event_id })
  let body = %*{
      "data": "No Response"
  }
  let response = client.request(server & "/cmd", httpMethod = HttpPost, body = $body)
```

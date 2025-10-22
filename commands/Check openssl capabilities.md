---
id: 97875943-822b-4d93-985c-94d6059b1ffb
name: Check openssl capabilities
type: command
executor: bash
data: "$ getcap openssl /usr/bin/openssl \nopenssl=ep"
output: null
created_at: '2023-04-06T03:56:18.914964+00:00'
updated_at: '2023-04-10T20:34:20.931371+00:00'
---

# Check openssl capabilities

```bash
$ getcap openssl /usr/bin/openssl 
openssl=ep
```

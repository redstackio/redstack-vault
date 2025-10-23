---
id: e077b775-3951-4831-9582-c3c7891c415f
name: Getcap List All Files with Capabilities Set
type: command
executor: bash
data: getcap -r / 2>/dev/null
output: 'user@ubuntu18x64:~$ getcap -r / 2>/dev/null

  /usr/bin/openssl = cap_dac_override+ep

  /usr/bin/mtr-packet = cap_net_raw+ep'
created_at: '2019-10-11T21:24:57.010925+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Getcap List All Files with Capabilities Set

```bash
getcap -r / 2>/dev/null
```

## Expected Output

```
user@ubuntu18x64:~$ getcap -r / 2>/dev/null
/usr/bin/openssl = cap_dac_override+ep
/usr/bin/mtr-packet = cap_net_raw+ep
```



---
id: a5425d8d-80d1-4fbd-8407-b43712affb5d
name: List Connected Users
type: command
executor: bash
data: '$ impacket-smbclient Administrator@10.10.10.10

  # who

  host:  \\10.10.10.10, user: Administrator, active:     1, idle:     0'
output: null
created_at: '2023-04-06T03:56:04.179154+00:00'
updated_at: '2023-04-10T20:36:03.709267+00:00'
---

# List Connected Users

```bash
$ impacket-smbclient Administrator@10.10.10.10
# who
host:  \\10.10.10.10, user: Administrator, active:     1, idle:     0
```



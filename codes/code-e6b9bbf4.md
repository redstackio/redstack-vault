---
id: e6b9bbf4-f5f5-4b27-b748-7bba09e6d9fe
type: code
language: Bash
verified: false
created_at: '2020-03-23T01:50:57.460478+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet e6b9bbf4

**Language**: Bash

```bash
apt update && apt install snmp-mibs-downloader -y \
&& sed -i '/mibs/s/^/#/g' /etc/snmp/snmp.conf
```

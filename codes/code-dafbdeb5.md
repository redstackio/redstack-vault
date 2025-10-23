---
id: dafbdeb5-fce4-44f7-bfff-028506873b6a
type: code
language: Bash
verified: false
created_at: '2020-03-17T04:15:34.352551+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet dafbdeb5

**Language**: Bash

```bash
apt update && apt install snmp-mibs-downloader -y \
&& sed -i '/mibs/s/^/#/g' /etc/snmp/snmp.conf
```



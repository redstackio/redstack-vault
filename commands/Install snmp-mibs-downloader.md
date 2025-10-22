---
id: cb616849-fd9b-4017-afa9-33019b9c0e5c
name: Install snmp-mibs-downloader
type: command
executor: bash
data: apt update && apt install snmp-mibs-downloader -y && sed -i '/mibs/s/^/#/g'
  /etc/snmp/snmp.conf
output: null
created_at: '2019-09-17T00:51:23.949173+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Install snmp-mibs-downloader

```bash
apt update && apt install snmp-mibs-downloader -y && sed -i '/mibs/s/^/#/g' /etc/snmp/snmp.conf
```

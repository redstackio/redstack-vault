---
id: 6836c849-441e-411f-86cc-e03361b788f1
name: Delete rule
type: command
executor: bash
data: 'iptables -D INPUT -i eth0 -p tcp --dport 443 -j ACCEPT

  '
output: null
created_at: '2020-07-14T18:21:35.433496+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Delete rule

```bash
iptables -D INPUT -i eth0 -p tcp --dport 443 -j ACCEPT

```



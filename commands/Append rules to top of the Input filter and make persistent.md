---
id: 0c99f814-dd6c-45c7-85ea-513ce72bef7e
name: Append rules to top of the Input filter and make persistent
type: command
executor: bash
data: '/sbin/iptables -I INPUT -p tcp --dport 50050 -s -j ACCEPT

  /sbin/iptables -I INPUT -p tcp --dport 22 -s -j ACCEPT

  service netfilter-persistent save

  iptables -L -v

  '
output: null
created_at: '2020-07-14T18:21:35.433339+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# Append rules to top of the Input filter and make persistent

```bash
/sbin/iptables -I INPUT -p tcp --dport 50050 -s -j ACCEPT
/sbin/iptables -I INPUT -p tcp --dport 22 -s -j ACCEPT
service netfilter-persistent save
iptables -L -v

```



---
id: 5ee4c6c9-bfe8-4299-9685-7b8df50bc359
name: iptables
type: cheatsheet
verified: false
created_at: '2020-07-14T18:21:35.461465+00:00'
updated_at: '2023-05-29T16:48:52.690130+00:00'
---

# iptables

**Command** ([[Append rules to top of the Input filter and make persistent]]):

```bash
/sbin/iptables -I INPUT -p tcp --dport 50050 -s -j ACCEPT
/sbin/iptables -I INPUT -p tcp --dport 22 -s -j ACCEPT
service netfilter-persistent save
iptables -L -v

```

**Command** ([[Delete rule]]):

```bash
iptables -D INPUT -i eth0 -p tcp --dport 443 -j ACCEPT

```

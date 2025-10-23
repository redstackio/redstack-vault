---
id: df437724-1e21-41bc-b62c-6c7b52d78c81
name: Host Discovery using nmap
type: command
executor: bash
data: nmap -sn -n --disable-arp-ping 192.168.1.1-254 | grep -v "host down"
output: null
created_at: '2023-04-06T03:56:21.904156+00:00'
updated_at: '2023-04-10T20:25:09.485621+00:00'
---

# Host Discovery using nmap

```bash
nmap -sn -n --disable-arp-ping 192.168.1.1-254 | grep -v "host down"
```



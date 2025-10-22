---
id: aa6d7778-46a5-4161-84ac-6961f2805b89
name: scan all udp ports
type: command
executor: bash
data: 'nmap -p- -sU -oN all_udp_ports.txt target-ip

  '
output: null
created_at: '2020-07-14T18:14:50.436544+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
---

# scan all udp ports

```bash
nmap -p- -sU -oN all_udp_ports.txt target-ip

```

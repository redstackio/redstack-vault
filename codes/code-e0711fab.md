---
id: e0711fab-a891-403e-8596-4819535baf5f
type: code
language: ps1
verified: false
created_at: '2023-04-06T03:56:23.097341+00:00'
updated_at: '2023-04-10T20:25:12.041396+00:00'
---

# Code Snippet e0711fab

**Language**: ps1

```ps1
sudo apt-get install tcpdump
tcpdump -w 0001.pcap -i eth0
tcpdump -A -i eth0

# capture every TCP packet
tcpdump -i eth0 tcp

# capture everything on port 22
tcpdump -i eth0 port 22
```

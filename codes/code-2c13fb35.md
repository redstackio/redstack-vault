---
id: 2c13fb35-4b37-40fb-8168-4cb8697608f8
type: code
language: Python3
verified: false
created_at: '2020-03-23T01:20:44.177670+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 2c13fb35

**Language**: Python3

```python3
#!/usr/bin/env python3
from scapy.all import *
import sys

if len(sys.argv) < 2:
    print(f"Usage: {sys.argv[0]} <INTERFACE>")
    exit(0)
else:
    interface = sys.argv[1]
    print(f"Sniffing on {interface}")

def print_data(pkt):
    if (pkt.haslayer(ICMP)) and (pkt[ICMP].type == 8):
        data = pkt[ICMP].load[-4:].decode("utf-8")
        print(f"{data}", flush=True, end="")

sniff(iface = interface, prn=print_data)
```

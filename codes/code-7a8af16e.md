---
id: 7a8af16e-ca0b-411d-91db-9056a6cef468
type: code
language: Python3
verified: false
created_at: '2020-03-16T08:11:02.820584+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
---

# Code Snippet 7a8af16e

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

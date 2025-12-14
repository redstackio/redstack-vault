---
id: proc-ip-ping-zomato
tags:
  - reconnaissance
  - ip-resolution
type: procedure
tools:
  - '[[tools/ping]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/ping-resolve-ip]]'
verified: false
platforms:
  - Linux
  - Windows
  - macOS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T03:46:37.145Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# IP-Address-Discovery-with-Ping

## Summary

This procedure uses the ping utility to resolve a domain name to its IP address, serving as the initial step in reconnaissance to identify the target's network location for Zomato-associated infrastructure.

## Description

In a reconnaissance scenario targeting Zomato, ping is employed to query DNS and obtain the IP address (e.g., 52.77.124.190) of the target domain. This enables subsequent scanning and enumeration. The procedure assumes public DNS resolution and no firewalls blocking ICMP. Expected outcomes include the target's IP for further tool usage.

## Requirements

1. Network access to the internet and target domain
2. ping tool installed (standard on most OS)
3. No special credentials needed

## Defense

Defensive measures and detection strategies:

- Monitor DNS queries for unusual patterns
- Implement DNS logging to track resolution attempts

## Objectives

1. Resolve target domain to IP address
2. Confirm target reachability
3. Prepare for deeper network scans

## Instructions

### Step 1: Resolve Domain IP

**Context**: Ping the target domain to obtain its IP address and verify connectivity.

**Command** ([[commands/ping-resolve-ip]]):
```bash
ping zomato.com
```

> This command sends ICMP echo requests to zomato.com, displaying the resolved IP 52.77.124.190 in the output. Stop with Ctrl+C after confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Network Information

### Sub-Techniques


## Commands Used

- [[commands/ping-resolve-ip]]

## Tools Used

- [[tools/ping]]

## Tags

- [[Reconnaissance]]
- [[ip-resolution]]

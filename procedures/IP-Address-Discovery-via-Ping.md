---
id: proc-ip-discovery-ping-927413
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
  - Web
  - AWS
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Gather Victim Host Information]]'
updated_at: '2025-12-14T17:27:35.681Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# IP-Address-Discovery-via-Ping

## Summary

This procedure uses the ping utility to resolve a domain name to its IP address, providing the starting point for reconnaissance on targets like Zomato's infrastructure.

## Description

In the context of external reconnaissance, ping sends ICMP echo requests to resolve the domain to an IP (e.g., zomato.com to 52.77.124.190), confirming reachability and enabling subsequent scanning. This is a low-risk initial step with no authentication needed, but it reveals the target's public IP for further attacks.

## Requirements

1. Internet connectivity
2. Command-line access (Linux/Windows/macOS)
3. Target domain name (e.g., zomato.com)

## Defense

Defensive measures and detection strategies:

- Monitor ICMP traffic for unusual ping volumes
- Use firewalls to rate-limit ICMP requests

## Objectives

1. Resolve domain to IP address
2. Confirm target host is live
3. Gather basic network info for next steps

## Instructions

### Step 1: Execute Ping Command

**Context**: Send ICMP packets to the target domain to retrieve its IP.

**Command** ([[commands/ping-resolve-ip]]):
```bash
ping -c 4 zomato.com
```

> This command sends 4 ping packets and displays the resolved IP 52.77.124.190 along with round-trip times. Successful output confirms the host is reachable.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Gather Victim Host Information]] Gather Victim Host Information

### Sub-Techniques


## Commands Used

- [[commands/ping-resolve-ip]]

## Tools Used

- [[tools/ping]]

## Tags

- [[Reconnaissance]]
- [[ip-resolution]]

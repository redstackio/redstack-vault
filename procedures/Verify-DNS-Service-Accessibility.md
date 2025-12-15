---
tags:
  - verification
  - dns
  - connectivity
type: procedure
tools:
  - '[[tools/telnet]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/telnet-connect-port]]'
platforms:
  - Linux
  - Network
techniques:
  - '[[Active Scanning]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 182f2686-aff9-4037-b9f2-e5406e5767ca
created_at: '2025-12-14T17:26:36.891Z'
updated_at: '2025-12-14T17:26:36.891Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-DNS-Service-Accessibility

## Summary

This procedure tests TCP connectivity to the DNS port (53) on the target host to ensure the service is reachable before attempting exploitation, confirming no immediate firewalls block access.

## Description

Following port discovery, this step uses telnet to attempt a direct connection to port 53 on ci.nextcloud.com. A successful connection validates that the BIND9 DNS service is accessible over TCP, setting the stage for UDP-based DoS exploitation via TKEY queries. This is a low-risk verification in external attack scenarios.

## Requirements

1. Network access to the target port 53
2. Telnet client available on the attacker's system
3. Prior knowledge of the target host from scanning

## Defense

Defensive measures and detection strategies:

- Disable unnecessary TCP wrappers or use UDP-only for DNS to avoid TCP probes
- Log and alert on failed or suspicious telnet connections in firewall logs
- Employ network segmentation to restrict external access to DNS ports

## Objectives

1. Confirm TCP reachability of the DNS service
2. Validate service responsiveness without exploitation
3. Identify any basic access restrictions

## Instructions

### Step 1: Establish TCP Connection

**Context**: Use telnet to connect to the target host and port, observing if the connection succeeds.

**Command** ([[commands/telnet-connect-port]]):
```bash
telnet ci.nextcloud.com 53
```

> This initiates a TCP handshake to port 53. On success, it displays "Connected to ci.nextcloud.com. Escape character is '^]'". Type quit or use Ctrl+C to exit. Failure indicates blocked access or downed service.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/telnet-connect-port]]

## Tools Used

- [[tools/telnet]]

## Tags

- [[verification]]
- [[DNS]]
- [[connectivity]]

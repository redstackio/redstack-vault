---
tags:
  - dns-exfiltration
  - monitoring
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/monitor-dns-requests]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: 24536e99-98a3-4515-a4b0-bd6875d3d95b
created_at: '2025-12-13T09:00:27.636Z'
updated_at: '2025-12-13T09:00:27.636Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Monitor DNS for Data Exfiltration

## Summary

This procedure involves monitoring an attacker-controlled DNS server for requests triggered by blind XXE, allowing exfiltration of internal data.

## Description

Since direct channels are blocked, DNS is used for blind exfiltration. Monitor incoming queries to reconstruct leaked data from the target's internal environment.

## Requirements

1. Control over a DNS server or domain
2. Network monitoring tool like tcpdump
3. Triggered XXE payload on target

## Defense

Defensive measures and detection strategies:

- Block outbound DNS from sensitive servers
- Anomaly detection on DNS traffic volume

## Objectives

1. Capture exfiltrated data via DNS
2. Reconstruct internal information
3. Validate exploitation success

## Instructions

### Step 1: Capture DNS Traffic

**Context**: Listen for incoming DNS requests from the target.

**Command** ([[commands/monitor-dns-requests]]):
```bash
tcpdump -i any port 53
```

> This command captures traffic on port 53 to observe exfiltration attempts.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/monitor-dns-requests]]

## Tools Used



## Tags

- [[dns-exfiltration]]
- [[monitoring]]

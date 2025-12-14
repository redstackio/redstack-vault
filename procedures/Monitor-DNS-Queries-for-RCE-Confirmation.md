---
tags:
  - confirmation
  - dns
  - exfiltration
type: procedure
tools:
  - '[[tools/BIND]]'
tactics:
  - '[[Command and Control]]'
commands: []
verified: false
platforms:
  - Network
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
updated_at: '2025-12-14T17:23:27.244Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: cdc5380a-28dd-4865-a321-f5581fd3fb66
validated: true
mitre_tactics:
  - '[[Command and Control]]'
mitre_techniques:
  - '[[Exfiltration Over Command and Control Channel]]'
---
---

# Monitor-DNS-Queries-for-RCE-Confirmation

## Summary

This procedure monitors DNS server logs to confirm successful RCE by detecting queries triggered by the deserialized payload.

## Description

After sending the URLDNS payload, the server's deserialization causes a DNS resolution to the attacker's domain, providing out-of-band confirmation of code execution without alerting the target.

## Requirements

1. Controlled DNS server (e.g., BIND) hosting the domain
2. Access to server logs
3. Knowledge of target IP for query source validation

## Defense

Defensive measures and detection strategies:

- Monitor application server DNS traffic for unusual domains
- Implement DNS logging and anomaly detection
- Block resolutions to unknown external domains

## Objectives

1. Observe incoming DNS queries
2. Validate source IP as target server
3. Confirm deserialization success

## Instructions

### Step 1: Inspect BIND Logs

**Context**: Review logs for queries to the controlled domain post-payload send.

No direct command; manually tail or grep logs:

```bash
tail -f /var/log/named/query.log | grep dod.jexboss.info
```

> Expected output: Log entries showing query from DoD server IP.

## MITRE ATT&CK Mapping

### Tactics

- [[Command and Control]] Command and Control

### Techniques

- [[Exfiltration Over Command and Control Channel]] Exfiltration Over C2 Channel Using DNS

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/BIND]]

## Tags

- confirmation
- dns
- exfiltration

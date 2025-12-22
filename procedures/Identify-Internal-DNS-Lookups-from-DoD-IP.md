---
tags:
  - dns
  - internal-ip
  - whois
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/identify-dns-lookup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T03:53:38.023Z'
sub_techniques: []
id: 003048c5-b25a-46cc-807f-96585dfc4caf
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Identify-Internal-DNS-Lookups-from-DoD-IP

## Summary

This procedure analyzes DNS resolution attempts in collaborator logs to identify internal IP addresses originating from DoD networks, confirming exposure of backend infrastructure.

## Description

SSRF often triggers DNS lookups from internal servers when resolving attacker domains. By examining these in Burp Collaborator and cross-referencing with WHOIS, attackers can map government-owned IPs and infer network topology.

## Requirements

1. Access to collaborator DNS logs
2. WHOIS lookup tool or service
3. Knowledge of target organization (DoD)

## Defense

Defensive measures and detection strategies:

- Restrict DNS queries from servers to trusted resolvers
- Monitor for anomalous DNS traffic to external domains
- Implement DNS sinkholing for malicious payloads

## Objectives

1. Pinpoint internal source IPs
2. Verify ownership via public records
3. Map potential internal assets

## Instructions

### Step 1: Review DNS Logs

**Context**: Check for DNS A/AAAA queries in collaborator interactions.

**Command** ([[commands/identify-dns-lookup]]):
```bash
# Manual log review or whois 214.72.0.2
whois 214.72.0.2
```

> Output shows IP owned by U.S. Department of Defense, confirming internal origin.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Vulnerability Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/identify-dns-lookup]]

## Tools Used


## Tags

- dns
- internal-ip
- whois

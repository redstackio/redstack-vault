---
id: p2b3c4d5-e6f7-8901-bcde-f2345678901
tags:
  - whois
  - domain-check
  - availability
type: procedure
tools: []
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/whois-domain-check]]'
verified: false
platforms:
  - Cloud
  - Azure
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Vulnerability Scanning]]'
updated_at: '2025-12-14T04:51:26.527Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Vulnerability Scanning]]'
---
# Verify Unclaimed Domain Availability

## Summary

This procedure checks if a domain pointed to by a CNAME record is registered or available for takeover, focusing on outdated cloud services like Azure endpoints.

## Description

After identifying a CNAME to ████ (an Azure endpoint), verify its status to confirm takeover feasibility. This step prevents false positives and assesses risk in environments with legacy cloud configs.

## Requirements

1. WHOIS client installed
2. Access to domain registrars' search tools
3. Knowledge of the target domain from DNS query

## Defense

Defensive measures and detection strategies:

- Monitor expired domains via Azure Resource Manager alerts
- Use automated scripts to scan for dangling records weekly
- Integrate with certificate transparency logs for early detection

## Objectives

1. Confirm domain is unclaimed
2. Gather registration details if any
3. Evaluate takeover potential

## Instructions

### Step 1: Perform WHOIS Lookup

**Context**: Query WHOIS database for registration status.

**Command** ([[commands/whois-domain-check]]):
```bash
whois ████.azurewebsites.net
```

> Output: If available, no registrant; if expired, note deletion date.

### Step 2: Manual Registrar Check

**Context**: Cross-verify on registrar sites like GoDaddy.

No command; use browser to search the domain and check availability status.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Vulnerability Scanning]] Active Scanning: Vulnerability Scanning

### Sub-Techniques


## Commands Used

- [[commands/whois-domain-check]]

## Tools Used


## Tags

- [[WHOIS]]
- [[domain-check]]

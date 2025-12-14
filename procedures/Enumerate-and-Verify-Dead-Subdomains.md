---
tags:
  - subdomain-enumeration
  - takeover-verification
  - dns
type: procedure
tools:
  - '[[tools/subfinder]]'
  - '[[tools/tko-subs]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/subfinder-enumerate-subdomains]]'
  - '[[commands/tko-subs-check-takeover]]'
verified: false
platforms:
  - Linux
  - macOS
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Hardware]]'
updated_at: '2025-12-14T04:51:26.780Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: d22539a3-0193-48fc-a22b-a4f6599b0a07
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Hardware]]'
---
# Enumerate-and-Verify-Dead-Subdomains

## Summary

This procedure enumerates subdomains of a target domain and verifies which ones are dead or eligible for takeover by checking if they point to decommissioned cloud resources like Azure endpoints.

## Description

Attackers use passive and active enumeration to build a list of subdomains, then validate takeover potential by probing DNS resolutions. In the scenario, this targets domains with stale Azure Traffic Manager records. Outcomes include a filtered list of claimable subdomains. Requires Go-based tools installed.

## Requirements

1. subfinder and tko-subs installed via Go
2. Target domain and list of subdomains from prior recon
3. Network access for DNS queries

## Defense

Defensive measures and detection strategies:

- Enforce strict DNS TTL and automate cleanup of decommissioned resources
- Monitor for anomalous DNS queries using SIEM tools like Splunk
- Use subdomain enumeration defenses like rate-limiting DNS responses

## Objectives

1. Generate comprehensive subdomain list
2. Identify dead cloud pointers
3. Confirm takeover eligibility

## Instructions

### Step 1: Enumerate Subdomains

**Context**: Use subfinder to discover all subdomains passively from various sources.

**Command** ([[commands/subfinder-enumerate-subdomains]]):
```bash
subfinder -d starbucks.com -o subdomains.txt
```

> This queries certificate transparency logs, search engines, and more to output a file with subdomains like svcardproxydevus.starbucks.com.

### Step 2: Check for Takeover Eligibility

**Context**: Feed the subdomain list into tko-subs to verify dead endpoints.

**Command** ([[commands/tko-subs-check-takeover]]):
```bash
tko-subs -l subdomains.txt
```

> Outputs status for each, e.g., "svcardproxydevus.starbucks.com points to dead Azure resource via trafficmanager.net".

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Hardware]] Gather Victim Host Information: Domains

### Sub-Techniques


## Commands Used

- [[commands/subfinder-enumerate-subdomains]]
- [[commands/tko-subs-check-takeover]]

## Tools Used

- [[tools/subfinder]]
- [[tools/tko-subs]]

## Tags

- [[subdomain-enumeration]]
- [[DNS]]

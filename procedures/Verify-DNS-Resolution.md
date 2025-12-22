---
tags:
  - dns
  - resolution
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - DNS
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:51:10.711Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f44484f9-60ca-448e-95a2-e92b0b404bb7
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-DNS-Resolution

## Summary

This procedure uses DNS queries to confirm the resolution of a subdomain, revealing CNAME and A records that indicate a dangling configuration.

## Description

For podcasts.slack-core.com, verification shows it resolves to redirect.feedpress.me (CNAME) and 5.135.16.40 (A), confirming the setup points to an unclaimed Feed.Press service without active control.

## Requirements

1. DNS resolver access (e.g., public like 8.8.8.8)
2. Target subdomain name
3. Basic command-line tools

## Defense

Defensive measures and detection strategies:

- Log and alert on anomalous DNS queries
- Use internal DNS monitoring to track resolution changes
- Implement rate limiting on DNS queries

## Objectives

1. Validate DNS record types
2. Identify IP endpoints
3. Confirm vulnerability prerequisites

## Instructions

### Step 1: Perform DNS Lookup

**Context**: Query the full DNS details for the subdomain.

Execute [[commands/dig-dns-lookup]]:

```bash
dig podcasts.slack-core.com
```

> Explanation: Queries A and CNAME records, showing server (e.g., 8.8.8.8), timestamp, and resolution to CNAME redirect.feedpress.me. and A 5.135.16.40.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]] Reconnaissance

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques


## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[DNS]]
- [[resolution]]

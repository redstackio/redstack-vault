---
tags:
  - data-exfiltration
  - monitoring
type: procedure
tools:
  - '[[tools/xsshunter]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:29:20.210Z'
sub_techniques: []
id: 34abba49-c52a-4ee5-85a6-98aa1cfe31ba
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Monitor-and-Capture-XSS-Execution

## Summary

This procedure monitors the external XSS service for payload execution reports, capturing stolen admin cookies, IPs, and leaked user data.

## Description

Using XSS Hunter, this step collects telemetry from triggered payloads, including HTTP requests with cookies, user-agent, IP, and any DOM-extracted data like emails. Requires prior hunt setup; outcomes enable further attacks like session hijacking.

## Requirements

1. Active XSS Hunter dashboard access
2. Payload domain configured correctly
3. Understanding of captured data formats

## Defense

Defensive measures and detection strategies:

- Block external domains in CSP and network filters
- Inspect outbound traffic for anomalous beacons to unknown hosts
- Use SIEM to alert on script loads from untrusted sources

## Objectives

1. Receive confirmation of XSS success
2. Collect admin credentials and PII
3. Analyze for additional exploitation

## Instructions

### Step 1: Access Monitoring Dashboard

**Context**: Log in to view hunt status and hits.

**Instructions**: Navigate to xsshunter.com dashboard for the specific hunt.

> Browser access. Expected output: Dashboard showing hunt details.

### Step 2: Review Captured Data

**Context**: Analyze reports for stolen information.

**Instructions**: Examine hit logs for IP, cookies (e.g., session IDs), headers, and leaked content like user lists.

> Manual review. Expected output: Detailed exfiltration data.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/xsshunter]]

## Tags

- [[data-exfiltration]]
- [[monitoring]]

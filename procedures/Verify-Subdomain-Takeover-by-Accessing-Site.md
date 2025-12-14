---
id: proc-verify-takeover
tags:
  - verification
  - subdomain-takeover
  - dns
type: procedure
tools:
  - '[[tools/dig]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/dig-dns-lookup]]'
verified: false
platforms:
  - Web
  - Cloud
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T04:38:49.767Z'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Verify-Subdomain-Takeover-by-Accessing-Site

## Summary

This procedure confirms successful subdomain takeover by accessing the hijacked domain and verifying the deployed content is visible.

## Description

Post-deployment, navigate to the subdomain (e.g., http://d02-1-ag.productioncontroller.starbucks.com/) to load the attacker's site. Optionally, re-query DNS to ensure resolution. Target is web browser access; prerequisites include completed prior steps. Outcomes: Visual confirmation of control, assessing potential for further exploitation like data theft.

## Requirements

1. Completed deployment to claimed service
2. Web browser or curl for access
3. DNS propagation time allowance

## Defense

Defensive measures and detection strategies:

- Set up domain monitoring tools like Certificate Transparency logs or DNS change alerts
- Use browser security features to warn on unexpected content
- Regularly test subdomains for takeover using tools like subjack

## Objectives

1. Validate DNS hijacking success
2. Confirm content delivery on trusted domain
3. Identify any propagation delays or issues

## Instructions

### Step 1: Re-Query DNS

**Context**: Ensure the subdomain now resolves to the claimed service.

**Command** ([[commands/dig-dns-lookup]]):
```bash
dig d02-1-ag.productioncontroller.starbucks.com
```

> Output should now show A records or successful resolution to the Azure IP, not NXDOMAIN.

### Step 2: Access the Site

**Context**: Load the webpage to view deployed content.

**Instructions**: Open http://d02-1-ag.productioncontroller.starbucks.com/ in a browser. The POC or malicious page should appear, confirming takeover.

> If it fails, wait for DNS TTL (up to 1 hour) and retry.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Active Scanning]] Active Scanning

### Sub-Techniques

- None

## Commands Used

- [[commands/dig-dns-lookup]]

## Tools Used

- [[tools/dig]]

## Tags

- [[verification]]
- [[subdomain-takeover]]
- [[DNS]]

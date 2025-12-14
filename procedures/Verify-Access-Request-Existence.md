---
id: proc-uuid-verify
tags:
  - exfiltration
  - verification
  - related-vulnerability
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/exfiltrate-access-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Data from Local System]]'
updated_at: '2025-12-14T17:28:59.061Z'
skill_level: intermediate
impact_level: medium
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Data from Local System]]'
---
# Verify-Access-Request-Existence

## Summary

This procedure uses a related vulnerability to exfiltrate and verify the existence of a user access request in the DoD system's database by supplying its ID, confirming creation or deletion impacts.

## Description

Leveraging another reported vulnerability (HackerOne #1489470), this sends a POST to https://██████/██████████ with encoded parameters to dump request details from the database. It's optional for validation before/after deletion. Assumes network access; outcomes include request data if present or empty response if deleted/absent. This aids in proving exploitation success but increases detection risk due to data exfiltration.

## Requirements

1. Known request ID to verify
2. Network access to the exfiltration endpoint
3. curl for POST requests

## Defense

Defensive measures and detection strategies:

- Patch the referenced exfiltration vulnerability (see https://hackerone.com/reports/1489470)
- Implement data loss prevention (DLP) rules on API endpoints to block unauthorized queries
- Alert on repeated exfiltration attempts with varying IDs

## Objectives

1. Exfiltrate request details to confirm existence post-creation
2. Verify deletion by checking for empty responses
3. Assess impact of broken access controls

## Instructions

### Step 1: Prepare Parameters

**Context**: Set the ID in the payload for the target request.

Replace '██████████' with the ID (e.g., 12345) and ensure URL encoding.

### Step 2: Execute Exfiltration

**Context**: POST to the endpoint to retrieve request data if it exists.

**Command** ([[commands/exfiltrate-access-request]]):
```bash
curl https://██████/██████████ -X POST -data="url=%2F████&██████████=████████" -k
```

> This exploits the related vuln to dump the request. If present, output includes details like user info; if deleted, empty body or error.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]] Collection

### Techniques

- [[Data from Local System]] Data from Local System (adapted for web DB exfil)

### Sub-Techniques


## Commands Used

- [[commands/exfiltrate-access-request]]

## Tools Used


## Tags

- [[Exfiltration]]
- [[verification]]
- [[related-vulnerability]]

---
tags:
  - api-bypass
  - auth-bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-create-staff]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[External Remote Services]]'
updated_at: '2025-12-14T17:32:57.974Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 6d482f50-8a01-4a85-b4f0-37675b164041
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[External Remote Services]]'
---
# Create Unauthorized Staff Account via API

## Summary

Exploit unauthenticated POST /api/staff to create staff accounts using leaked token.

## Description

No auth on endpoint allows POST with X-Token: 8e9998ee3137ca9ade8f372739f062c1 and staff_id=STF:84DJKEIP38 (from Twitter barcode), creating sandra.allison account.

## Requirements

1. API token
2. Staff ID value
3. HTTP client like curl or Burp

## Defense

Defensive measures: Require auth headers, validate staff_id; Detection: Log unauthorized POSTs to admin endpoints.

## Objectives

1. Submit creation request
2. Gain staff access
3. Expected outcome: New account

## Instructions

### Step 1: Send Creation Request

**Context**: Use token to bypass auth.

**Command** ([[commands/curl-create-staff]]):
```bash
curl -X POST 'https://api.bountypay.h1ctf.com/api/staff' -H 'X-Token: 8e9998ee3137ca9ade8f372739f062c1' -d 'staff_id=STF:84DJKEIP38'
```

> Expected output: Success with account details.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[External Remote Services]] External Remote Services

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-create-staff]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- api-bypass
- auth-bypass

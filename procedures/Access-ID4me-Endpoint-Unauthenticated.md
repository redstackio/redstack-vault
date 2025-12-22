---
tags:
  - nextcloud
  - id4me
  - access-control
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-access-id4me-endpoint]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
id: dbeab1c5-b8c3-4f2b-9fac-559e490e3c86
created_at: '2025-12-13T09:01:26.588Z'
updated_at: '2025-12-13T09:01:26.588Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Access ID4me Endpoint Unauthenticated

## Summary

This procedure accesses the ID4me endpoint directly as an unauthenticated user, exploiting the fact that disabling hides only the button but not the controllers.

## Description

By navigating to /apps/user_oidc/id4me, attackers can reach the active endpoint, allowing further exploitation for account creation.

## Requirements

1. Access to Nextcloud server URL
2. Browser or curl
3. user_oidc app installed

## Defense

Defensive measures and detection strategies:

- Implement proper access controls to disable endpoints fully
- Monitor HTTP logs for access to sensitive paths

## Objectives

1. Bypass disabled feature
2. Reach authentication interface
3. Confirm endpoint availability

## Instructions

### Step 1: Navigate to Endpoint

**Context**: Open the URL in a browser or via command.

**Command** ([[commands/curl-access-id4me-endpoint]]):
```bash
curl http://localhost:8080/apps/user_oidc/id4me
```

> This returns the ID4me page if vulnerable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-access-id4me-endpoint]]

## Tools Used



## Tags

- [[id4me]]
- [[access-control]]

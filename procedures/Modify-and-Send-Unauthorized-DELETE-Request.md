---
id: proc-modify-unauth-delete
tags:
  - request-modification
  - unauthorized-deletion
  - fabric-io
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Persistence]]'
commands:
  - '[[commands/fabric-delete-member-original]]'
  - '[[commands/fabric-delete-member-modified]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:28:58.770Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Persistence]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Modify-and-Send-Unauthorized-DELETE-Request

## Summary

Tamper with the intercepted DELETE request in Burp to target a different organization and member, exploiting retained ex-admin access to perform unauthorized removal.

## Description

Using the captured request from HackerOrg, replace parameters to point to VictimOrg and Victimmember. Forward via Burp Repeater; the server accepts due to unrevoked permissions. This core exploit highlights the broken access control at the /api/v3/accounts/{account_id}/organizations/{org_id}/leave endpoint.

## Requirements

1. Intercepted request in Burp Repeater
2. Victim Org and Member IDs
3. Active ex-admin session

## Defense

Defensive measures and detection strategies:

- Validate org membership in every API call
- Log cross-org requests and alert on anomalies
- Use short-lived JWT tokens with explicit revocation

## Objectives

1. Bypass authorization checks
2. Achieve member deletion without UI access
3. Demonstrate privilege persistence

## Instructions

### Step 1: Modify Parameters

**Context**: Alter the request to target victim entities.

In Burp Repeater, change account_id to 552787195127ae16b8000987 and org_id to 54af7e07b8568e8c6a0001e. Retain auth headers.

**Expected Output**: Modified request: `DELETE /api/v3/accounts/552787195127ae16b8000987/organizations/54af7e07b8568e8c6a0001e/leave HTTP/1.1 Host: fabric.io`.

### Step 2: Send Request

**Context**: Execute the tampered request.

Click 'Send' in Burp; equivalent to executing [[commands/fabric-delete-member-modified]].

**Expected Output**: 200 OK response; no auth denial.

## MITRE ATT&CK Mapping

### Tactics

- [[Persistence]] Persistence

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/fabric-delete-member-original]]
- [[commands/fabric-delete-member-modified]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[request-modification]]
- [[unauthorized-deletion]]

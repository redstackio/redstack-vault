---
id: proc-mtn-edit-operational-data-001
tags:
  - data-manipulation
  - account-compromise
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:35.295Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Edit or Delete Cashier, Station, and Supervisor Data

## Summary

This procedure targets operational endpoints in the admin dashboard to view, edit, or delete data for cashiers, stations, and supervisors, compromising the application's backend management.

## Description

Specific endpoints for each entity type (/admin/cashiers, /admin/stations, /admin/supervisors) lack granular access controls, allowing full manipulation. This can disrupt operations or enable further escalation in the web environment.

## Requirements

1. Admin dashboard session
2. Entity-specific endpoint access
3. HTTP client for requests

## Defense

Defensive measures and detection strategies:

- Role-based access control (RBAC) for entity management
- Log all CRUD operations on operational data
- Backup and recovery for deleted records

## Objectives

1. Access entity lists
2. Perform edits or deletions
3. Disrupt or compromise operations

## Instructions

### Step 1: Access Cashier Endpoint

**Context**: GET the cashiers list and edit a record.

Example:

```bash
curl -X GET https://target-app.com/admin/cashiers \
  -H "Authorization: Bearer <session_token>"
```

> Expected output: List of cashier accounts.

### Step 2: Edit or Delete Entity

**Context**: Use PUT for edits or DELETE for removal (similar for stations/supervisors).

Example for delete:

```bash
curl -X DELETE https://target-app.com/admin/cashiers/456 \
  -H "Authorization: Bearer <session_token>"
```

> Expected output: 204 No Content on success.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[account-compromise]]
- [[data-manipulation]]

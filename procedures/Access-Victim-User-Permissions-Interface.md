---
id: d7634bdd-4ef3-4cab-9358-3e28ab475602
name: Access-Victim-User-Permissions-Interface
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:33:24.656Z'
tactics:
  - '[[Discovery]]'
techniques:
  - '[[Account Discovery]]'
sub_techniques: []
tags:
  - idor
  - access
commands: []
platforms:
  - Web
tools: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---

# Access-Victim-User-Permissions-Interface

## Summary

This procedure loads the unauthorized permissions editing interface for a victim user by manipulating the ID in the CrowdSignal edit request, exposing full user details.

## Description

Building on the IDOR, this interacts with the popup interface triggered by the invitation endpoint. The technical approach uses browser manipulation of the 'Edit' button's GET request. Target is the PHP endpoint without checks, leading to editable victim profile. Prerequisites: Authenticated session and victim ID.

## Requirements

1. Loaded team users page in browser
2. Developer tools for request interception
3. Victim ID from prior enumeration

## Defense

Defensive measures and detection strategies:

- Enforce role-based access control (RBAC) on edit endpoints
- Validate user-team membership before loading interfaces
- Rate-limit ID-based requests and monitor anomalies

## Objectives

1. Load editable permissions for unauthorized user
2. Expose victim details in UI
3. Set up for takeover action

## Instructions

### Step 1: Intercept Edit Request

**Context**: Modify the network request for user edit.

On the team users page, right-click 'Edit' on a team member, copy the request as curl, and replace ID with victim's.

> Expected output: Modified request ready.

### Step 2: Load Popup Interface

**Context**: Submit the request to display victim permissions.

Paste and execute the modified request in terminal or dev tools console.

> Popup opens with victim's email and permissions form.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- idor
- access


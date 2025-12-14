---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - idor
  - unauthorized-access
  - graphql
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:25:52.804Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Manipulate-User-ID-for-Unauthorized-Access
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T00:00:00Z
updated_at: 2023-10-01T00:00:00Z
tactics: [[Discovery]]
techniques: [[Account Discovery]], [[Exploit Public-Facing Application]]
sub_techniques: []
tags: idor, unauthorized-access, graphql
commands: []
platforms: Web
tools: [[tools/Burp-Suite]]
---

# Manipulate-User-ID-for-Unauthorized-Access

## Summary

This procedure exploits an IDOR vulnerability by altering the user ID parameter in a GraphQL request to Semrush's Content Outline Builder, enabling unauthorized retrieval of other users' sensitive information.

## Description

Targeting the GraphQL API in Semrush's Content Outline Builder, this procedure modifies the `userId` variable in the query payload after intercepting it. The attack scenario assumes an authenticated session but bypasses object-level authorization checks. Outcomes include exposure of user details like content outlines or profiles. The vulnerability stems from insufficient server-side validation of the user ID against the requester's permissions.

## Requirements

1. Identified GraphQL endpoint from prior reconnaissance
2. Authenticated session cookie or token
3. Proxy tool like Burp Suite for request modification

## Defense

Defensive measures and detection strategies:

- Implement indirect object references with server-side permission checks
- Log and alert on mismatched user IDs in requests
- Use GraphQL schema introspection limits and query validation

## Objectives

1. Bypass access controls to access another user's data
2. Retrieve sensitive information from Content Outline Builder
3. Validate the IDOR impact without exploitation evidence

## Instructions

### Step 1: Intercept the Original Request

**Context**: Capture a legitimate GraphQL request for your own user data.

Trigger a user data query in the Content Outline Builder and intercept it via Burp Suite.

Examine the payload, e.g., query: "query UserData($userId: ID!) { user(id: $userId) { ... } }" with variables: {"userId": "123"}.

**Expected Output**: Original request and response with your data.

### Step 2: Modify and Replay

**Context**: Change the user ID to target another account and submit the request.

Edit the variables to {"userId": "124"} (or another known/test ID), ensuring headers like Authorization remain intact.

Forward the request to the server.

**Expected Output**: Response with data for user 124, including additional sensitive fields.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[idor]]
- [[unauthorized-access]]
- [[graphql]]

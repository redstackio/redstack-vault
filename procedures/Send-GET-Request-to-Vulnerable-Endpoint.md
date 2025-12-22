---
id: p5e6f7g8-h9i0-1234-efgh-567890123456
tags:
  - idor
  - api-request
  - exploitation
type: procedure
tools:
  - '[[tools/Web-Browser]]'
tactics:
  - '[[Discovery]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:32:28.838Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Send-GET-Request-to-Vulnerable-Endpoint

## Summary

This procedure sends a GET request to the IDOR-vulnerable /api/v1/permission/user/{USER_ID}/ endpoint using the guest JWT token to retrieve unauthorized user data.

## Description

The endpoint lacks proper authorization checks, allowing any authenticated user (including guests) to access data by specifying an arbitrary USER_ID. This direct object reference bypasses intended permissions, exposing personal information.

## Requirements

1. Valid JWT token from guest login
2. Tool for sending HTTP requests (browser or proxy)
3. Known user ID to target (e.g., 1 or 2 from test users)

## Defense

Defensive measures and detection strategies:

- Implement server-side ID validation against requesting user's permissions
- Rate-limit endpoint requests
- Log anomalous access patterns to user objects

## Objectives

1. Manipulate USER_ID parameter
2. Include JWT in Authorization header
3. Receive target user's sensitive data

## Instructions

### Step 1: Prepare the Request URL

**Context**: Construct the endpoint with target ID.

Set URL to http://localhost:8000/api/v1/permission/user/{USER_ID}/, replace {USER_ID} with e.g., 1.

> Targets specific user. Expected output: Formatted URL ready.

### Step 2: Add JWT Header

**Context**: Authenticate the request.

Add header: Authorization: Bearer {token}, where {token} is the copied JWT.

> Ensures request is processed. Expected output: Header set.

### Step 3: Send GET Request

**Context**: Execute the request via browser or tool.

Send GET to the prepared URL with header.

> Bypasses checks. Expected output: 200 OK with user JSON (email, name).

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Web-Browser]]

## Tags

- idor
- api-request
- exploitation

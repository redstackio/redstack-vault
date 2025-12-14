---
id: proc-rocket-discover-admin-email
tags:
  - user-discovery
  - admin-enumeration
  - rocket-chat
type: procedure
tools:
  - '[[tools/Custom-Python-Script-for-Rocket-Chat-Exploitation]]'
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
updated_at: '2025-12-14T17:32:58.333Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Discover-Admin-Email-Address-in-Rocket-Chat

## Summary

This procedure uses a custom script to query Rocket.Chat endpoints and identify the admin user's email address, targeting it for reset token extraction in the account takeover chain.

## Description

Leveraging authenticated tokens, the script interacts with user search or list APIs in Rocket.Chat to enumerate users and filter for admin roles. This occurs in a web-based environment vulnerable to information disclosure. Outcomes include the admin email, enabling targeted exploitation. Requires prior token extraction.

## Requirements

1. Extracted rc_uid and rc_token
2. Custom Python script for API queries
3. Access to Rocket.Chat API endpoints

## Defense

Defensive measures and detection strategies:

- Restrict user list endpoints to admin-only access
- Rate-limit API queries to prevent enumeration
- Audit logs for unusual user search patterns

## Objectives

1. Enumerate users to find admin
2. Extract admin email for targeting
3. Maintain stealth in discovery

## Instructions

### Step 1: Prepare Script

**Context**: Set up the Python script with tokens.

Edit the custom Python script to include rc_uid and rc_token as variables.

### Step 2: Query User Endpoint

**Context**: Send authenticated request to discover users.

Run the script to call /api/v1/users.list or similar endpoint, parsing response for admin roles (e.g., is_admin: true) and extracting email.

> Example script snippet: Use requests library with headers {'X-Auth-Token': rc_token, 'X-User-Id': rc_uid}, GET /api/v1/users.list, filter JSON for admin.

Expected: Admin email like "admin@example.com".

### Step 3: Verify Email

**Context**: Confirm the email belongs to admin.

Cross-check with known admin indicators or re-query specific user.

> Expected: Confirmed admin email ready for next step.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Python-Script-for-Rocket-Chat-Exploitation]]

## Tags

- [[user-discovery]]
- [[admin-enumeration]]

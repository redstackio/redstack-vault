---
id: proc-rocket-extract-reset-token
tags:
  - regex-exploitation
  - blind-search
  - account-takeover
  - rocket-chat
type: procedure
tools:
  - '[[tools/Custom-Python-Script-for-Rocket-Chat-Exploitation]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:32:58.332Z'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Extract-Admin-Password-Reset-Token-via-Blind-Regex-Search

## Summary

This procedure exploits a vulnerability in Rocket.Chat by using a blind regex search mechanism to retrieve the admin's password reset token, bypassing traditional access controls and enabling account takeover.

## Description

The attack targets a flawed endpoint in Rocket.Chat that allows low-privilege users to perform regex searches on sensitive data like reset tokens without SQL injection. Using the admin email and tokens, the script iteratively tests regex patterns to extract the token. This web-based exploit leads to privilege escalation. Requires discovered admin email.

## Requirements

1. Admin email address
2. rc_uid and rc_token
3. Custom Python script for regex operations
4. Knowledge of regex for blind extraction

## Defense

Defensive measures and detection strategies:

- Sanitize and restrict regex usage in API endpoints
- Implement proper authorization checks for reset token access
- Monitor for anomalous regex queries in application logs

## Objectives

1. Retrieve admin reset token via blind search
2. Enable password reset for takeover
3. Escalate to admin privileges

## Instructions

### Step 1: Configure Script for Target

**Context**: Set admin email in the script.

Update the Python script with the admin email and tokens, preparing the regex search payload.

### Step 2: Initiate Blind Regex Search

**Context**: Perform iterative searches to build the token.

Execute the script to send requests to the vulnerable endpoint (e.g., password reset search), using regex patterns like . to match characters one by one, observing response differences (blind oracle).

> Example: Script uses requests to POST to /api/v1/passwordReset with regex payload in search field, e.g., {'email': admin_email, 'search': '^tokenprefix.*$'}, analyzing timing or content length for matches.

Expected: Full token reconstructed, e.g., "reset_token_abc123".

### Step 3: Validate Token

**Context**: Use token to confirm usability.

Send a request to the reset endpoint with the extracted token to verify it triggers a password change option.

> Expected: Successful reset initiation, confirming token validity.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Custom-Python-Script-for-Rocket-Chat-Exploitation]]

## Tags

- [[regex-exploitation]]
- [[blind-search]]

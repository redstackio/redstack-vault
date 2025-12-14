---
id: p4d5e6f7-g8h9-0123-defg-4567890123
tags:
  - unauthorized-access
  - exfiltration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Account Discovery]]'
updated_at: '2025-12-14T17:25:23.655Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Replay-Modified-Request-to-Access-Unauthorized-Profile

## Summary

This procedure sends the tampered request to the server, retrieving the target user's profile data due to the IDOR flaw.

## Description

Forwarding the modified request to the profile endpoint results in the server responding with the target user's data (ID 4820036), as no authorization verifies ownership. This exposes sensitive information in the DoD application.

## Requirements

1. Modified request from prior step
2. Active proxy session
3. Target ID confirmed valid

## Defense

Defensive measures and detection strategies:

- Enforce strict access controls on profile endpoints
- Audit logs for cross-user access attempts
- Use role-based access control (RBAC)

## Objectives

1. Execute the tampered request
2. Receive and view unauthorized data
3. Confirm IDOR success

## Instructions

### Step 1: Forward Request

**Context**: Send the altered request to the server.

In Burp Repeater, click 'Send' on the modified profile request.

> Expected output: HTTP 200 response with profile HTML/JSON for target user.

### Step 2: Inspect Response

**Context**: Analyze the returned data for sensitivity.

View the response body in Burp to extract user information.

> Expected output: Target user's details (e.g., name, email, sensitive DoD info) displayed.

### Step 3: Validate Unauthorized Access

**Context**: Ensure it's not the attacker's own data.

Compare response to original profile; confirm mismatch.

> Expected output: Data belongs to ID 4820036, not 4820038.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[unauthorized-access]]

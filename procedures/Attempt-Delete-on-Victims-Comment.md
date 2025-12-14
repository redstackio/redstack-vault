---
id: proc-attempt-delete-victim
tags:
  - idor
  - deletion
  - disclosure
  - web
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
updated_at: '2025-12-14T17:25:33.664Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Attempt-Delete-on-Victims-Comment

## Summary

This procedure exploits IDOR by sending a DELETE request to a victim's comment ID, triggering a captcha or validation failure that nonetheless discloses the full comment content in the HTTP response.

## Description

The RGhost DELETE /comments/{id} endpoint processes requests from any authenticated user without verifying ownership, returning the comment details in the response body before applying captcha checks. This allows attackers to read private comments intended only for the owner, facilitating targeted information gathering or harassment.

## Requirements

1. Authenticated attacker session
2. Burp Suite with Repeater tab open
3. Victim's comment ID identified
4. HTTPS access to RGhost

## Defense

Defensive measures and detection strategies:

- Enforce strict ownership checks before any response generation
- Avoid including sensitive data in error responses
- Implement captcha earlier in the request pipeline
- Monitor for delete attempts on non-owned objects

## Objectives

1. Disclose victim's comment content via response leakage
2. Confirm vulnerability persistence across operations
3. Collect data for broader enumeration

## Instructions

### Step 1: Prepare DELETE Request

**Context**: Use Burp to craft or intercept a DELETE request targeting the victim's ID.

Set up in Repeater:

```http
DELETE /comments/{victim_id} HTTP/1.1
Host: rghost.net
Authorization: Bearer [token]
Content-Type: application/json

{}
```

> Expected: Request ready for submission.

### Step 2: Send and Observe Response

**Context**: Execute the request to force content revelation.

Click 'Send' in Repeater.

> Expected: Response like 403 with body {"comment": "full victim text", "captcha_required": true}.

### Step 3: Extract Content

**Context**: Parse the response for leaked data.

Copy the comment field from the JSON response.

> Expected: Raw comment text harvested for analysis.

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

- idor
- disclosure

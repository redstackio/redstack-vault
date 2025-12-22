---
id: proc-attempt-edit-victim
tags:
  - idor
  - edit
  - disruption
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
updated_at: '2025-12-14T17:25:33.659Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
  - '[[Exploit Public-Facing Application]]'
---
# Attempt-Edit-on-Victims-Comment

## Summary

This procedure uses IDOR to attempt editing a victim's comment, revealing the original content in the response while failing to save changes, and potentially disabling the victim's client-side edit functionality for harassment.

## Description

RGhost's edit /comments/{id} endpoint echoes the original comment in responses during validation, without ownership checks. Attackers can view private text and, in some cases, trigger UI changes that lock the victim's edit option, though server-side persistence is prevented by checks.

## Requirements

1. Active authenticated session
2. Burp Suite Repeater for request modification
3. Victim's comment ID and approximate content knowledge
4. Access to the web interface for observing UI effects

## Defense

Defensive measures and detection strategies:

- Validate ownership before echoing content in responses
- Sanitize error responses to exclude full object data
- Client-side: Use session-bound IDs to prevent tampering effects
- Alert on repeated edit failures from unauthorized users

## Objectives

1. View victim's original comment content
2. Disrupt victim's editing experience
3. Demonstrate broader IDOR impact

## Instructions

### Step 1: Capture Edit Request

**Context**: Perform a legitimate edit to get a template request.

Intercept in Burp Proxy and send to Repeater.

> Expected: PUT request with content payload.

### Step 2: Target Victim's ID and Alter Payload

**Context**: Swap ID and modify content slightly to trigger response.

Edit in Repeater:

```http
PUT /comments/{victim_id} HTTP/1.1
Host: rghost.net
Authorization: Bearer [token]
Content-Type: application/json

{"content": "Modified victim's text (Y to X)"}
```

> Expected: Response shows original before failure.

### Step 3: Check for UI Disruption

**Context**: Observe if victim's interface is affected.

Submit and then view the victim's thread in browser.

> Expected: Edit button disabled for victim; original content logged.

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
- harassment

---
id: proc-tamper-comment-id
tags:
  - idor
  - tampering
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
updated_at: '2025-12-14T17:25:33.668Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Account Discovery]]'
---
# Tamper-with-Comment-ID-in-Requests

## Summary

This procedure involves intercepting and modifying HTTP requests to the RGhost comment endpoints by replacing the comment ID with a victim's ID, allowing an authenticated attacker to attempt unauthorized access to other users' comments without proper ownership validation.

## Description

In the RGhost web application, comment IDs are sequential integers exposed in URLs and request bodies. Lacking server-side checks for user ownership, tampering with these IDs in authenticated requests to DELETE /comments/ or edit /comments/ enables viewing of private comment data in responses. This is a classic IDOR exploitation, discovered via manual request manipulation, leading to information disclosure even when actions fail due to additional protections like captchas.

## Requirements

1. Authenticated session to RGhost with valid user credentials
2. Burp Suite installed and proxy configured to intercept browser traffic
3. Knowledge of a victim's comment ID (e.g., from public threads or prior enumeration)
4. Network access to the RGhost application

## Defense

Defensive measures and detection strategies:

- Implement server-side ownership validation on all comment operations using user-session binding
- Rate-limit requests to comment endpoints to prevent enumeration
- Log and monitor anomalous request patterns, such as sequential ID tampering from single IPs
- Use indirect object references (e.g., hashed IDs) instead of sequential integers

## Objectives

1. Gain unauthorized access to a specific victim's comment for viewing
2. Confirm IDOR vulnerability by observing content in failed responses
3. Set up for further enumeration or disruption

## Instructions

### Step 1: Intercept Legitimate Request

**Context**: Start by performing a normal action (e.g., delete your own comment) to capture a baseline request in Burp Suite Proxy.

Send the request through Burp and forward it to Repeater for modification. No specific command; use Burp's UI to intercept.

> Expected: Captured request like DELETE /comments/{attacker_id} with Authorization header.

### Step 2: Modify Comment ID

**Context**: Replace the ID with a known victim's comment ID to test access.

In Burp Repeater, edit the path or body:

```http
DELETE /comments/{victim_id} HTTP/1.1
Host: rghost.net
Authorization: Bearer [token]
```

> Expected: Response body includes victim's comment text, confirming disclosure.

### Step 3: Validate Disclosure

**Context**: Check if the response leaks sensitive data despite action failure.

Submit the request and inspect the JSON response for comment content fields.

> Expected: Fields like {"content": "victim's text"} visible, even with error messages.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Account Discovery]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- idor
- tampering

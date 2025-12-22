---
id: proc-imgur-modify-sid-93154
tags:
  - csrf
  - web
  - bypass
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:27:03.363Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Modify Request to Bypass Sid Token

## Summary

This procedure edits an intercepted POST request to remove the 'Sid' CSRF token, allowing forged submission to Imgur's abuse reporting endpoint.

## Description

In exploiting the CSRF vulnerability, use the proxy to delete the 'Sid' token from the request body, stripping validation while preserving other parameters like meme ID and category. This targets Imgur's web application, where the server fails to enforce token checks. Requires an intercepted request; results in a bypassable submission that mimics an authenticated action.

## Requirements

1. Intercepted POST request in proxy tool.
2. Knowledge of request format (multipart/form-data or x-www-form-urlencoded).
3. Proxy with request editing capabilities.

## Defense

Defensive measures and detection strategies:

- Validate all CSRF tokens server-side with uniqueness and expiration.
- Reject requests missing or invalid tokens with 403 Forbidden.
- Audit logs for requests without tokens.

## Objectives

1. Remove 'Sid' and any ancillary validation fields.
2. Maintain request integrity for successful processing.
3. Test bypass without alerting the server.

## Instructions

### Step 1: Edit Request Body

**Context**: Locate and delete the token.

In Burp Suite Repeater or Inspector, find 'Sid=...' in POST data and delete the line.

> Optionally remove other session tokens if they block submission.

### Step 2: Preserve Essential Data

**Context**: Ensure the request remains valid.

Retain fields like 'report_category=abusive' and 'meme_id=ieTEJEd'.

> Forward the edited request to proceed.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[csrf]]
- [[web]]
- [[bypass]]

---
tags:
  - auth-bypass
  - anonymous-access
  - header-removal
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:25:47.745Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 06997226-b489-4ed7-b00d-eda7acd18448
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Bypass-Authentication-to-Download-Attachments

## Summary

This procedure removes the Authorization header from attachment download requests, exploiting the endpoint's failure to enforce authentication for anonymous access to any file.

## Description

The /attachments/{ID} endpoint does not validate the Authorization header, serving files to unauthenticated requests. After modifying the ID, deleting the header allows anyone to download private attachments without credentials, amplifying the IDOR impact.

## Requirements

1. Modified ID request ready in Burp Repeater
2. Original request with Authorization header present
3. Target IDs confirmed valid

## Defense

Defensive measures and detection strategies:

- Mandate and validate Authorization headers on all endpoints
- Implement token-based auth with scope checks for attachments
- Alert on requests missing auth headers to sensitive paths

## Objectives

1. Confirm auth is not required for downloads
2. Enable fully anonymous exploitation
3. Demonstrate exposure of all attachments

## Instructions

### Step 1: Locate Authorization Header

**Context**: Identify the header to remove.

In Repeater, inspect raw request for Authorization: Bearer <token>.

> Review. Expected: Header found in baseline request.

### Step 2: Remove Header

**Context**: Strip auth to test bypass.

Delete the entire Authorization line and send the request.

> Edit and send. Expected: 200 OK with file content.

### Step 3: Verify Anonymous Access

**Context**: Test without any session.

Replay multiple times; use curl equivalent for external validation: curl -X GET https://ameim.bs2dl.yy.com/attachments/359912920 -H "X-Signal-Agent: OWA" --output file.jpg

> Expected: File downloads without auth errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[auth-bypass]]
- [[anonymous-access]]

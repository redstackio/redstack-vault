---
id: 123e4567-e89b-12d3-a456-426614174002
name: Craft-Malicious-Protocol-Relative-URL-for-Pathname
type: procedure
verified: false
submitted: true
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:02.233Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
tags:
  - ssrf
  - payload
platforms:
  - Node.js
  - JavaScript
tools:
  - '[[tools/undici]]'
commands: []
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---

# Craft-Malicious-Protocol-Relative-URL-for-Pathname

## Summary

This procedure crafts and injects malicious inputs such as protocol-relative or absolute URLs into the pathname option of undici.request to bypass origin restrictions and enable SSRF.

## Description

The vulnerability arises because undici does not properly validate pathname inputs, allowing strings like '//127.0.0.1' to be interpreted as a new origin rather than a path. This overrides the specified origin (e.g., http://example.com) and directs the request to internal addresses. The procedure assumes a vulnerable endpoint has been identified and focuses on payload creation and submission.

## Requirements

1. Identified vulnerable input point from prior reconnaissance
2. Testing environment or access to the application
3. Basic understanding of URL schemes

## Defense

Defensive measures and detection strategies:

- Implement pathname validation to reject absolute URLs (e.g., using URL constructor checks)
- Whitelist allowed path patterns
- Log and alert on requests with suspicious pathnames

## Objectives

1. Create effective SSRF payloads
2. Submit payloads without triggering errors
3. Confirm payload acceptance for next stage

## Instructions

### Step 1: Generate Payloads

**Context**: Design inputs that exploit the validation gap.

Craft strings like `pathname: '//127.0.0.1'` or `pathname: 'http://127.0.0.1'`.

> These will resolve to http://127.0.0.1/ when combined with the protocol.

### Step 2: Inject via Endpoint

**Context**: Deliver the payload through the user-controlled input.

If API-based, use a POST request with the malicious pathname value.

> Expected: Server processes the input without rejection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/undici]]

## Tags

- [[ssrf]]
- [[payload]]

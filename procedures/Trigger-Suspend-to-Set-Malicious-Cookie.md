---
id: uuid-trigger-suspend
tags:
  - xss
  - cookie
  - propagation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Pass the Hash]]'
updated_at: '2025-12-14T03:15:35.810Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Pass the Hash]]'
---
# Trigger-Suspend-to-Set-Malicious-Cookie

## Summary

This procedure activates a mandate suspension to set a signed cookie embedding the XSS payload, enabling potential cross-context exploitation.

## Description

Suspending a mandate triggers a response that sets a signed 'messages' cookie containing the owner's name (with payload). This cookie can propagate the XSS to other vectors, such as subdomain takeovers or header injections if combined with other flaws.

## Requirements

1. Stored payload in an active mandate
2. Access to suspension functionality

## Defense

Defensive measures and detection strategies:

- Sanitize cookie values before signing
- Validate cookie contents on set and read
- Rotate signing keys and monitor for tampering

## Objectives

1. Set cookie with embedded payload
2. Observe propagation potential
3. Demonstrate chained exploitation

## Instructions

### Step 1: Initiate Suspension

**Context**: Use the suspend action to trigger cookie setting.

**Instructions**: Click the suspend link, e.g., https://mobilevikings.be/en/account/easypay/287740/suspend/.

> Inspect the response headers for Set-Cookie with the payload; the cookie path is /, making it site-wide.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Pass the Hash]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- cookie
- propagation

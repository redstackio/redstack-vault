---
tags:
  - xss
  - validation
  - twitter
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: f5f8be5f-c698-4101-ad2b-be8e4d3184e6
created_at: '2025-12-14T03:16:14.475Z'
updated_at: '2025-12-14T03:16:14.475Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Poll-Publication-and-Server-Validation

## Summary

This procedure tests server-side validation by attempting to publish a poll with malicious payloads, confirming that protections prevent broader exploitation beyond self-XSS.

## Description

Server-side checks reject polls with obvious XSS patterns, such as `<img src=x onerror=alert(1)>`, by not displaying them in the feed despite creating a backend 'card'. Even subtle inputs like `<x>` are blocked, ensuring no cross-user impact. This step verifies the vulnerability's containment to the preview phase.

## Requirements

1. Poll with injected payload ready for submission
2. Twitter account with publishing permissions
3. Browser for observing responses

## Defense

Defensive measures and detection strategies:

- Apply server-side input validation and sanitization before storage
- Use allowlisting for permitted characters in poll options
- Audit publication logs for rejected payloads

## Objectives

1. Evaluate server rejection of malicious inputs
2. Confirm no publication to feed
3. Demonstrate impact limitations

## Instructions

### Step 1: Submit Poll for Publication

**Context**: Attempt to publish the poll containing the payload.

Complete the poll setup and click "Tweet" or publish button.

### Step 2: Analyze Response

**Context**: Review server behavior and feed for visibility.

Observe rejection for malicious inputs; test variants like `<x>` to check sanitization.

> Expected: Server creates but hides the card; no feed appearance, isolating to self-XSS.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[validation]]

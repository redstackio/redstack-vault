---
id: proc-send-request-001
tags:
  - request-forward
  - exploit-execution
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
updated_at: '2025-12-14T17:25:23.712Z'
skill_level: intermediate
impact_level: low
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Send-Modified-Request

## Summary

This procedure forwards the tampered POST request through Burp Suite to apply unauthorized changes to the target store's settings.

## Description

Submitting the modified request bypasses authorization due to the IDOR flaw, resulting in a successful update confirmed by a 302 redirect. The Rails app processes the request without validating ownership, altering the victim's column display for low stock variants.

## Requirements

1. Modified request prepared in Burp
2. Active session (authenticity_token valid)

## Defense

Defensive measures and detection strategies:

- Validate resource ownership server-side
- Audit 302 redirects for unexpected patterns

## Objectives

1. Execute the exploit request
2. Confirm server acceptance
3. Observe response

## Instructions

### Step 1: Forward in Burp

**Context**: Send the altered request to the server.

In Burp Repeater or Proxy, click 'Forward' or 'Send'.

> Expected output: Response headers including 302 Location: /dashboard or similar.

### Step 2: Check Response

**Context**: Verify no errors.

Inspect response body for success indicators.

> Expected output: No 403/401; redirect to updated page.

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

- [[exploit-execution]]

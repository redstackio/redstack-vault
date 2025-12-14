---
id: proc-paypalme-xss-safari-trigger
tags:
  - xss-execution
  - safari
  - user-interaction
type: procedure
tools:
  - '[[tools/Safari]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:38.023Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Clicking-Modal-Button-on-Safari

## Summary

This procedure executes the XSS payload in Safari by clicking the modal button, validating JavaScript injection and domain access for full cross-browser proof-of-concept.

## Description

With the Safari-adapted payload loaded, clicking 'X' triggers the href to run the direct javascript:alert(document.domain). This leverages the same validation flaw but accounts for Safari's stricter URI handling. Post-execution, it confirms the vulnerability's breadth, potentially allowing authenticated actions on paypal.com.

## Requirements

1. Loaded modal from Safari navigation.
2. Safari browser session.
3. Ability to click interactive elements.

## Defense

Defensive measures and detection strategies:

- Block javascript: in all browser contexts via server-side filtering.
- Enable Safari's XSS protection features.
- Detect repeated modal clicks with encoded payloads in analytics.
- Use SRI for scripts to prevent tampering.

## Objectives

1. Trigger and execute the injected code.
2. Display domain alert for verification.
3. Demonstrate exploit consistency across browsers.

## Instructions

### Step 1: Click the Button

**Context**: Activate the href to run the payload.

Click 'X' in the modal.

> Executes: javascript:alert(document.domain) (from decoded flow).

**Expected Output**: Alert shows domain.

### Step 2: Confirm Impact

**Context**: Check for execution without blocks.

Observe alert closure.

**Expected Output**: Successful run, no crashes.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Safari]]

## Tags

- [[xss-execution]]
- [[tools/Safari]]

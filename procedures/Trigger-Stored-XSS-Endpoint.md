---
id: proc-trigger-xss-856836
tags:
  - xss
  - trigger
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:20.968Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-Endpoint

## Summary

This procedure accesses the PyPi simple API endpoint to trigger the stored XSS payload injected via the requires_python field, leading to JavaScript execution in the victim's browser.

## Description

The endpoint /api/v4/projects/:id/packages/pypi/simple/:package_name generates HTML links for packages, inserting requires_python into data-requires-python without escaping. Visiting as an authenticated user (or public if enabled) executes the payload, potentially stealing session data, though CSP may block inline scripts initially.

## Requirements

1. Uploaded malicious package
2. Browser access to GitLab instance
3. Victim context (e.g., logged-in user visiting the endpoint)

## Defense

Defensive measures and detection strategies:

- Enable strict CSP with 'unsafe-inline' blocked
- Log and monitor endpoint accesses for anomalies
- Escape HTML attributes in presenters (e.g., .html_safe in Rails)

## Objectives

1. Execute injected JavaScript
2. Demonstrate client-side impact like alerts or data exfil
3. Highlight persistence of stored payload

## Instructions

### Step 1: Access the Simple Endpoint

**Context**: Open the generated URL in a browser to render the HTML and trigger injection into the data attribute.

No command required; use browser:

Visit: https://gitlab.com/api/v4/projects/18315917/packages/pypi/simple/package_test_1

> Inspect the page source to see <a ... data-requires-python=""><script>alert(1)</script>">. If CSP blocks, alert may not fire; proceed to bypass.

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
- [[trigger]]

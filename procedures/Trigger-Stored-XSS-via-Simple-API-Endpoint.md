---
id: proc-trigger-xss-simple-endpoint
tags:
  - xss
  - trigger
  - execution
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
updated_at: '2025-12-14T17:32:20.496Z'
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
# Trigger-Stored-XSS-via-Simple-API-Endpoint

## Summary

This procedure triggers the stored XSS by accessing the PyPi simple API endpoint, where the malicious requires_python is rendered unsanitized in HTML, executing injected JavaScript on the visitor's browser.

## Description

The simple endpoint (/api/v4/projects/:id/packages/pypi/simple/:package_name) generates an HTML index of packages, inserting requires_python into <a data-requires-python="..."> links without escaping. The payload breaks out via '"; executes <script>alert(1)</script>. On GitLab.com, CSP blocks inline scripts, but execution occurs for non-CSP or bypassed scenarios. Victims include any user visiting the URL, risking session hijacking.

## Requirements

1. Uploaded package with payload from prior procedure
2. Browser access to the GitLab instance
3. Project ID and package name known

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP (script-src 'self') to block inline JS
- Log and alert on anomalous endpoint accesses
- Sanitize all user inputs in HTML generation

## Objectives

1. Render the stored payload in browser context
2. Execute arbitrary JavaScript
3. Demonstrate impact like alert or data exfil

## Instructions

### Step 1: Construct Endpoint URL

**Context**: Build the URL using project ID and package name.

For basic XSS: https://gitlab.com/api/v4/projects/18315917/packages/pypi/simple/package_test_1

For CSP bypass: https://gitlab.com/api/v4/projects/18315917/packages/pypi/simple/package_csp_bypass

### Step 2: Visit and Observe Execution

**Context**: Load the URL in a browser to trigger rendering.

Open the URL; inspect the HTML source to see data-requires-python="2.7 '"><script>alert(1)</script>'" – the breakout executes the script.

> Expected: Alert(1) pops up. For bypass, inspect network tab for load of /vakzz-h1/public/-/raw/a/test.js (allowed domain).

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
- [[Execution]]

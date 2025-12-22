---
id: e5f6g7h8-i9j0-1234-efgh-567890123456
tags:
  - verification
  - js-execution
  - xss
  - browser-console
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Browser
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:21.089Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify-JavaScript-Execution-from-PDF-XSS

## Summary

This procedure confirms successful XSS exploitation by observing JavaScript execution in the browser console after opening a malicious PDF in Nextcloud's viewer.

## Description

Upon rendering the POC PDF, vulnerable PDF.js executes embedded JS, logging messages and attempting actions like external fetches (blocked by CORS). Verification in the console proves control in the victim's browser context, enabling risks like session cookie theft or DOM manipulation. Tested in Safari 13.0.5 and Firefox 74.0, with no execution in Chrome due to stricter rendering.

## Requirements

1. Browser with developer console (Safari or Firefox).
2. Successful upload and opening of the malicious PDF.
3. Understanding of CORS and browser differences.

## Defense

Defensive measures and detection strategies:

- Enable strict CSP headers to block inline JS execution.
- Monitor browser consoles or logs for unexpected script runs in PDF contexts.
- Use endpoint detection to flag anomalous JS in file viewers.

## Objectives

1. Observe direct evidence of JS execution.
2. Assess limitations like CORS blocks on external interactions.
3. Evaluate browser-specific reliability for broader impact.

## Instructions

### Step 1: Open Browser Developer Console

**Context**: Prepare to monitor script activity during PDF rendering.

In Safari or Firefox, press F12 or Cmd+Option+I to open dev tools, then switch to the Console tab.

> Clears any prior logs for clean observation.

### Step 2: Render the Malicious PDF

**Context**: Trigger the exploit and watch for output.

With console open, navigate back to Nextcloud, open the uploaded POC PDF in the viewer.

> Expected output: Console logs 'Hello, this is code running in' followed by the file path, e.g., '/path/to/poc.pdf'.

### Step 3: Analyze Execution and Limitations

**Context**: Review logs and test for further actions.

Note any additional attempts, like fetch requests to external URLs, which fail due to CORS. In Chrome, confirm no logs appear.

> Success: JS execution verified; potential for cookie access via document.cookie in custom payloads.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Collection]]
- [[verification]]


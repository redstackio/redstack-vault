---
id: proc-observe-js-execution
tags:
  - xss-execution
  - alert-popup
  - verification
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:12.991Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe JavaScript Execution

## Summary

This procedure verifies the success of the XSS injection by observing the execution of the injected JavaScript in the browser, such as an alert popup, confirming arbitrary code execution.

## Description

Upon reflection, the unsanitized input renders the SVG tag, triggering onload in the victim's browser. This allows theft of cookies via document.cookie or phishing. Impact is high for authenticated users.

## Requirements

1. Submitted payload from previous step
2. Browser to render the response
3. DevTools for DOM inspection

## Defense

Defensive measures and detection strategies:

- Escape all user inputs before output (e.g., htmlspecialchars)
- Monitor for unexpected JS events in client-side logs
- Use HttpOnly flags on cookies to prevent theft

## Objectives

1. Confirm payload execution
2. Assess impact (e.g., alert, cookie access)
3. Document for reporting

## Instructions

### Step 1: Render the Response

**Context**: Load the server's reflected response in a browser.

If using the HTML file, submit and observe the page load; alternatively, copy the curl response into an HTML viewer.

**Expected Output**: Browser parses the reflected HTML.

### Step 2: Monitor for Execution

**Context**: Check for JS triggers like onload.

Look for alert(1) popup or inspect elements for the SVG tag in the DOM.

**Expected Output**: Alert dialog or console errors indicating execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-execution]]
- [[verification]]

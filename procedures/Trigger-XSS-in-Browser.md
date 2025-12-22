---
id: proc-uuid-5
tags:
  - xss-trigger
  - browser-execution
  - payload-activation
type: procedure
tools:
  - '[[tools/Chromium]]'
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
updated_at: '2025-12-14T03:16:02.875Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-in-Browser

## Summary

This procedure accesses the served directory in a browser, causing the unsanitized filename to inject and execute the XSS payload, loading the malicious iframe and script.

## Description

Browsers render the directory index, parsing the injected HTML from the filename, which embeds an iframe sourcing malware_frame.html. The script then loads external JS, compromising the viewer. Impact: Arbitrary code execution, potential data theft or malware install. Target: Localhost:8000. Expected: Visible execution like alerts or network requests.

## Requirements

1. Running public server on port 8000
2. Browser like Chromium installed
3. Local network access to 127.0.0.1
4. Malicious files served

## Defense

Defensive measures and detection strategies:

- Browser extensions like NoScript to block JS
- Server-side escaping of output (e.g., via libraries like escape-html)
- User training on avoiding untrusted directory listings; monitor for unexpected iframes via dev tools

## Objectives

1. Execute injected XSS in victim context
2. Load and run external malicious script
3. Demonstrate full compromise chain

## Instructions

### Step 1: Access the Directory

**Context**: Navigate to the server URL to trigger rendering of the vulnerable listing.

**Command** (browser open):
```bash
chromium http://127.0.0.1:8000
```

> Opens Chromium to the URL; inspect element to see injected <iframe> in the <li> tag. Success if poc.js loads (check network tab for request to bl4de.tech).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Chromium]]

## Tags

- xss-trigger
- browser-execution

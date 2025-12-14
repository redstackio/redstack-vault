---
tags:
  - xss
  - browser
  - execution
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
updated_at: '2025-12-14T03:15:46.828Z'
skill_level: beginner
impact_level: high
detection_risk: high
sub_techniques: []
id: 1ee16342-c134-4114-8429-3f619b901067
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-by-Accessing-Served-Page-in-Browser

## Summary

This procedure accesses the served HTML page in a browser, causing the unescaped JavaScript payload from the XLSX to execute, demonstrating the stored XSS impact.

## Description

Loading the page in Chromium executes the script in the browser's context, popping an alert and potentially allowing further attacks like cookie theft. This exploits the lack of escaping in the Node.js app. Prerequisites: Server running on 8080. Expected outcome: Visible XSS effects confirming vulnerability.

## Requirements

1. Local server active on port 8080
2. Web browser like Chromium (version 67.0 or later)
3. Network access to localhost

## Defense

Defensive measures and detection strategies:

- Implement strict CSP headers to prevent inline script execution
- Browser-side: Use extensions like NoScript; server-side: Log and alert on script execution attempts
- Educate users on risks of viewing untrusted spreadsheet content in web apps

## Objectives

1. Load the vulnerable HTML in a browser
2. Observe JavaScript execution from stored payload
3. Validate impact like alerts or DOM manipulation

## Instructions

### Step 1: Access the Endpoint

**Context**: Navigate to the served page to trigger parsing and rendering.

**Instructions**: Open Chromium and visit http://localhost:8080. Inspect the page source to confirm the script tag in the table.

> Expected output: Alert('xss!') pops up; source shows embedded <script> in cell.

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

- xss
- browser
- execution

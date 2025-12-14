---
id: proc-uuid-4
tags:
  - xss
  - execution
type: procedure
tools:
  - '[[tools/Firefox-Browser]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:02.816Z'
skill_level: intermediate
impact_level: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-Directory-Access

## Summary

This procedure accesses the html-pages directory listing to execute the stored JavaScript payload, resulting in arbitrary code execution in the victim's browser.

## Description

Navigating to the root URL displays the listing with the malicious directory name inserted unsanitized into HTML elements like <title> and <span>, breaking out and executing the <svg onload=alert(5);> payload. This can lead to session theft or phishing in shared setups.

## Requirements

1. Server running on port 6060
2. Malicious directory present
3. Vulnerable browser (e.g., Firefox 59.0.2)

## Defense

Defensive measures and detection strategies:

- Enable browser XSS filters (XSS Auditor)
- Content Security Policy (CSP) to block inline scripts
- Audit server logs for anomalous access patterns

## Objectives

1. Trigger client-side JavaScript execution
2. Demonstrate impact like alerts or data exfil
3. Validate vulnerability exploitation

## Instructions

### Step 1: Access the Directory Listing

**Context**: Use a browser to visit the server root and interact with the listing.

**Instructions**: In [[tools/Firefox-Browser]], go to http://127.0.0.1:6060/ and click the malicious directory, or directly access http://127.0.0.1:6060/%22%3E%3Csvg%20onload=alert(5);%3E/.

> The payload executes immediately, showing an alert(5) popup.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox-Browser]]

## Tags

- xss
- execution

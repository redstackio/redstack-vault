---
id: proc-003
tags:
  - xss
  - execution
  - client-side-attack
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:25.469Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-via-Sharing-Page-Visit

## Summary

This procedure triggers the stored XSS payload by visiting the sharing URL, resulting in JavaScript execution in the browser.

## Description

The sharing page in wis.pr inserts the unsanitized group name into the twitter:description meta tag, allowing the script payload to execute as the page loads. This can lead to session hijacking, data theft, or phishing for any unauthenticated visitor. The procedure validates execution and assesses impact.

## Requirements

1. Valid sharing URL from malicious group
2. Target browser without strict security extensions
3. Network access to wis.pr

## Defense

Defensive measures and detection strategies:

- Apply strict CSP headers to prevent script execution
- Encode meta tag content to escape HTML entities
- Use browser security features like XSS Auditor
- Detect and block anomalous script alerts in monitoring tools

## Objectives

1. Execute arbitrary JavaScript in victim context
2. Demonstrate impact like alert or cookie theft
3. Validate vulnerability for reporting

## Instructions

### Step 1: Visit Sharing URL

**Context**: Load the page to trigger reflection and execution.

Paste the sharing URL into a web browser and navigate to it.

### Step 2: Observe Execution

**Context**: Confirm the payload runs.

Inspect the page source for the meta tag containing the payload. The script should execute immediately, showing an alert('test').

> Payload appears as: <meta name="twitter:description" content="Test>"<script>alert('test');</script>">, breaking out and running the script.

**Expected Output**: Alert dialog; potential console errors if blocked.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[client-side-attack]]

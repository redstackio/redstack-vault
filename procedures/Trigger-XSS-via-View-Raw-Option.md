---
id: proc-slack-boxnote-trigger-001
tags:
  - execution
  - xss-trigger
  - javascript
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
updated_at: '2025-12-14T03:16:37.481Z'
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
# Trigger-XSS-via-View-Raw-Option

## Summary

This procedure exploits the 'view raw' feature of a shared BoxNote to execute the stored XSS payload in the victim's browser, achieving arbitrary JavaScript execution.

## Description

The 'view raw' option on files.slack.com renders the BoxNote content without proper escaping, allowing the injected script to run in the context of the authenticated user's session. This can lead to alerts, data theft, or further attacks like keylogging. It targets any team member accessing the link, amplifying impact.

## Requirements

1. Shareable link to the malicious BoxNote
2. Victim with Slack authentication
3. Browser without strict XSS protections (e.g., no blocking extensions)

## Defense

Defensive measures and detection strategies:

- Enforce Content Security Policy (CSP) to block inline scripts and event handlers
- Sanitize raw views with HTML entity encoding
- Detect and block access to raw views for suspicious files via WAF rules

## Objectives

1. Execute the payload in a victim's browser
2. Confirm code execution (e.g., via alert)
3. Exploit for session theft or exfiltration

## Instructions

### Step 1: Access the Shared Link

**Context**: Have the victim open the provided BoxNote URL in their browser.

Navigate to the link, e.g., `https://files.slack.com/files-pri/T027N7MK3-F1NCA92JF/...boxnote.boxnote`, ensuring Slack authentication.

### Step 2: Select View Raw

**Context**: Choose the 'view raw' option to load unsanitized content.

In the BoxNote preview, click the 'view raw' button or link, which fetches and renders the raw HTML.

### Step 3: Observe Execution

**Context**: Verify the payload runs, such as displaying an alert with the domain.

The onerror handler triggers `alert(document.domain)`, confirming execution. Extend for real attacks like stealing cookies.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[Execution]]
- [[xss]]

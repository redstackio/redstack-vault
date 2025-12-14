---
tags:
  - xss-trigger
  - execution
  - session-hijacking
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:26.142Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: f5fd8a02-75db-4a14-bde3-4617356bfd90
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Editing-Saved-Filter

## Summary

This procedure demonstrates execution of the stored XSS payload in Concrete CMS 8.5.2 by loading the saved filter, triggering JavaScript in the victim's browser context.

## Description

After injection, simulate a victim user (or use a secondary browser session) to interact with the saved filter. Clicking 'Edit' on the filter search bar causes the application to render the unsanitized phrase field, executing the onerror handler or similar JavaScript. This can lead to alert popups for proof-of-concept or more severe actions like stealing session cookies via data exfiltration to an attacker-controlled server. The vulnerability affects privileged users editing the filter, amplifying impact.

## Requirements

1. Saved filter with injected payload from previous procedure
2. Access to the file search interface as a non-admin or secondary user
3. Web browser to observe execution
4. Optional: Attacker server for payload exfiltration testing

## Defense

Defensive measures and detection strategies:

- Output escape all rendered user inputs in edit interfaces
- Deploy browser-based XSS auditors or extensions
- Monitor for unexpected JavaScript alerts or network requests from the app
- Regularly scan saved filters for XSS patterns

## Objectives

1. Load the saved filter to render the malicious payload
2. Execute JavaScript in the browser context
3. Demonstrate potential for session theft or data exfiltration

## Instructions

### Step 1: Access File Search as Victim

**Context**: Simulate a user who can view/edit saved filters.

Log in as a different user or use an incognito session, then navigate to Dashboard > Files > Search.

> The search interface loads, showing saved filters if applicable.

### Step 2: Edit the Saved Filter

**Context**: Trigger rendering of the stored payload.

Locate the saved filter in the search bar and click 'Edit'.

> The edit window opens, rendering the phrase field and executing the payload (e.g., alert(1) via onerror).

### Step 3: Verify Execution

**Context**: Confirm XSS success and assess impact.

Observe the JavaScript execution; modify payload to document.cookie and send to attacker endpoint for real exploitation.

> Browser console or network tab shows execution; alert or request confirms trigger.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[Execution]]
- [[session-hijacking]]

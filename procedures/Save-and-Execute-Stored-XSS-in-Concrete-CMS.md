---
id: proc-save-execute-stored-xss-concrete-cms
tags:
  - xss
  - stored-xss
  - execution
  - concrete-cms
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
updated_at: '2025-12-14T03:15:35.537Z'
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
# Save-and-Execute-Stored-XSS-in-Concrete-CMS

## Summary

This procedure covers saving the injected XSS payload in Concrete CMS and triggering its execution upon page rendering, resulting in arbitrary JavaScript in viewers' browsers.

## Description

After injection, the payload is stored in the CMS database without encoding. When the page is viewed, the unsanitized output renders the script, executing it in the browser context. This leads to persistent attacks affecting all users, such as stealing cookies or defacing content. This procedure builds on prior injection steps and validates exploitation through observable effects like alert popups.

## Requirements

1. Injected payload from previous procedure still in the input field
2. Permissions to save content changes
3. Ability to view the affected page in a browser

## Defense

Defensive measures and detection strategies:

- Enforce output escaping for all dynamic content rendering
- Monitor for anomalous JavaScript execution via browser consoles or CSP violation reports
- Regularly audit stored content for malicious patterns

## Objectives

1. Persist the XSS payload in the CMS storage
2. Trigger execution on page load for any viewer
3. Confirm impact through client-side effects like alerts or data exfiltration

## Instructions

### Step 1: Submit and Save Content

**Context**: Persist the payload by saving the edited Feature Paragraph.

Click the save or submit button on the editing form to store the content.

> The CMS confirms the save, updating the page with the injected payload in the backend.

### Step 2: View the Affected Page

**Context**: Render the page to execute the stored script.

Navigate to or refresh the page containing the Feature Paragraph. The payload executes automatically.

> An alert box with '1' appears, verifying JavaScript execution in the browser.

### Step 3: Validate Execution

**Context**: Confirm the vulnerability's impact beyond the POC.

Replace the alert with more malicious code, such as `document.cookie` access, and re-test to simulate real attacks like session theft.

> Browser console or network tab shows potential data exfiltration attempts.

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
- [[stored-xss]]
- [[Execution]]
- [[concrete-cms]]

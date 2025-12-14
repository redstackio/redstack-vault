---
id: proc-inject-xss-payload-comment
tags:
  - xss
  - injection
  - javascript
  - nextcloud
type: procedure
tools:
  - '[[tools/Firefox]]'
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
updated_at: '2025-12-14T03:15:26.509Z'
skill_level: beginner
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-XSS-Payload-in-Comment

## Summary

This procedure details submitting a malicious HTML payload into the Nextcloud comment form to exploit insufficient sanitization, breaking out of the textarea to inject and render executable JavaScript code.

## Description

The vulnerability arises from an outdated Nextcloud version that echoes user input into HTML without escaping, allowing attackers to close the enclosing textarea tag and insert custom elements like an img with an onmouseover event. This leads to reflected XSS, where the payload executes when the page renders the comment. The attack targets public demo sites and can chain to steal cookies or redirect users.

## Requirements

1. Access to the comment form from the prior procedure
2. Web browser for form submission
3. Knowledge of basic HTML/JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Sanitize all user inputs with HTML entity encoding (e.g., convert < to &lt;)
- Use libraries like DOMPurify for client-side cleaning
- Log and alert on submissions containing script tags or event handlers

## Objectives

1. Inject HTML to escape the input context
2. Render the payload as executable code on the page
3. Enable JavaScript execution for further exploitation

## Instructions

### Step 1: Craft and Enter Payload

**Context**: Prepare a payload that closes the textarea and injects a harmless but demonstrative script trigger.

In the comment textarea, input:

```
</textarea><img src=x onmouseover=alert(document.domain)>
```

> This payload ends the textarea, adds an img tag with a broken src (to avoid loading), and attaches an alert on mouseover to confirm execution.

### Step 2: Submit the Form

**Context**: Send the payload to the server for rendering in the comments section.

Click the submit button on the form.

> Expected: The page refreshes or updates to show the new comment with the img element rendered inline, not escaped.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Firefox]]

## Tags

- [[xss]]
- [[injection]]
- [[JavaScript]]
- [[nextcloud]]

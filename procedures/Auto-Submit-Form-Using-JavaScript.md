---
id: proc-uuid-2
tags:
  - javascript
  - auto-submit
  - form-injection
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
updated_at: '2025-12-13T23:52:43.767Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Auto-Submit-Form-Using-JavaScript

## Summary

This procedure adds JavaScript to an HTML page to automatically submit a form upon loading, enabling drive-by exploitation of the Slack XSS vulnerability without requiring victim interaction.

## Description

Building on the malicious HTML form, this procedure injects a script that calls submit() on the named form element when the page loads. This automates the POST request to Slack's endpoint, reflecting the malicious 'path' parameter. The attack scenario involves delivering this page via phishing, where the victim's browser executes the script in the context of their Slack session, potentially leading to JS execution or insecure redirects. Expected outcomes include immediate form submission and payload delivery; prerequisites are the HTML from the prior procedure and basic JS knowledge.

## Requirements

1. Existing HTML file with named form
2. Browser developer tools for testing submission
3. Victim must be authenticated in Slack

## Defense

Defensive measures and detection strategies:

- Browser extensions blocking auto-submits (e.g., NoScript)
- Server-side rate limiting on feedback submissions
- Logging and alerting on rapid or scripted form posts

## Objectives

1. Automate form submission on page load
2. Ensure payload reaches the vulnerable endpoint
3. Minimize user interaction for higher success rate

## Instructions

### Step 1: Insert Script Tag

**Context**: Add a script element before the closing body tag to target and submit the form.

Append to the HTML:

```html
<script>document.pisarenko.submit();</script>
```

> This uses document.getElementById or name selector implicitly via document.pisarenko to submit the form named 'pisarenko'.

### Step 2: Test Auto-Submission

**Context**: Load the updated HTML in a browser to verify automatic POST.

Open 'xss.html' in a browser with dev tools open (Network tab).

> Observe the form submit immediately, sending the request to Slack. If authenticated, check for reflection in the response.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[JavaScript]]
- [[auto-submit]]
- [[form-injection]]

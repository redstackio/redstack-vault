---
tags:
  - xss
  - payload-injection
  - html
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: beginner
impact_level: high
detection_risk: low
sub_techniques: []
id: 6a75e819-474c-4da1-b2d7-a0bab5b060d2
created_at: '2025-12-14T03:15:35.931Z'
updated_at: '2025-12-14T03:15:35.931Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Create-Local-HTML-File-with-XSS-Payload-for-Gravatar

## Summary

This procedure creates a local HTML file embedding a malicious XSS payload targeting Gravatar's insufficient sanitization, using an onmouseover event to inject JavaScript like 'prompt(916137)' into HTML attributes for testing vulnerability exploitation.

## Description

In the context of the Gravatar XSS vulnerability, attackers craft a local HTML file that simulates pages from various Gravatar directories and parameters. The payload, sourced from http://pastebin.com/fsAKWTe1, injects script into elements, allowing arbitrary JS execution when triggered. This step prepares the environment for client-side testing without requiring server access, highlighting how unsanitized inputs lead to attribute-based XSS. Expected outcome is a functional PoC file demonstrating injection across 171 potential instances.

## Requirements

1. Text editor (e.g., Notepad, VS Code) for HTML creation
2. Access to internet for copying payload from Pastebin
3. Local file system write permissions

## Defense

Defensive measures and detection strategies:

- Implement strict Content Security Policy (CSP) to block inline scripts
- Sanitize all user inputs and encode HTML attributes on output
- Use tools like OWASP ZAP or browser dev tools to scan for injected payloads during development

## Objectives

1. Prepare injectable payload mimicking Gravatar's vulnerable structure
2. Enable local simulation of remote exploitation
3. Validate payload syntax for reliable execution

## Instructions

### Step 1: Retrieve and Adapt Payload

**Context**: Obtain the base payload and integrate it into an HTML structure simulating Gravatar elements.

Copy the code from http://pastebin.com/fsAKWTe1, which includes injections like 'onmouseover='prompt(916137)'bad="' into tags such as <a> for JSON/XML links.

Create a file named 'gravatar_poc.html' with content like:

```html
<!DOCTYPE html>
<html>
<head><title>Gravatar PoC</title></head>
<body>
<a href="#" onmouseover="prompt(916137)" bad="'">JSON</a>
<a href="#" onmouseover="prompt(916137)" bad="'">XML</a>
<!-- Simulate various directories/parameters -->
</body>
</html>
```

> This embeds the payload in attributes, ready for rendering. Save the file locally.

### Step 2: Verify File Integrity

**Context**: Ensure the HTML is valid and payload is intact for subsequent loading.

Open the file in a text editor and inspect for proper injection points.

> Expected: No syntax errors; attributes show injected script.

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
- [[payload-creation]]

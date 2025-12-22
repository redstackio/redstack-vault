---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
tags:
  - xss
  - dom-xss
  - javascript
  - web-vulnerability
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:46.780Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
---
id: b2c3d4e5-f6g7-8901-bcde-f23456789012
name: Inject-DOM-XSS-Payload-into-Username-Field
type: procedure
verified: false
submitted: false
created_at: 2023-10-01T12:00:00Z
updated_at: 2023-10-01T12:00:00Z
tactics: [[Initial Access]], [[Execution]], [[Collection]]
techniques: [[Exploit Public-Facing Application]], [[JavaScript]]
sub_techniques: []
tags: xss, dom-xss, javascript, web-vulnerability
commands: []
platforms: Web
tools: []
---

# Inject-DOM-XSS-Payload-into-Username-Field

## Summary

This procedure exploits a DOM-based Cross-Site Scripting (XSS) vulnerability in the username field of a web application's troubleshoot page by injecting a payload that manipulates the DOM to execute arbitrary JavaScript, such as displaying a confirmation dialog, and can be extended to steal cookies or hijack sessions.

## Description

In this attack scenario, the target is a U.S. Department of Defense web application at `https://████/█████████/home/troubleshoot.html?lang=en`. The vulnerability arises from improper client-side validation and sanitization of user input in the username field, allowing attackers to inject HTML attributes like `autofocus` and `onfocus`. Upon page load or focus, this executes JavaScript via the `Function()` constructor. The expected outcome is arbitrary code execution in the victim's browser context, leading to session compromise. Prerequisites include browser access to the public URL; no authentication is needed.

## Requirements

1. Web browser with developer tools enabled for DOM inspection.
2. Direct internet access to the target URL.
3. Basic knowledge of HTML and JavaScript for payload crafting.

## Defense

Defensive measures and detection strategies:

- Implement server-side input validation and output encoding to prevent DOM manipulation.
- Use Content Security Policy (CSP) headers to restrict inline script execution and autofocus behaviors.
- Monitor browser console for unexpected JavaScript errors or dialog pops in web logs.

## Objectives

1. Inject and execute arbitrary JavaScript in the browser to confirm vulnerability.
2. Demonstrate potential for cookie theft or session hijacking.
3. Highlight risks of client-side sanitization failures in web apps.

## Instructions

### Step 1: Access the Target Page

**Context**: Load the vulnerable troubleshoot page to expose the username input field.

Navigate to `https://████/█████████/home/troubleshoot.html?lang=en` in your browser.

> The page should load, showing the input form. Use dev tools (F12) to inspect the username field for any existing sanitization.

### Step 2: Craft and Inject the Payload

**Context**: Enter a payload that breaks out of the input context and injects executable HTML/JS attributes.

In the username field, input: `1--><button/autofocus/onfocus=Function("confirm`1`")();//`

> This payload uses `-->` to comment out closing tags, injects a `<button>` with `autofocus` to trigger on load, and `onfocus` to run `Function("confirm`1`")()`, which alerts a dialog. Submit or interact to trigger.

### Step 3: Verify Execution

**Context**: Confirm the payload alters the DOM and executes code.

Interact with the page (e.g., tab to the field or submit). Check for the confirmation dialog.

> Successful execution shows a browser dialog with "1". Inspect DOM to see the injected button; extend payload for real attacks like `document.cookie` exfiltration.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dom-xss]]
- [[JavaScript]]
- [[web-vulnerability]]

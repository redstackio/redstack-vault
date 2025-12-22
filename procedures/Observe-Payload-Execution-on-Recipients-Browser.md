---
tags:
  - xss
  - execution
  - angular
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 3ae15507-fa2b-4c79-a388-4983a3aca832
created_at: '2025-12-13T23:55:20.663Z'
updated_at: '2025-12-13T23:55:20.663Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe Payload Execution on Recipient's Browser

## Summary

This procedure verifies the execution of the injected Angular expression as JavaScript in the recipient's browser when viewing the private message, confirming the stored XSS impact.

## Description

Upon the recipient accessing the conversation, the unsanitized Subject field triggers Angular to evaluate the expression, executing embedded JavaScript. This can lead to alerts, DOM manipulation, or more severe actions like cookie theft. The procedure assumes prior injection success and uses browser monitoring to capture execution. It highlights the client-side nature of the vulnerability in FetLife's Angular implementation, with outcomes including proof-of-concept exploitation.

## Requirements

1. Recipient account with access to the injected message
2. Browser developer tools for monitoring execution
3. Prior successful payload injection

## Defense

Defensive measures and detection strategies:

- Render dynamic content with Angular's bypassSecurityTrustHtml only after strict validation
- Implement runtime monitoring for unexpected script execution via browser extensions or WAF
- Educate users on phishing-like attacks in messaging features and enable two-factor authentication

## Objectives

1. Trigger and observe JavaScript execution from the stored payload
2. Assess potential impacts like session compromise
3. Validate the full chain for reporting or mitigation

## Instructions

### Step 1: Access the Message as Recipient

**Context**: Simulate victim behavior to trigger rendering of the vulnerable subject.

Log in as the recipient, navigate to the inbox, and open the private conversation containing the injected message.

### Step 2: Monitor for Execution

**Context**: Use tools to capture the payload's JavaScript runtime behavior.

Open the browser console (F12) before viewing the message. Upon loading, watch for the alert or console output from the payload (e.g., "XSS" alert dialog).

> Execution confirms the XSS, as the expression is parsed and run in the browser context.

### Step 3: Analyze Impact

**Context**: Evaluate the exploit's reach, such as access to session data.

In the console, test further by modifying the payload to log `document.cookie` or make requests, observing if sensitive data is accessible.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]
- [[angular]]

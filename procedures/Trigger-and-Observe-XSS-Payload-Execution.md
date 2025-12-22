---
tags:
  - xss
  - javascript
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
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:08.016Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 55e75c6e-45ae-4686-a336-14e5ebf6617d
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-and-Observe-XSS-Payload-Execution

## Summary

This procedure involves loading the reflected response in a vulnerable browser and interacting with the affected element to execute the injected JavaScript, verifying the XSS success.

## Description

Once the server reflects the malicious Referer into the onclick of a cancel button, visiting the page in a browser like IE (which doesn't encode Referer) will embed the payload. Clicking the button triggers execution, potentially stealing sessions or data. This step confirms impact and can be used to exfiltrate information via the alert or network requests.

## Requirements

1. Reflected response from previous step
2. Vulnerable browser (e.g., Internet Explorer)
3. Victim-like interaction simulation

## Defense

Defensive measures and detection strategies:

- Encode all dynamic content in HTML attributes (e.g., using htmlspecialchars in PHP)
- Browser-side: Enable modern Referer policies (strict-origin-when-cross-origin)
- Monitor client-side errors or unexpected JS execution in browser dev tools

## Objectives

1. Execute the payload in the victim's context
2. Observe effects like alerts or data theft
3. Assess potential for further exploitation (e.g., cookie access)

## Instructions

### Step 1: Load the Page

**Context**: Simulate victim access by opening the endpoint URL in the target browser, ensuring the Referer is sent unencoded.

Navigate to https://apps.owncloud.com/messages/?action=newmessage&username=anderslund from a malicious referring page or directly if testing.

> The page should load with the cancel button containing the reflected onclick.

### Step 2: Interact and Observe

**Context**: Click the cancel button to fire the onclick event.

Interact with the button; watch for JavaScript execution.

> Expected: Alert dialog with payload (e.g., alert(1) or document.domain), confirming XSS. In a real attack, replace with stealthy exfiltration like sending cookies to attacker server.

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
- execution

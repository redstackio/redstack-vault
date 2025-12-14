---
tags:
  - xss-execution
  - cookie-theft
type: procedure
tools: []
tactics:
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
id: 9f04df8a-7abc-4b9c-8e9c-f995a5148f3a
created_at: '2025-12-14T03:47:18.448Z'
updated_at: '2025-12-14T03:47:18.448Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-on-Account-List-Page

## Summary

This procedure triggers the execution of the stored XSS payload by viewing the account list page on OWOX Finance, leading to JavaScript execution and potential cookie theft in the attacker's or victim's browser.

## Description

After payload injection, the account list at https://finance.owox.com/customer/accountList renders usernames without escaping, executing the script when loaded. The payload alerts document cookies, but in a real attack, it could exfiltrate data via AJAX to an external server. This affects any authenticated user viewing the list, enabling session hijacking. Prerequisites include the prior injection step; outcomes include arbitrary code execution client-side.

## Requirements

1. Payload successfully injected from previous procedure
2. Authenticated session (attacker's or victim's)
3. Web browser to load the vulnerable page

## Defense

Defensive measures and detection strategies:

- Output encode all user-controlled data on render (e.g., HTML entity encoding)
- Deploy client-side protections like strict CSP headers blocking inline scripts
- Monitor browser consoles and network traffic for unexpected alerts or exfiltration requests

## Objectives

1. Execute the stored JavaScript payload in the browser context
2. Steal sensitive data like session cookies for hijacking
3. Demonstrate impact on shared application views

## Instructions

### Step 1: Navigate to Account List

**Context**: Load the page that renders the injected username, triggering the payload.

Go to https://finance.owox.com/customer/accountList.

> The page displays the list of accounts, including the malicious username, which executes the script on render.

### Step 2: Observe Execution

**Context**: Verify the XSS by checking for payload effects like alerts or data exfiltration.

Upon loading, an alert should pop up displaying document.cookie contents. In an advanced payload, inspect network tab for requests to attacker servers.

> Success is indicated by the alert or logged exfiltration; cookies may include session tokens for further abuse.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss-trigger]]
- [[data-exfiltration]]

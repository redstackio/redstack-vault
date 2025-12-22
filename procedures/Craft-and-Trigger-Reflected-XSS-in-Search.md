---
tags:
  - xss
  - injection
  - javascript
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
updated_at: '2025-12-14T03:15:31.421Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: b33426a6-53df-429a-bea7-10fde2af6ef8
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Craft-and-Trigger-Reflected-XSS-in-Search

## Summary

This procedure crafts a malicious search URL exploiting the unquoted reflection of the search_query parameter in Moneybird's backend search, injects a JavaScript event handler, and triggers it via user interaction to execute arbitrary code, potentially leading to account takeover.

## Description

The vulnerability arises because the search_query value is output in HTML without quotes, allowing closure of attributes and injection of handlers like onclick. Using the account [id], construct a URL with payload 'test" onclick=alert(document.domain)', URL-encode it, load in a browser to reflect, and click the result to fire the script. Targets authenticated or public search views; outcomes include JS execution for phishing or manipulation.

## Requirements

1. Extracted account [id] from prior steps
2. Web browser for URL loading and interaction
3. Knowledge of URL encoding for payload

## Defense

Defensive measures and detection strategies:

- Properly quote all reflected parameters in HTML output
- Implement Content Security Policy (CSP) to block inline scripts
- Sanitize and escape user inputs; monitor for event handler injections
- WAF rules to detect common XSS payloads

## Objectives

1. Inject and reflect malicious JavaScript
2. Execute payload in browser context
3. Escalate to credential theft or account control

## Instructions

### Step 1: Construct Malicious URL

**Context**: Build the search URL with injected payload.

No command; replace [id] in https://moneybird.com/[id]/search?search_query=test%22%20onclick%3Dalert%28document.domain%29 (encoded: test" onclick=alert(document.domain)).

> Payload closes the unquoted attribute and adds onclick; verify encoding with browser dev tools.

### Step 2: Load URL in Browser

**Context**: Perform the search to reflect the payload.

No command; paste URL into browser address bar and press Enter.

> Search results load; inspect HTML source to confirm reflection without quotes (e.g., <div>search_query=test" onclick=...).

### Step 3: Interact to Trigger Payload

**Context**: Execute the JS by clicking the vulnerable element.

No command; click on the search result link containing the injected handler.

> Alert dialog appears with 'moneybird.com', confirming XSS success; extend payload for real attacks (e.g., formjacking).

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]
- [[JavaScript]]

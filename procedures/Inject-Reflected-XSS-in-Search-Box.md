---
id: proc-xss-search-pressable
tags:
  - xss
  - reflected-xss
  - javascript-execution
  - cookie-theft
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
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:55.024Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
---

# Inject-Reflected-XSS-in-Search-Box

## Summary

This procedure demonstrates injecting a reflected XSS payload into the search box of pressable.com's knowledgebase to execute arbitrary JavaScript, such as alerting document cookies to steal session data.

## Description

The search functionality at https://pressable.com/knowledgebase/ reflects user input from the ?s= parameter without proper sanitization, allowing JavaScript in attributes like onerror to execute when the page loads. This targets public-facing web applications and can lead to session hijacking in a real attack scenario where victims visit manipulated search URLs.

## Requirements

1. Web browser with JavaScript enabled
2. Access to public internet
3. No authentication required

## Defense

Defensive measures and detection strategies:

- Implement output encoding for HTML contexts using libraries like OWASP ESAPI
- Use Content Security Policy (CSP) to restrict script execution
- Monitor for anomalous JavaScript alerts or cookie access in logs

## Objectives

1. Execute arbitrary JavaScript on the victim's browser
2. Steal session cookies for potential account takeover
3. Demonstrate insufficient input validation

## Instructions

### Step 1: Craft and Inject Payload

**Context**: Prepare a payload that breaks out of the input context and injects executable JavaScript.

Enter the following payload into the search box:

"><img src=x onerror=javascript:alert(document.cookie)>

Append to URL: https://pressable.com/knowledgebase/?s="><img src=x onerror=javascript:alert(document.cookie)>&post_type=knowledgebase

Submit the search form.

> This payload closes any open attributes or tags, injects an image with a faulty src, and triggers onerror to run the alert.

### Step 2: Verify Execution

**Context**: Confirm the payload reflects and executes by observing the alert.

Inspect the page source for the unsanitized reflection and check browser console for errors or executions.

> Expected: An alert dialog displays the user's cookies, proving JS execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[Exploit Public-Facing Application]]
- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[reflected-xss]]
- [[web-vulnerability]]

---
tags:
  - xss-trigger
  - execution
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
id: eb5b98be-26de-485f-a530-72137246893b
created_at: '2025-12-13T23:55:06.654Z'
updated_at: '2025-12-13T23:55:06.654Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Viewing-Notes

## Summary

This procedure triggers the stored XSS payload by rendering the customer notes in the Shopify admin, executing arbitrary JavaScript in the viewer's browser context to steal cookies or perform other attacks.

## Description

Once injected, the payload in the notes field executes when an admin views the customer profile. Triggers include page load or events like mouseover on links. For example, a javascript:alert(document.cookie) payload displays cookies, while a redirect sends them to an attacker-controlled server. This exploits the admin's authenticated session, enabling hijacking. The attack relies on another user (or self) viewing the tainted notes.

## Requirements

1. Injected payload from previous procedure
2. Access to view the affected customer profile
3. Victim admin session (self or targeted user)

## Defense

Defensive measures and detection strategies:

- Render notes in isolated iframes with sandboxing
- Implement XSS auditors or WAF rules to block execution
- Scan for anomalous JavaScript in stored data via backend validation

## Objectives

1. Execute the injected script in the browser
2. Capture sensitive data like session cookies
3. Achieve session hijacking or data exfiltration

## Instructions

### Step 1: Navigate to Tainted Profile

**Context**: Load the customer page containing the stored payload.

From the customers list or search, open the profile with the modified notes.

> The profile loads, and notes render in the UI.

### Step 2: Interact to Trigger Execution

**Context**: Cause the payload to run via rendering or event.

View the notes section; if event-based, hover or click the injected element. The script executes immediately.

> An alert pops up with cookies, or a redirect occurs to exfiltrate data.

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

- [[xss-trigger]]
- [[Execution]]

---
id: proc-trigger-xss-linkedin-click
tags:
  - xss
  - execution
  - data-theft
type: procedure
tools: []
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:47:18.067Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-via-LinkedIn-Icon-Click

## Summary

This procedure triggers the stored JavaScript payload by clicking the LinkedIn icon in the lemlist interface, executing the script in the page context to achieve unauthorized actions or data exfiltration.

## Description

Once the payload is stored, the LinkedIn icon in the rendered buddy view uses the injected URL, interpreting it as a javascript: URI upon click. This executes the script client-side, allowing access to DOM elements, cookies, or network requests. The attack targets any user viewing the campaign, with high impact on session integrity in the web environment.

## Requirements

1. Saved buddy with injected payload
2. Access to the campaign view (self or victim)
3. Browser capable of executing javascript: links

## Defense

Defensive measures and detection strategies:

- Escape URLs in hyperlinks to prevent scheme execution
- Enforce strict CSP to block inline scripts
- Monitor for unexpected network requests or DOM manipulations

## Objectives

1. Cause the icon click to load the malicious URL
2. Execute the payload for code injection
3. Achieve data theft or user impersonation

## Instructions

### Step 1: Access Campaign View

**Context**: Load the page where the buddy's LinkedIn icon is displayed.

Navigate back to the campaign dashboard or share the view.

> Icon appears next to the buddy entry.

### Step 2: Click LinkedIn Icon

**Context**: Interact with the icon to trigger the URL.

Click the LinkedIn icon; the browser processes the javascript: payload.

> Script executes immediately, e.g., alert shows or data sends to attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Execution]]

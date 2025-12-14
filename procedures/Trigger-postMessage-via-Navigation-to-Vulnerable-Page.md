---
tags:
  - xss
  - dom-xss
  - postmessage
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
updated_at: '2025-12-14T03:47:12.861Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 927eb445-5707-45e8-a5c9-aa403ccf5471
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-postMessage-via-Navigation-to-Vulnerable-Page

## Summary

This procedure triggers the postMessage event by navigating from the malicious POC page to the vulnerable notes.html, sending the crafted payload during the interaction.

## Description

The vulnerable page at http://talks.lystit.com/data-saloon-presentation/plugin/notes/notes.html listens for postMessage events without origin checks. By clicking a link on the attacker's page that navigates to this URL, the JavaScript sends the message with unsanitized JSON data, which the handler parses and injects into the DOM via innerHTML, executing any scripts.

## Requirements

1. Hosted malicious POC page accessible
2. Victim browser session
3. Target page must be reachable (no auth required)

## Defense

Defensive measures and detection strategies:

- Implement Content Security Policy (CSP) to block inline scripts
- Use structured clone or safe parsing for postMessage data
- Log and alert on cross-origin postMessage attempts

## Objectives

1. Deliver the payload to the vulnerable handler
2. Ensure navigation occurs in the same context
3. Bypass any implicit same-origin assumptions

## Instructions

### Step 1: Load the Malicious Page

**Context**: Victim visits the attacker's POC page to initiate the chain.

**Instructions**: Open https://gamer7112.com/lyst_1.html (or local equivalent) in the browser.

> The page displays a link to the presentation; no immediate execution occurs.

### Step 2: Click the Trigger Link

**Context**: Interaction sends postMessage and navigates to target.

**Instructions**: Click the "Click to view presentation" link.

> This fires the event listener, sending postMessage(JSON.stringify({notes: '<script>alert("XSS")</script>'}), '*') or targeted origin, then loads the vulnerable page.

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
- postmessage
- navigation-trigger

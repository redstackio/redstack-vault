---
tags:
  - xss
  - exfiltration
  - session-theft
  - web
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
updated_at: '2025-12-14T03:47:18.490Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e0a1adff-820d-4030-9d4c-893db145894d
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-XSS-for-Session-Theft

## Summary

This procedure triggers the stored XSS payload in the Lark Suite helpdesk by having a victim view the affected profile, leading to JavaScript execution and potential theft of session cookies for unauthorized access.

## Description

Once the payload is injected into the city field, any helpdesk user viewing the user's profile will render the unsanitized input, executing the script in their browser. This can capture cookies, keystrokes, or redirect to phishing sites. The attack relies on social engineering to lure victims or natural workflow in the helpdesk. Reported impact includes unauthorized internal access; defenses focus on sanitization and monitoring.

## Requirements

1. Injected payload from prior procedure
2. Victim access to the helpdesk profile view
3. Attacker-controlled server for exfiltration

## Defense

Defensive measures and detection strategies:

- Deploy browser-based protections like XSS auditors or extensions
- Log and alert on unexpected outbound requests from helpdesk pages
- Regular security audits of form fields using tools like OWASP ZAP

## Objectives

1. Execute the payload in victim context
2. Collect sensitive data like session tokens
3. Gain unauthorized helpdesk access

## Instructions

### Step 1: Lure Victim to Profile

**Context**: Use social engineering or wait for routine helpdesk interactions to trigger the view.

No specific command; instruct victim via email or chat: "Please review user profile at [link to helpdesk profile]." Expected: Victim loads the page, rendering the city field.

### Step 2: Monitor Exfiltration

**Context**: Watch attacker server for incoming data from the executed script.

Set up a listener (e.g., using netcat or a web server) at the exfiltration endpoint. Expected: POST or GET request with victim's cookie data upon payload execution.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- exfiltration
- session-theft

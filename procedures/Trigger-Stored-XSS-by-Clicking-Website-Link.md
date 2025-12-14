---
id: proc-uuid-5
tags:
  - xss
  - execution
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
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:15:52.956Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-Stored-XSS-by-Clicking-Website-Link

## Summary

This procedure triggers the stored XSS by viewing the account details and clicking the malicious website link, executing JavaScript to steal cookies.

## Description

The payload renders as a clickable link in the account view. Clicking it invokes the javascript: scheme, running alert(document.cookie) in the victim's browser context. This enables session hijacking or further attacks. Targets are users with view access; outcomes include JS execution and data exfiltration.

## Requirements

1. Stored payload in profile
2. Access to account view page
3. Victim interaction (click)

## Defense

Defensive measures and detection strategies:

- Escape URLs in rendering to prevent scheme execution
- Browser-side URL scheme blocking via CSP or extensions
- Monitor for JS alerts or cookie access anomalies

## Objectives

1. Execute arbitrary JS in victim browser
2. Steal session cookies
3. Demonstrate impact of stored XSS

## Instructions

### Step 1: View Account Details

**Context**: Navigate to where the link is rendered.

No specific command; go to the account details page.

> The website field appears as a link.

### Step 2: Click and Execute

**Context**: Interact to trigger the payload.

No specific command; click the website link.

> An alert displays document.cookie; in real attacks, replace with exfil code.

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
- [[cookie-theft]]

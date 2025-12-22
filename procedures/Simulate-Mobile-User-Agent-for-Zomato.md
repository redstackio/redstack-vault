---
tags:
  - user-agent
  - mobile-simulation
  - web
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:16:14.413Z'
sub_techniques: []
id: 69e13937-e7c9-49a0-802c-b294396a0760
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Simulate-Mobile-User-Agent-for-Zomato

## Summary

This procedure changes the browser's user agent to simulate a mobile device, enabling access to Zomato's mobile website version where the XSS vulnerability exists.

## Description

Zomato's mobile site has a reflected XSS in the category parameter that is not present or exploitable on the desktop version. By spoofing a mobile user agent (e.g., iPhone Safari or Android Chrome), attackers can load the vulnerable interface. This step is crucial for targeting mobile-specific rendering and parameter handling, potentially leading to JavaScript execution in the victim's browser for session hijacking or data theft.

## Requirements

1. Web browser with developer tools (e.g., Chrome or Firefox)
2. Network access to zomato.com
3. Basic knowledge of browser inspection tools

## Defense

Defensive measures and detection strategies:

- Implement user agent validation or device detection to enforce consistent rendering
- Monitor for anomalous user agent switches in logs
- Use Content Security Policy (CSP) to restrict script execution regardless of device

## Objectives

1. Access the mobile-optimized vulnerable endpoint
2. Ensure parameter reflection occurs in a script context
3. Prepare for payload injection without desktop mitigations

## Instructions

### Step 1: Open Browser Developer Tools

**Context**: Access the tools needed to modify the user agent.

Open your browser's developer console (F12 or right-click > Inspect), navigate to the Network or Application tab, and locate the user agent override option.

### Step 2: Set Mobile User Agent

**Context**: Spoof the user agent to mimic a mobile device.

In Chrome DevTools, go to the Device Toolbar (mobile icon) or manually set the user agent to: Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1

Reload the browser or navigate to zomato.com to confirm the mobile view loads.

**Expected Output**: The site displays a mobile layout with touch-optimized elements.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[user-agent]]
- [[mobile-simulation]]

---
id: proc-simulate-mobile-ua-230119
tags:
  - user-agent
  - mobile-simulation
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-11-01T00:00:00Z'
techniques:
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-14T17:24:39.995Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Simulate-Mobile-User-Agent-Access

## Summary

This procedure simulates a mobile device by modifying the browser's user agent string to access Zomato's mobile-optimized website, which exposes the vulnerable reflected XSS endpoint not present in the desktop version.

## Description

In the context of exploiting web vulnerabilities like reflected XSS, simulating a mobile user agent is crucial for targeting mobile-specific implementations. Zomato's site serves different code paths based on the user agent, and the mobile version inadequately sanitizes the 'category' parameter in photos pages. This step ensures the attacker loads the correct interface without needing a physical mobile device. Expected outcomes include loading the mobile UI, confirming vulnerability exposure.

## Requirements

1. Web browser with developer tools (e.g., Chrome, Firefox)
2. Network access to Zomato.com
3. Basic knowledge of browser inspection tools

## Defense

Defensive measures and detection strategies:

- Implement user agent validation or normalization on the server side to prevent spoofing
- Monitor for anomalous user agent patterns in access logs
- Use Content Security Policy (CSP) to restrict script execution regardless of device

## Objectives

1. Load Zomato's mobile site to access vulnerable endpoints
2. Verify mobile-specific UI elements are present
3. Set up for subsequent payload injection

## Instructions

### Step 1: Open Browser Developer Tools

**Context**: Access the tools needed to modify the user agent for the session.

Open your browser's developer console (F12 or right-click > Inspect) and navigate to the Network or Application tab where user agent overrides are available.

### Step 2: Switch User Agent to Mobile

**Context**: Change the user agent to mimic a mobile device, triggering the mobile site.

In Chrome DevTools, go to the Device Toolbar (mobile icon) or use the console to set `navigator.userAgent` temporarily. Set it to a string like `Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.1.2 Mobile/15E148 Safari/604.1` for iOS or similar for Android.

> This overrides the user agent for the current tab or session, ensuring mobile rendering.

### Step 3: Verify Mobile Site Load

**Context**: Confirm the switch by accessing Zomato.com.

Navigate to `https://www.zomato.com` and check for mobile UI elements like hamburger menus or touch-optimized layouts.

**Expected Output**: Site loads with mobile viewport and features.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[user-agent]]
- [[mobile-simulation]]

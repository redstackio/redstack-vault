---
tags:
  - recon
  - js-analysis
  - api-discovery
type: procedure
tools: []
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/zomato-deactivate-special-menu-js-snippet]]'
platforms:
  - Web
techniques:
  - '[[Gather Victim Host Information]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: 9a4c04fe-388c-4eb4-b6a1-b5ee8634ca1c
created_at: '2025-12-14T17:25:29.765Z'
updated_at: '2025-12-14T17:25:29.765Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Gather Victim Host Information]]'
---
# Analyze JavaScript for Vulnerable API Endpoints

## Summary

This procedure involves inspecting client-side JavaScript code in the Zomato application to identify API endpoints and request structures for special menu management that lack proper authorization checks, revealing potential IDOR vulnerabilities.

## Description

In web applications like Zomato, client-side code often exposes API details. By searching for functions handling menu deactivation, attackers can find POST requests that use parameters like request_type, user_id, and menu_set_id without verifying restaurant ownership. This step is crucial for understanding the attack surface and crafting subsequent exploits. Prerequisites include access to the Zomato web app and browser developer tools.

## Requirements

1. Authenticated session in Zomato web or mobile app
2. Browser with developer console (e.g., Chrome DevTools)
3. Basic knowledge of JavaScript and API structures

## Defense

Defensive measures and detection strategies:

- Obfuscate or minify client-side JavaScript to hide API details
- Implement server-side logging of API calls for anomaly detection (e.g., unusual res_id usage)
- Use Content Security Policy (CSP) to limit script execution

## Objectives

1. Discover vulnerable API endpoints for special menu operations
2. Extract request parameters and formats for exploitation
3. Confirm lack of authorization in client code

## Instructions

### Step 1: Inspect Application JavaScript

**Context**: Load the Zomato app and search for menu management functions to find exposed API calls.

**Command** ([[commands/zomato-deactivate-special-menu-js-snippet]]):
```javascript
var a={request_type:"deactivate-special-menu",user_id:USER_ID,menu_set_id:e}; $.post("XXX/XXXXXX")
```

> This snippet constructs a POST request without ownership checks. Paste it into the console or search for similar code in sources. Expected output: Identification of endpoint "/XXX/XXXXXX" and parameters like menu_set_id.

### Step 2: Validate Vulnerability Indicators

**Context**: Test if the found function bypasses auth by reviewing the code for missing res_id validation.

> Manually review the $.post call for authorization headers or checks. Success: No visible ownership verification.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]]

### Techniques

- [[Gather Victim Host Information]]

### Sub-Techniques


## Commands Used

- [[commands/zomato-deactivate-special-menu-js-snippet]]

## Tools Used


## Tags

- [[recon]]
- [[js-analysis]]

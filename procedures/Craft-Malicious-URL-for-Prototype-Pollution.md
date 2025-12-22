---
id: proc-uuid-craft-url-pollution
tags:
  - prototype-pollution
  - url-crafting
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-13T23:56:04.023Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Craft-Malicious-URL-for-Prototype-Pollution

## Summary

This procedure involves constructing a malicious URL hash to exploit prototype pollution in the deparam function of the Swiftype CDN JavaScript script, setting arbitrary properties on Object.prototype without authentication.

## Description

The attack targets the vulnerable deparam function in https://s.swiftypecdn.com/install/v2/st.js, which parses location.hash by splitting on '&' and '=' without safeguards against __proto__. By crafting a hash like #__proto__[asd]=alert(document.domain), attackers can pollute the global Object.prototype. This is a precursor to further exploitation, such as XSS, and affects any site loading the script, like https://blog.swiftype.com/. Prerequisites include identifying sites using the vulnerable script version.

## Requirements

1. Access to a web browser or URL shortener for delivery
2. Knowledge of the target site's base URL (e.g., https://blog.swiftype.com/)
3. No special tools; manual string construction suffices

## Defense

Defensive measures and detection strategies:

- Sanitize URL hash parsing to block __proto__, constructor, or prototype access
- Use Object.create(null) for parsing objects to avoid prototype inheritance
- Monitor for anomalous JS execution via Content Security Policy (CSP) with strict script-src

## Objectives

1. Pollute Object.prototype with arbitrary key-value pairs
2. Prepare for gadget chain exploitation in the same script
3. Enable non-interactive delivery via phishing links

## Instructions

### Step 1: Identify Target Site and Script

**Context**: Confirm the target loads the vulnerable Swiftype script at https://s.swiftypecdn.com/install/v2/st.js.

Inspect the page source or network tab in browser dev tools to verify script inclusion.

**Expected Output**: Confirmation of script URL in page resources.

### Step 2: Construct Pollution Payload

**Context**: Build the hash fragment to target __proto__ and set a property that can be evaluated later.

Manually craft the string: Base URL + #__proto__[property]=javascript_payload. For example, use 'asd' as property and 'alert(document.domain)' as value.

**Expected Output**: Full URL: https://blog.swiftype.com/#__proto__[asd]=alert(document.domain).

### Step 3: Validate Payload Syntax

**Context**: Ensure the hash parses correctly without escaping issues.

Test in a local JS environment: Simulate deparam by splitting the hash and assigning to an object.

**Expected Output**: Object.prototype.property equals the payload string.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[prototype-pollution]]
- [[url-manipulation]]

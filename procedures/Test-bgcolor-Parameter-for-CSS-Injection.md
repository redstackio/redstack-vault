---
id: proc-test-bgcolor-css-injection
tags:
  - css-injection
  - web-vulnerability
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
updated_at: '2025-12-13T23:52:34.316Z'
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
# Test bgcolor Parameter for CSS Injection

## Summary

This procedure tests the bgcolor parameter in the /embed/admin/ endpoint for CSS injection by injecting an encoded payload that closes the intended style rule and applies arbitrary CSS to all elements, such as changing the background to red.

## Description

The vulnerability arises from improper sanitization of the bgcolor parameter, which is directly inserted into a CSS rule like body {background: [value];}. By injecting a payload like %7D*%7Bbackground:red (decoding to }*{background:red}), attackers close the brace, use a universal selector (*), and apply new styles. This targets web applications like Chaturbate's embed feature. Prerequisites include browser access to the public endpoint; no authentication is needed.

## Requirements

1. Web browser with developer tools for URL manipulation and inspection.
2. URL encoder to prepare payloads (e.g., online tools or browser console).
3. Access to the target domain (e.g., chaturbate.com).

## Defense

Defensive measures and detection strategies:

- Sanitize CSS inputs by whitelisting allowed values (e.g., hex colors only) and using CSS-in-JS libraries.
- Implement Content Security Policy (CSP) to restrict inline styles.
- Monitor for anomalous CSS payloads in logs and use WAF rules to block brace/universal selector combinations.

## Objectives

1. Confirm arbitrary CSS injection capability.
2. Visualize breakout via page-wide style changes.
3. Establish foundation for token enumeration.

## Instructions

### Step 1: Prepare and Access Target URL

**Context**: Construct the URL with the encoded payload to test injection without triggering errors.

No command; manually enter in browser address bar:

```url
https://chaturbate.com/embed/admin/?bgcolor=%7D*%7Bbackground:red&tour=nvfS&disable_sound=0&campaign=iNSGX
```

> This decodes to body {background: }*{background:red;}, applying red background to all elements. Inspect the page source to confirm the injected CSS in the <style> tag.

### Step 2: Verify Injection Success

**Context**: Check for visual confirmation of the exploit.

Use browser developer tools (F12) to inspect the <body> style and confirm the red background application.

**Expected Output**: Page renders with red background; no syntax errors in console.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[css-injection]]
- [[web-vulnerability]]

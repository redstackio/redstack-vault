---
id: proc-uuid-1234
tags:
  - xss
  - dom-xss
  - csp-bypass
  - javascript-url
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:49.500Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
  - '[[Execution]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
  - '[[JavaScript]]'
---
# DOM-Based XSS in Reblog Feature

## Summary

This procedure exploits a DOM-Based XSS vulnerability in Tumblr's reblog page due to missing CSP, allowing javascript: URLs to execute upon user interaction, leading to arbitrary JavaScript in the victim's browser.

## Description

The reblog page at /reblog/ID/OTHER_ID lacks proper CSP rules, enabling attackers to embed javascript: URLs in links. When a victim clicks the link and confirms, the payload executes, potentially stealing session data or performing unauthorized actions. Discovered via manual testing of interaction features.

## Requirements

1. Access to Tumblr.com as an attacker
2. Victim logged into Tumblr
3. Web browser without strict URL handling

## Defense

Defensive measures and detection strategies:

- Implement strict CSP with 'unsafe-inline' disallowed for script-src
- Sanitize and validate all URLs to block javascript: schemes
- Monitor for anomalous JavaScript execution in browser consoles

## Objectives

1. Execute arbitrary JavaScript in victim's context
2. Steal session cookies or tokens
3. Perform account takeover actions

## Instructions

### Step 1: Craft and Access Malicious Reblog URL

**Context**: Prepare the vulnerable page with embedded payload.

Navigate to `https://www.tumblr.com/reblog/620008931446652928/JBuEvzz5` containing a link like `<a href="javascript:alert(document.domain)">click me</a>`.

> The page loads without CSP blocking the javascript: URL.

### Step 2: Interact with Malicious Link

**Context**: Trigger DOM parsing of the URL.

Click the 'click me' link to process the javascript: payload.

> Browser attempts to execute the URL scheme.

### Step 3: Confirm Execution

**Context**: Bypass any browser warnings.

Click 'open' in the dialog to run the payload.

> JavaScript executes, e.g., alerting the domain.

### Step 4: Verify Exploitation

**Context**: Confirm impact.

Observe alert or use payload to exfiltrate data, e.g., send cookies to attacker server.

> Successful execution grants access to victim's DOM and session.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access
- [[Execution]] Execution

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application
- [[JavaScript]] JavaScript

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[dom-xss]]
- [[tumblr]]

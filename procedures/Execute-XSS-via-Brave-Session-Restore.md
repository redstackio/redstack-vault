---
id: proc-brave-session-xss
tags:
  - xss
  - javascript-execution
  - privilege-escalation
  - brave-ios
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - iOS
  - Mobile
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
updated_at: '2025-12-14T03:16:14.694Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[JavaScript]]'
  - '[[Exploitation for Privilege Escalation]]'
---
# Execute XSS via Brave Session Restore

## Summary

This procedure exploits an XSS vulnerability in Brave iOS's SessionRestoreHandler.swift by providing unvalidated javascript: URLs during session restoration, allowing arbitrary JavaScript execution on the high-privilege internal://local origin for privilege escalation.

## Description

In Brave iOS 1.32.3 and higher on iOS 14.x and below, the SessionRestoreHandler lacks URL scheme validation, processing arbitrary schemes like javascript: on the internal: domain. Combined with a prior uuidKey leak, attackers can craft exploit URLs to restore malicious JavaScript, executing in a context with access to internal browser APIs and features. This leads to potential data exfiltration or further compromise. The attack requires the victim to interact with a malicious link after the leakage phase.

## Requirements

1. Victim has already leaked uuidKey via prior procedure.
2. Brave iOS 1.32.3+ on iOS 14.x or below.
3. Malicious page with crafted javascript: URL for restoration.

## Defense

Defensive measures and detection strategies:

- Validate all restored URLs in SessionRestoreHandler.swift to block non-http/https schemes like javascript:.
- Sandbox internal://local origin more strictly using WKWebView configurations.
- Monitor for anomalous JavaScript execution in browser logs or crash reports.

## Objectives

1. Deliver and execute arbitrary JavaScript on internal://local.
2. Escalate privileges to access internal app features.
3. Demonstrate full compromise potential.

## Instructions

### Step 1: Craft Exploit URL

**Context**: Prepare the malicious URL that includes the javascript: payload for unvalidated restoration.

On the attacker's page, generate a link like `https://attacker.com/exploit?restore=javascript:alert('XSS on internal')` using the leaked uuidKey if needed for targeting.

### Step 2: Trigger Restoration

**Context**: Have the victim click the exploit URL to invoke SessionRestoreHandler.

Instruct the victim to click the specially crafted hyperlink on the malicious page. The handler processes the javascript: URL without validation, executing it on internal://local.

**Expected Output**: JavaScript runs in privileged context, e.g., alert pops or console logs from internal origin.

### Step 3: Verify Execution

**Context**: Confirm privilege escalation by testing internal access.

Observe if the JS can interact with Brave's internal APIs, such as reading stored data or modifying browser state.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Privilege Escalation]] Privilege Escalation

### Techniques

- [[JavaScript]] Command and Scripting Interpreter: JavaScript
- [[Exploitation for Privilege Escalation]] Exploitation for Privilege Escalation

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- xss
- brave-ios
- privilege-escalation

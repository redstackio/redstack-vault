---
tags:
  - xss-test
  - payload
  - bypass
type: procedure
tools:
  - '[[tools/Browser]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: fcfad662-e8db-43d1-b3d6-5b43efe8164e
created_at: '2025-12-14T03:16:37.181Z'
updated_at: '2025-12-14T03:16:37.181Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Test-Direct-XSS-Payload

## Summary

This procedure attempts a standard reflected XSS payload to demonstrate the module's built-in HTML escaping, which prevents direct script injection but sets the stage for bypass techniques.

## Description

In the vulnerable application, inject a basic <script> tag via the 'name' parameter. The bracket-template module escapes < and > to &lt; and &gt;, rendering the payload inert. This confirms the partial protection while exposing the need for advanced evasion. Tested in browsers like Chrome with XSS Auditor enabled; outcomes show no execution.

## Requirements

1. Active local server on port 8080
2. Browser with console access
3. Knowledge of basic XSS syntax

## Defense

Defensive measures and detection strategies:

- Enable browser XSS auditors and monitor for blocked requests
- Implement web application firewalls (WAF) to flag script tags
- Regularly audit template usage for direct input embedding

## Objectives

1. Validate escaping mechanism
2. Confirm non-execution of direct payloads
3. Prepare for escalation to bypass methods

## Instructions

### Step 1: Inject Standard Payload

**Context**: Test if unescaped HTML/JS can execute directly.

**Command** (Browser URL):

Visit http://localhost:8080?name=bl4de<script>console.log('XSS?')</script> in [[tools/Browser]].

> Output: Escaped HTML shows literal text; no console log. Inspect source to see &lt;script&gt;.

### Step 2: Check for Execution

**Context**: Verify prevention in dev tools.

**Command** (Browser console check):

Open console and refresh.

> Expected: No errors or logs from script. Success if payload is fully escaped.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Browser]]

## Tags

- xss-test
- payload
- bypass

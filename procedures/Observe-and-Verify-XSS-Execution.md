---
tags:
  - xss
  - verification
  - exfiltration
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:52:39.067Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: 53e972a9-1329-4983-b5e0-6883844292b9
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-and-Verify-XSS-Execution

## Summary

This procedure monitors the admin browser for XSS payload execution, confirming arbitrary JavaScript runs, external script loading via XMLHttpRequest, and potential data access.

## Description

After triggering, the payload executes in the admin's session, loading code from //ks.xss.ht and eval-ing it. This bypasses CSP's unsafe-inline allowance by using event listeners on XHR. In the attack, this could lead to AJAX requests stealing user info. Observe via dev tools or Burp for network activity. Expected outcome: Confirmed JS execution and exfiltration capability.

## Requirements

1. Access to admin browser session (simulated)
2. Burp Suite for network monitoring
3. Hosted script on external domain

## Defense

Defensive measures and detection strategies:

- Block or log XHR to external domains in CSP
- Use browser security extensions or WAF on admin panel
- Monitor for eval() usage or anomalous network calls from admin sessions

## Objectives

1. Verify script execution and CSP bypass
2. Confirm external code load
3. Demonstrate impact like data access

## Instructions

### Step 1: Monitor Browser Console

**Context**: Open dev tools in the admin browser to watch for JS errors or logs from the payload.

**Command** (Browser-based):

> In console: Monitor for 'load' event or eval execution.

> Expected output: No errors; potential alert or log from external script.

### Step 2: Inspect Network Traffic

**Context**: Use Burp or dev tools to capture XHR requests confirming external load.

**Command** (Burp-integrated):

> In Burp Proxy > HTTP history, filter for ks.xss.ht.

> Expected output: GET request to //ks.xss.ht with 200 status, response evaluated.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[xss]]
- [[verification]]

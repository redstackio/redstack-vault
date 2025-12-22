---
tags:
  - xss
  - execution
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Collection]]'
commands:
  - '[[commands/monitor-xss-execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-14T17:30:07.332Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 996849c0-77ef-4ff2-9395-51c589af4e46
validated: true
mitre_tactics:
  - '[[Collection]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Observe-and-Verify-XSS-Execution

## Summary

This procedure monitors the admin page for XSS payload execution, confirming JavaScript runs via external XHR and enables data collection in the admin context.

## Description

Upon rendering, the payload executes, using XHR to fetch and eval JS from //ks.xss.ht, bypassing CSP. This allows AJAX requests for stealing private info (e.g., session data). Prerequisites: Loaded admin page. Expected outcome: Confirmed execution with network activity.

## Requirements

1. Browser dev tools or Burp proxy active
2. Attacker domain with verification JS (e.g., alert or callback)

## Defense

Defensive measures and detection strategies:

- Block external XHR in CSP (strict-src)
- Monitor admin browser for unexpected network calls
- Implement client-side XSS auditors
- Alert on eval() usage in scripts

## Objectives

1. Verify script execution on page load
2. Confirm CSP bypass and external load
3. Demonstrate potential data exfiltration

## Instructions

### Step 1: Load Page and Monitor Network

**Context**: Open the admin page in a browser with dev tools.

**Command** ([[commands/monitor-xss-execution]]):
```bash
# Use browser dev tools; or proxy logs in Burp
tail -f /path/to/burp/logs | grep 'ks.xss.ht'
```

> Monitors for requests. Expected output: GET request to //ks.xss.ht.

### Step 2: Check Console for Execution

**Context**: Look for eval or errors indicating success.

**Command** ([[commands/monitor-xss-execution]]):
```bash
# Browser console check
console.log('XSS executed if this appears via payload')
```

> If payload includes logging, see output. Expected output: No errors; successful eval.

## MITRE ATT&CK Mapping

### Tactics

- [[Collection]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/monitor-xss-execution]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- xss
- execution

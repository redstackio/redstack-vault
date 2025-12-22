---
tags:
  - xss
  - reflected-xss
type: procedure
tools:
  - '[[tools/Curl]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-cache-test]]'
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: 3aa9da39-e65f-44da-974f-b2b060072b9a
created_at: '2025-12-13T09:00:34.263Z'
updated_at: '2025-12-13T09:00:34.263Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Verify and Execute Reflected XSS

## Summary

This procedure verifies the successful execution of a reflected XSS payload stored via cache deception by accessing the cached page and observing script behavior.

## Description

After injection, the attacker or victim accesses the cached URL, causing the browser to execute the reflected script. This can lead to session hijacking or data theft on platforms like Algolia if not mitigated.

## Requirements
1. Cached URL with injected payload
2. Web browser or request tool for verification
3. Safe testing environment to avoid real harm

## Defense

Defensive measures and detection strategies:
- Enable Content Security Policy (CSP) to block unauthorized scripts
- Monitor for JavaScript execution anomalies in browser logs

## Objectives
1. Confirm script execution
2. Demonstrate impact like alert pop-up
3. Assess potential for further exploits

## Instructions

### Step 1: Retrieve Cached Response

**Context**: Fetch the cached page to check for payload.

**Command** ([[commands/curl-cache-test]]):
```bash
curl "https://target.algolia.com/search?query=<script>alert('XSS')</script>/fake.js"
```

> Verify the response body contains the script.

### Step 2: Execute in Browser

**Context**: Navigate to the URL in a browser to trigger execution.

**Instructions**: Open the URL in a web browser and observe the alert or script action.

> No command needed; manual verification.

## MITRE ATT&CK Mapping

### Tactics
- [[Execution]]

### Techniques
- [[JavaScript]]

### Sub-Techniques

## Commands Used
- [[commands/curl-cache-test]]

## Tools Used
- [[tools/Curl]]

## Tags
- xss
- reflected-xss

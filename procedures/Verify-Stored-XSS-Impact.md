---
tags:
  - stored-xss
  - web-exploitation
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Execution]]'
commands: []
platforms:
  - Web
techniques:
  - '[[JavaScript]]'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 27bc9a5a-9661-4a67-86ec-ec7a2f0972ed
created_at: '2025-12-11T03:47:56.909Z'
updated_at: '2025-12-11T03:47:56.909Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0002]]'
mitre_techniques:
  - '[[T1059.007]]'
---
# Verify Stored XSS Impact

## Summary

This procedure checks if the poisoned cache leads to stored XSS by accessing the affected page and observing attacker content execution.

## Description

After cache poisoning, users accessing the sign-in page may render attacker-injected JavaScript, enabling XSS. This verifies the attack's impact on page integrity in a web environment.

## Requirements

1. Poisoned cache from prior steps
2. Browser or tool to simulate user access
3. XSS payload hosted on attacker domain

## Defense

Defensive measures and detection strategies:

- Use Content-Security-Policy headers
- Monitor for unexpected script executions in client-side logs

## Objectives

1. Confirm cache serves poisoned content
2. Execute XSS payload in target context
3. Assess integrity interference

## Instructions

### Step 1: Access Cached Page

**Context**: Simulate a legitimate user request to trigger the poisoned cache.

Use a browser or tool to visit https://paypal.com/signin.

> Observe if redirect occurs or content is altered.

### Step 2: Test for XSS Execution

**Context**: Verify if injected content executes.

Execute [[commands/test-cached-page-access]]:

```bash
curl -v https://paypal.com/signin
```

> Check response for XSS payload indicators like <script>alert('XSS')</script>.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques

## Commands Used

- [[commands/test-cached-page-access]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[procedures/Verify-Stored-XSS-Impact]]
- #verification

---
tags:
  - ssti
  - rce
  - escalation
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/curl-submit-registration-form]]'
platforms:
  - Web
techniques:
  - '[[Command-Line Interface]]'
skill_level: advanced
impact_level: high
detection_risk: high
sub_techniques: []
id: 47a29cae-1865-417c-b337-48c8fe2771e3
created_at: '2025-12-13T09:01:16.957Z'
updated_at: '2025-12-13T09:01:16.957Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
---
# Escalate SSTI to Malicious Payloads

## Summary

This procedure escalates the confirmed SSTI vulnerability by injecting advanced payloads to achieve remote code execution, sensitive information disclosure, or server attacks.

## Description

Building on the basic injection, more complex payloads (e.g., for command execution or variable access) are injected into the First Name field. Outcomes depend on the template engine but can include RCE or data exfiltration via emails.

## Requirements

1. Confirmed SSTI from prior steps
2. Knowledge of template engine (e.g., Jinja2, Twig)
3. HTTP client for form submission

## Defense

Defensive measures and detection strategies:

- Restrict template execution privileges
- Implement WAF rules for injection patterns

## Objectives

1. Inject escalated payloads
2. Observe execution effects in emails or responses
3. Achieve RCE or disclosure

## Instructions

### Step 1: Craft and Inject Escalated Payload

**Context**: Develop a payload for RCE or disclosure and submit via registration.

**Command** ([[commands/curl-submit-registration-form]]):
```bash
curl -X POST https://www.glovoapp.com/kg/en/bishkek/register -d 'first_name={{escalated_payload_here}}' -d 'email=your@email.com' -d 'password=yourpassword'
```

> Replace with actual payload; monitor for effects.

### Step 2: Verify Escalation Outcomes

**Context**: Check emails or server behavior for signs of successful execution.

> Look for disclosed data or command output in email content.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Command-Line Interface]]

### Sub-Techniques



## Commands Used

- [[commands/curl-submit-registration-form]]

## Tools Used



## Tags

- [[ssti]]
- [[rce]]

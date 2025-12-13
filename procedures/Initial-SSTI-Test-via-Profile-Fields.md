---
tags:
  - ssti
  - smarty
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/smarty-ssti-test-math]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
id: 0486a465-4273-44aa-b2bc-82c478b871b4
created_at: '2025-12-13T09:01:17.037Z'
updated_at: '2025-12-13T09:01:17.037Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initial SSTI Test via Profile Fields

## Summary

This procedure tests for Server-Side Template Injection (SSTI) by injecting a simple mathematical expression into user profile fields, which are rendered in invitation emails, to confirm if the input is evaluated as template code.

## Description

The attack targets the Smarty templating engine on a PHP backend. By editing profile fields like firstname, lastname, and nickname, and triggering an invitation email, the payload is processed, potentially revealing a template error or evaluated result, indicating SSTI. This is the initial step in escalating to code execution.

## Requirements

1. Valid user account with profile editing access
2. Ability to send invitation emails
3. Access to a secondary email to receive invitations

## Defense

Defensive measures and detection strategies:

- Implement input sanitization for template variables
- Monitor for unusual patterns in email templates or logs indicating injection attempts

## Objectives

1. Confirm SSTI vulnerability
2. Observe template evaluation in emails
3. Prepare for version confirmation and escalation

## Instructions

### Step 1: Inject Test Payload

**Context**: Edit the user profile to include the mathematical expression and trigger the email.

**Command** ([[commands/smarty-ssti-test-math]]):
```bash
{7*7}
```

> Set firstname, lastname, and nickname to this payload; invite a friend using another email; observe template error in the received email indicating Smarty injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/smarty-ssti-test-math]]

## Tools Used



## Tags

- [[ssti]]
- [[smarty]]

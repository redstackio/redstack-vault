---
id: proc-uuid-1
tags:
  - ssti
  - smarty
  - detection
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Reconnaissance]]'
commands:
  - '[[commands/smarty-math-test]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Active Scanning]]'
updated_at: '2025-12-14T17:24:08.608Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Reconnaissance]]'
mitre_techniques:
  - '[[Active Scanning]]'
---
# Test-for-Smarty-SSTI-with-Math-Expression

## Summary

This procedure tests for Server-Side Template Injection (SSTI) in Smarty by injecting a simple math expression into user-controlled profile fields, triggering a parsing error when the template is rendered in email invitations.

## Description

In the Unikrn vulnerability, user inputs like firstname, lastname, and nickname are inserted unsanitized into Smarty templates for email generation. Injecting Smarty syntax like {7*7} causes a template error if SSTI is present, confirming the vulnerability without executing code. This is a low-risk detection step requiring only profile edit access and email triggering.

## Requirements

1. Valid user account with profile editing permissions
2. Ability to send email invitations
3. Access to view received emails

## Defense

Defensive measures and detection strategies:

- Sanitize or escape user inputs before template insertion
- Disable Smarty's PHP tag support and limit variable access
- Monitor email generation logs for template errors

## Objectives

1. Detect presence of SSTI in template processing
2. Confirm Smarty-like syntax parsing
3. Establish foundation for further exploitation

## Instructions

### Step 1: Inject Test Payload

**Context**: Modify a profile field to include the math expression, which Smarty will attempt to evaluate during email rendering.

**Command** ([[commands/smarty-math-test]]):
```smarty
{7*7}
```

> Inject this into firstname, lastname, or nickname via the web form (use Burp Suite to intercept if needed). Save the profile changes.

### Step 2: Trigger Template Rendering

**Context**: Generate an email invitation to process the tainted template.

**Instructions**: Navigate to the invitation feature, select a recipient (e.g., yourself), and send the email. Check the inbox for the rendered email.

> Expected output: A template error message in the email, such as a Smarty parsing exception, instead of the numeric result or plain text.

## MITRE ATT&CK Mapping

### Tactics

- [[Reconnaissance]]

### Techniques

- [[Active Scanning]]

### Sub-Techniques


## Commands Used

- [[commands/smarty-math-test]]

## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[ssti]]
- [[smarty]]
- [[detection]]

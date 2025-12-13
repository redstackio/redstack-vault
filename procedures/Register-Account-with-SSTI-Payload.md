---
tags:
  - ssti
  - injection
  - web-vuln
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-submit-registration-form]]'
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
id: c05f1221-bad1-4398-aacb-26f9f275152d
created_at: '2025-12-13T09:01:16.965Z'
updated_at: '2025-12-13T09:01:16.965Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Register Account with SSTI Payload

## Summary

This procedure involves injecting a Server Side Template Injection (SSTI) payload into the First Name field during the Glovo user registration process to test for unsafe template rendering.

## Description

The procedure targets the sign-up form on the Glovo website, where user input is embedded into server-side templates for email generation without proper sanitization. This allows for template expressions to be evaluated, potentially leading to further exploitation.

## Requirements

1. Access to the Glovo website (https://www.glovoapp.com)
2. A valid email address and password for registration
3. Web browser or HTTP client like curl

## Defense

Defensive measures and detection strategies:

- Implement input sanitization and validation for template fields
- Monitor for suspicious patterns in registration data and email subjects

## Objectives

1. Inject and submit SSTI test payload
2. Achieve successful account registration
3. Set up for verification in subsequent steps

## Instructions

### Step 1: Navigate to Registration Form

**Context**: Access the sign-up page to begin the registration process.

**Command** ([[commands/curl-submit-registration-form]]):
```bash
curl https://www.glovoapp.com/kg/en/bishkek/register
```

> Loads the registration form; proceed to fill in fields.

### Step 2: Inject SSTI Payload and Submit

**Context**: Enter the payload '{{7*7}}' in the First Name field and complete submission.

**Command** ([[commands/curl-submit-registration-form]]):
```bash
curl -X POST https://www.glovoapp.com/kg/en/bishkek/register -d 'first_name={{7*7}}' -d 'email=your@email.com' -d 'password=yourpassword'
```

> Submits the form with the injected payload; expect account creation confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/curl-submit-registration-form]]

## Tools Used



## Tags

- [[ssti]]
- [[injection]]

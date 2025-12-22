---
id: c97e03b4-d238-427b-b983-d329f9384ef8
name: Test Basic SSTI Injection in Profile Name
type: procedure
verified: false
submitted: true
created_at: '2025-12-11T03:47:39.269Z'
updated_at: '2025-12-11T03:47:39.269Z'
tactics:
  - '[[Initial Access]]'
techniques:
  - '[[Exploit Public-Facing Application]]'
sub_techniques: []
tags:
  - ssti
  - jinja2
  - web
commands: []
platforms:
  - Web
tools: []
skill_level: beginner
impact_level: medium
detection_risk: low
validated: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---

# Test Basic SSTI Injection in Profile Name

## Summary

This procedure tests for Server-Side Template Injection (SSTI) in Uber's rider profile name field by injecting a simple Jinja2 expression, which is evaluated in the confirmation email, confirming unsanitized rendering.

## Description

The attack targets the profile name update on rider.uber.com, where user input is rendered in a Jinja2 template for emails sent from support@uber.com. By setting the name to a Python expression like string repetition, the email evaluates it, indicating SSTI. This can lead to arbitrary code execution, though limited by input length. The target environment is a web application using Flask and Jinja2, with expected outcomes including confirmed vulnerability for further exploitation.

## Requirements

1. Valid Uber rider account with access to rider.uber.com
2. Ability to receive emails from support@uber.com
3. Web browser for profile updates

## Defense

Defensive measures and detection strategies:

- Sanitize and escape user input in template rendering
- Monitor email template rendering logs for unexpected expressions

## Objectives

1. Confirm SSTI vulnerability in profile name
2. Observe code evaluation in email
3. Establish basis for advanced exploitation

## Instructions

### Step 1: Update Profile Name with Basic Payload

**Context**: Set the profile name to a simple Jinja2 expression to test for injection and evaluation.

**Command** ([[commands/jinja2-basic-expression]]):
```bash
{{ '7'*7 }}
```

> This sets the profile name to the expression, which should render as '7777777' in the email, confirming Python evaluation.

### Step 2: Trigger and Verify Email

**Context**: Update the profile to trigger the confirmation email and check the rendered content.

> Submit the profile update on rider.uber.com and inspect the received email for the evaluated output.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used

- [[commands/jinja2-basic-expression]]

## Tools Used



## Tags

- #ssti
- [[commands/jinja2-basic-expression]]

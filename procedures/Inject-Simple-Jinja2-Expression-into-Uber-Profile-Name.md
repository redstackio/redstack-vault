---
id: p1b2c3d4-e5f6-7890-abcd-ef1234567891
tags:
  - ssti
  - jinja2
  - profile-injection
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T12:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:24:08.807Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Inject-Simple-Jinja2-Expression-into-Uber-Profile-Name

## Summary

This procedure tests for Server-Side Template Injection (SSTI) by injecting a basic Jinja2 expression into the Uber rider profile name field, which is later rendered in email templates.

## Description

In Uber's Flask application using Jinja2, the user profile name is not sanitized before insertion into email templates. By setting the name to a simple expression like `{{ '7'*7 }}`, attackers can confirm injection when the email renders it as '7777777'. This establishes the vulnerability in the rider.uber.com profile update feature, targeting the email generation process.

## Requirements

1. Valid Uber rider account with access to profile settings
2. Web browser to interact with rider.uber.com
3. No special privileges beyond standard user access

## Defense

Defensive measures and detection strategies:

- Sanitize user inputs with Jinja2 escaping before template rendering
- Implement input validation to block template syntax like {{ }}
- Monitor email template logs for anomalous rendering patterns

## Objectives

1. Verify SSTI vulnerability in profile name field
2. Confirm user-controlled input reaches Jinja2 templates
3. Set foundation for advanced exploitation

## Instructions

### Step 1: Access Profile Settings

**Context**: Log in and navigate to the editable profile name field to prepare injection.

Log in to rider.uber.com and go to account settings or profile page.

### Step 2: Inject Payload

**Context**: Update the name field with the test payload to submit unsanitized input.

Enter `{{ '7'*7 }}` as the profile name and save changes.

> This submits the payload to the backend, where it awaits rendering in templates.

**Expected Output**: Profile update confirmation without errors; payload stored for later use.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[ssti]]
- [[jinja2]]
- [[web]]

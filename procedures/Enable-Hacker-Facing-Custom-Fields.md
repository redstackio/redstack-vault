---
tags:
  - xss
  - setup
  - hackerone
type: procedure
tools:
  - '[[tools/Internet-Explorer-11]]'
tactics:
  - '[[Execution]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:56:03.951Z'
skill_level: intermediate
impact_level: low
sub_techniques: []
id: 2cea2eb3-fc54-45c8-a29a-29a81d9fe726
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Enable-Hacker-Facing-Custom-Fields

## Summary

This procedure sets up hacker-facing custom text fields in a HackerOne program, creating a vector for storing unsanitized user input that can later be exploited for stored XSS.

## Description

In the context of exploiting a stored XSS vulnerability in HackerOne, this step involves configuring the program's settings to enable custom fields visible to hackers. This allows malicious payloads to be submitted in reports and rendered without proper sanitization when admins interact with them, particularly in Internet Explorer 11. Prerequisites include admin access to a HackerOne program.

## Requirements

1. Admin or owner access to a HackerOne program
2. Web browser access to hackerone.com
3. Basic familiarity with HackerOne's program management interface

## Defense

Defensive measures and detection strategies:

- Implement input validation and output encoding for all custom fields
- Use Content Security Policy (CSP) to restrict JavaScript execution
- Monitor for unusual custom field configurations in programs

## Objectives

1. Create a storage point for malicious input in reports
2. Ensure the field is hacker-facing to allow payload submission
3. Prepare the environment for XSS exploitation

## Instructions

### Step 1: Access Program Settings

**Context**: Log in and navigate to the custom fields configuration for the target program.

Navigate to `https://hackerone.com/:handle/custom_fields` where `:handle` is the program's handle.

### Step 2: Create New Custom Field

**Context**: Add a new text field that hackers can interact with.

Select "Custom Fields > Hacker Facing Custom Fields", then create a new field with:
- Title: 'hello'
- Type: 'text'
- Visibility: 'Hacker facing'

Click save to apply the changes.

> This field will now appear when hackers submit reports, allowing payload injection.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Internet-Explorer-11]]

## Tags

- [[xss]]
- [[setup]]

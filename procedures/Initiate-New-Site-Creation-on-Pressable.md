---
tags:
  - site-creation
  - web-workflow
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:32.023Z'
sub_techniques: []
id: 5d72dc3e-92fa-4c8f-a18d-fec8e954e36a
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Initiate-New-Site-Creation-on-Pressable

## Summary

This procedure starts the site creation process on try.pressable.com, advancing to the Display Name field where vulnerabilities can be exploited for stored XSS and HTML injection.

## Description

As part of the attack scenario, this manual step follows initial access and simulates legitimate user behavior to reach the unsanitized input. The Pressable platform's workflow lacks backend validation here, storing inputs directly. Outcomes include reaching the injection point without alerts.

## Requirements

1. Active session from previous access step
2. Basic knowledge of web forms
3. No credentials required for trial sites

## Defense

Defensive measures and detection strategies:

- Require CAPTCHA or email verification during site creation
- Log and analyze workflow progression for anomalies
- Sanitize all form inputs at submission

## Objectives

1. Advance to the vulnerable Display Name field
2. Maintain session integrity
3. Avoid triggering any early validations

## Instructions

### Step 1: Begin Site Creation Workflow

**Context**: Follow prompts to initiate a new site, leading to detailed input fields.

No command required; interact with the UI.

Click any 'Start Free Trial' or 'Create Site' button on the page, then proceed through initial prompts like selecting a site name or plan until the Display Name section appears.

> This positions you for injection. Expected output: Display Name field is now active and editable.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[web]]
- [[creation]]

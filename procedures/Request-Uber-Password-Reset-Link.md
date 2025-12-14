---
tags:
  - password-reset
  - uber
  - web
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T03:15:47.287Z'
sub_techniques: []
id: f8a24c84-28ce-41df-85c2-77ddc5c2382d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Request-Uber-Password-Reset-Link

## Summary

This procedure initiates a password reset for an Uber account, sending a reset link to the associated email address, setting up the environment for further exploitation in the password reset form.

## Description

In the context of exploiting a self-XSS vulnerability, this step requests a password reset from Uber's partner portal. The process involves navigating to the login page and submitting an email address, which triggers Uber to email a time-limited reset URL. This is a standard account recovery flow but serves as the entry point for injecting payloads in subsequent steps. The target environment is the web-based Uber partners portal at https://partners.uber.com/. Expected outcome is receipt of a functional reset link without errors.

## Requirements

1. Access to an email address linked to a valid Uber account
2. Web browser with internet connectivity
3. No prior authentication required

## Defense

Defensive measures and detection strategies:

- Rate limiting on password reset requests to prevent abuse
- Email verification and logging of reset attempts
- Monitoring for unusual reset patterns from the same IP

## Objectives

1. Obtain a valid password reset URL
2. Prepare for payload injection in the reset form
3. Validate account accessibility

## Instructions

### Step 1: Navigate to Uber Login

**Context**: Access the Uber partners login page to start the reset process.

Go to https://partners.uber.com/ and click on the 'Forgot Password' or similar link.

> This loads the password reset request form.

### Step 2: Submit Email for Reset

**Context**: Provide the target email to receive the reset link.

Enter the email address associated with the Uber account and submit the form.

> Uber processes the request and sends an email with the reset URL; check the inbox (including spam) for the link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[uber]]
- [[web]]

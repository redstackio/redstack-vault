---
tags:
  - xss
  - web
  - uber
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
updated_at: '2025-12-14T03:15:47.280Z'
sub_techniques: []
id: 144f2f14-f5cc-4935-9895-accdcbbaa9ae
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Navigate-to-Uber-Forgot-Password-Page

## Summary

This procedure accesses the Uber forgot password page to begin the recovery process, serving as the initial entry point for exploiting the self-XSS vulnerability.

## Description

In the context of testing Uber's password recovery for XSS, this step involves directly loading the forgot password URL in a browser. It requires no authentication and sets up the flow for subsequent injection. The target environment is Uber's web application at https://login.uber.com/forgot-password. Expected outcome is the form loading without errors, allowing email input.

## Requirements

1. Web browser with JavaScript enabled
2. Internet access to reach Uber's login domain
3. No credentials needed

## Defense

Defensive measures and detection strategies:

- Rate limiting on forgot password requests to prevent abuse
- CAPTCHA on repeated access to the page

## Objectives

1. Gain access to the password recovery interface
2. Prepare for email submission
3. Confirm the endpoint is live and unmodified

## Instructions

### Step 1: Load the Forgot Password URL

**Context**: Directly navigate to the specific Uber endpoint to initiate the recovery flow.

No command required; use browser address bar:

```plaintext
https://login.uber.com/forgot-password
```

> This loads the form. Verify the page title or URL matches exactly.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[xss]]
- [[web]]
- [[uber]]

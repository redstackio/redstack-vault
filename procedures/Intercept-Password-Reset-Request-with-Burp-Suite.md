---
tags:
  - burp-suite
  - http-interception
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Content-Type-Converter]]'
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Exploit Public-Facing Application]]'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
id: f746bfd6-4edd-4fb2-8378-9e8af6b47d02
created_at: '2025-12-11T06:10:31.176Z'
updated_at: '2025-12-11T06:10:31.176Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[TA0001]]'
mitre_techniques:
  - '[[T1190]]'
---
# Intercept Password Reset Request with Burp Suite

## Summary

This procedure uses Burp Suite to capture the HTTP request sent during the GitLab password reset submission, allowing for subsequent modification.

## Description

After submitting the password reset form, Burp Suite's proxy is used to intercept the outgoing request. This enables inspection and alteration of the request parameters. The procedure targets web applications like GitLab and requires Burp Suite configured as a proxy in the browser.

## Requirements

1. Burp Suite installed and running
2. Browser configured to use Burp proxy
3. Active password reset submission

## Defense

Defensive measures and detection strategies:

- Use HTTPS to encrypt requests
- Monitor for proxy usage indicators

## Objectives

1. Capture the reset request
2. Prepare for payload modification
3. Enable vulnerability exploitation

## Instructions

### Step 1: Enable Interception

**Context**: Ensure Burp Suite's intercept is on in the Proxy tab.

Submit the form and wait for the request to be captured.

> Inspect the request details in Burp Suite.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques



## Commands Used



## Tools Used

- [[tools/Burp-Suite]]

## Tags

- burp-suite
- http-interception

---
tags:
  - nextcloud
  - intercept
  - http-request
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T17:28:28.127Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: fc2cf254-f056-4df9-88b3-d3f8c3eabd68
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Intercept-Password-Reset-Request

## Summary

This procedure submits a password reset request on Nextcloud and intercepts the HTTP POST using Burp Suite, capturing details for replay and analysis.

## Description

Target the /lostpassword/email endpoint by entering an email (e.g., yougovxxx@gmail.com) in the reset form and submitting. With Burp proxying, intercept the request which includes a JSON body {"user":"email"} and headers like Content-Type: application/json, Requesttoken. This allows inspection and forwarding to Repeater/Intruder. Expected outcome: Single reset email sent, request captured.

## Requirements

1. Access to login page from previous procedure
2. Burp Suite with interception enabled
3. Valid target email for testing

## Defense

Defensive measures and detection strategies:

- Log all password reset attempts with user agents and tokens
- Require CAPTCHA on reset forms to deter automation

## Objectives

1. Capture authentic reset request
2. Verify endpoint behavior
3. Prepare for rate limit testing

## Instructions

### Step 1: Submit Reset Form

**Context**: Trigger the reset to generate the request.

On the login page, click 'Forgot password?', enter the email, and submit.

### Step 2: Intercept in Burp

**Context**: Capture and inspect the POST request.

In Burp Proxy > Intercept, catch the POST /lostpassword/email. View raw request: method POST, body {"user":"yougovxxx@gmail.com"}, headers (Cookie, User-Agent: Mozilla/5.0..., Accept: application/json, Content-Type: application/json;charset=utf-8, Requesttoken: ...).

> Expected output: Request details displayed; forward to continue (email arrives).

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- [[nextcloud]]
- [[intercept]]

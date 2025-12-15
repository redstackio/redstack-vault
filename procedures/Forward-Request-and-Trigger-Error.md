---
id: proc-713407-forward-trigger
tags:
  - forward
  - trigger
  - error
  - dos
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
tactics:
  - '[[Privilege Escalation]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Endpoint Denial of Service]]'
updated_at: '2025-12-14T17:26:56.288Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Privilege Escalation]]'
mitre_techniques:
  - '[[Endpoint Denial of Service]]'
---
# Forward-Request-and-Trigger-Error

## Summary

This procedure submits the modified upload request to trigger an ActiveStorage exception, causing an internal server error on the profile page and initiating the DoS.

## Description

After filename modification, forwarding the request to the HackerOne server (Ruby on Rails with ActiveStorage) results in an exception during file processing due to unsanitized special characters. This crashes the page rendering the image. Assumes interception is complete and targets https://hackerone.com/profile.

## Requirements

1. Modified request ready in Burp Suite
2. Server access via proxied connection
3. Valid session cookie in request

## Defense

Defensive measures and detection strategies:

- Implement filename sanitization and validation in ActiveStorage
- Monitor for 500 errors correlated with uploads

## Objectives

1. Submit the malicious upload
2. Observe immediate server exception
3. Confirm error on profile refresh

## Instructions

### Step 1: Disable Interception

**Context**: Allow the request to proceed to the server.

No command required; in Burp Proxy > Intercept, turn off interception.

> Request flows to server without further halts.

### Step 2: Forward and Refresh

**Context**: Trigger the processing and view the error.

No command required; forward the request in Burp, then refresh the profile page in the browser.

> Server returns 500 Internal Server Error; page fails to load.

## MITRE ATT&CK Mapping

### Tactics

- [[Privilege Escalation]] Impact

### Techniques

- [[Endpoint Denial of Service]] Endpoint Denial of Service

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Suite]]

## Tags

- forward
- trigger
- error
- dos

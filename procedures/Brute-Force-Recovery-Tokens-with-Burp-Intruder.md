---
id: p-brute-force-tokens
tags:
  - brute-force
  - auth-bypass
type: procedure
tools:
  - '[[tools/Burp-Intruder]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Password Guessing]]'
updated_at: '2025-12-14T17:31:31.152Z'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Password Guessing]]'
---
# Brute-Force-Recovery-Tokens-with-Burp-Intruder

## Summary

This procedure uses Burp Intruder to automate testing of generated recovery tokens against the Revive Adserver password reset endpoint, achieving authentication bypass and admin access.

## Description

Load the candidate tokens into Burp Intruder as a payload list and send POST requests to the recovery validation endpoint. Monitor responses for success indicators like redirect to reset form or valid token acceptance, leading to password change and login.

## Requirements

1. Burp Suite Professional
2. List of generated tokens
3. Captured recovery request template

## Defense

Defensive measures and detection strategies:

- Rate limit token validation attempts
- Use CAPTCHA on reset pages
- Monitor for high-volume requests to recovery endpoints

## Objectives

1. Automate token trials
2. Identify the correct recovery ID
3. Complete password reset for admin takeover

## Instructions

### Step 1: Capture Base Request

**Context**: Intercept a password reset request in Burp Proxy.

Navigate to the recovery page and capture the POST with the recovery_id parameter.

### Step 2: Configure Intruder Attack

**Context**: Set up payload positions and list.

In Intruder, mark §recovery_id§ as payload position, load tokens.txt as payloads, and start the attack. Use grep for success strings in responses.

**Expected Output**: Response with successful reset or login prompt.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Password Guessing]] Brute Force: Password Guessing

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/Burp-Intruder]]

## Tags

- intruder
- bypass

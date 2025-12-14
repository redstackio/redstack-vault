---
id: proc-trigger-reset-001
tags:
  - password-reset
  - rubygems
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
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:33:06.228Z'
skill_level: beginner
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Trigger RubyGems Password Reset

## Summary

This procedure initiates the password reset functionality on RubyGems.org, sending an email with a reset link in clear text, setting up the conditions for interception.

## Description

In the context of exploiting unencrypted email transmission from RubyGems (hosted on AWS EC2), this step triggers the reset process via the public-facing web interface. No authentication is required beyond providing a valid email address associated with an account. The email is sent without TLS, as evidenced by headers from the EC2 instance, making it vulnerable to MITM attacks. Expected outcome: Generation of a time-sensitive reset link in an interceptable email.

## Requirements

1. Access to the internet and the RubyGems website (https://rubygems.org)
2. Knowledge of the victim's registered email address
3. No special tools needed; standard web browser suffices

## Defense

Defensive measures and detection strategies:

- Implement TLS/STARTTLS for all outbound email (e.g., enforce SMTP over TLS)
- Monitor for anomalous reset requests via rate limiting or logging
- Use email encryption standards like S/MIME for sensitive links

## Objectives

1. Generate a password reset email containing a sensitive link
2. Confirm transmission from the vulnerable server
3. Prepare for interception in subsequent steps

## Instructions

### Step 1: Access Reset Page

**Context**: Navigate to the password reset endpoint to begin the process.

No command required; use a web browser to visit https://rubygems.org/password/new.

> Enter the victim's email (e.g., victim@gmail.com) and submit the form.

### Step 2: Submit Reset Request

**Context**: Trigger the email send, which will be unencrypted.

No command required; click the submit button on the form.

> Observe the success message: "You will receive an email with instructions on how to reset your password in a few minutes."

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Exploit Public-Facing Application]] Exploit Public-Facing Application

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[web-exploitation]]

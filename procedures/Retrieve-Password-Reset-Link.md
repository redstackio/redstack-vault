---
id: c3d4e5f6-g7h8-9012-cdef-345678901234
tags:
  - password-reset
  - email-retrieval
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Email
  - Web
submitted: true
created_at: '2024-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T17:32:58.373Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Retrieve-Password-Reset-Link

## Summary

This procedure involves accessing the target's original email inbox to obtain the password reset link generated in the previous step, preserving it for use after email changes.

## Description

Following the reset request, the system emails a unique reset URL to the original address (e.g., main@main.com). The attacker, with access to this inbox, copies the link. This step relies on email access and is critical because the link remains valid even after support-mediated email updates, enabling the takeover.

## Requirements

1. Access to the email inbox (main@main.com)
2. Email client or webmail interface
3. The reset request must have been successfully initiated

## Defense

Defensive measures and detection strategies:

- Shorten reset token lifetimes (e.g., 15 minutes)
- Monitor email delivery logs for unusual access patterns
- Use secure email protocols and notify users of reset attempts

## Objectives

1. Secure the reset token link
2. Ensure the link is not consumed prematurely
3. Enable exploitation in later steps

## Instructions

### Step 1: Access Email Inbox

**Context**: Log in to the email service to check for the reset message.

Open the email client and navigate to the inbox for main@main.com.

> Incoming emails should include the reset notification from NordVPN.

### Step 2: Copy Reset Link

**Context**: Extract the URL from the email body for later use.

Locate the password reset email, click or copy the provided URL (e.g., https://ucp.nordvpn.com/reset?token=abc123).

> Paste the link into a secure note or clipboard for safekeeping.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[email-access]]
- [[token-retrieval]]

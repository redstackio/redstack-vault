---
tags:
  - password-reset
  - phishing
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
  - '[[T1566.002]]'
updated_at: '2025-12-14T17:33:12.493Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
id: b1d3b080-a180-4f2f-ae37-a6cef93fffcb
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[T1566.002]]'
---
# Request-Password-Reset-for-Target-User

## Summary

This procedure initiates the password reset flow on the target website to obtain a reset link containing a vulnerable modifiable parameter, setting the stage for redirection exploitation.

## Description

In the context of the Mars website, the password reset functionality emails a link with a path parameter that specifies the post-reset page. This procedure triggers that email, allowing subsequent modification. It requires knowledge of the victim's username or email and assumes the site has no rate limiting on resets. Expected outcome is receipt of the email with the link.

## Requirements

1. Access to the target's password reset page (publicly accessible)
2. Knowledge of victim's email or username
3. Ability to receive or intercept the reset email (e.g., if victim is controlled or email forwarded)

## Defense

Defensive measures and detection strategies:

- Implement rate limiting on password reset requests per IP/email
- Monitor for unusual reset volumes
- Use CAPTCHA on reset forms to prevent automation

## Objectives

1. Obtain the initial reset link with token and path parameter
2. Confirm the vulnerability exists by inspecting the link structure
3. Prepare for link modification

## Instructions

### Step 1: Access Reset Page

**Context**: Navigate to the password reset endpoint to begin the process.

Visit the Mars website's forgot password page, typically at `/forgot-password` or similar, and enter the target's email or username.

> Upon submission, the site processes the request and sends an email.

### Step 2: Retrieve Reset Email

**Context**: Obtain the emailed link for analysis.

Check the email inbox associated with the target account. The link will resemble `https://mars.com/reset?token=abc123&path=/reset-complete`.

> Success is confirmed if the email arrives within seconds to minutes, containing the clickable link.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[T1566.002]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[password-reset]]
- [[Phishing]]

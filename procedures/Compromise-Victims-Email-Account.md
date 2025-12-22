---
tags:
  - email-compromise
  - initial-access
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands: []
platforms:
  - Web
techniques:
  - '[[Valid Accounts]]'
skill_level: intermediate
impact_level: high
detection_risk: high
sub_techniques: []
id: f8234577-d44b-4d56-8ffe-fe979bdf0888
created_at: '2025-12-14T17:24:45.501Z'
updated_at: '2025-12-14T17:24:45.501Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Compromise-Victims-Email-Account

## Summary

This procedure outlines gaining unauthorized access to a victim's email account, which is a prerequisite for intercepting confirmation tokens in services like login.gov, enabling subsequent auth bypass attacks.

## Description

Email compromise provides the attacker with access to sensitive communications, including activation and reset links. In the context of login.gov, this allows retrieval of non-expiring confirmation tokens. The target environment is any email provider (e.g., Gmail, Outlook) associated with the victim's account. Prerequisites include prior reconnaissance on the victim's email credentials via phishing or credential stuffing. Expected outcome: Full read/write access to the inbox.

## Requirements

1. Victim's email address and potential credentials (from prior phishing or leaks)
2. Network access to the email provider
3. Tools for credential testing if not already compromised (e.g., browser or password manager)

## Defense

Defensive measures and detection strategies:

- Enable 2FA on email accounts
- Monitor for unusual login locations via email provider alerts
- Use email security gateways to block phishing attempts

## Objectives

1. Gain access to confirmation emails from login.gov
2. Intercept token-containing links
3. Enable token-based auth bypass

## Instructions

### Step 1: Credential Acquisition

**Context**: Obtain or guess the victim's email credentials to initiate login.

**Instructions**: Use known credentials from prior attacks or test via login form. No specific command; perform manual login to the email provider.

> Successful login grants inbox access; failure indicates need for brute-force or phishing escalation.

### Step 2: Search for Target Emails

**Context**: Locate the specific confirmation email from login.gov.

**Instructions**: Search the inbox for subjects like "Confirm your email" or sender "login.gov". Open and inspect for token links.

> Expected output: Email with URL containing confirmation_token parameter.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques

- None

## Commands Used

- None

## Tools Used

- None

## Tags

- [[email-compromise]]
- [[initial-access]]

---
id: proc-nextcloud-add-mailbox-sieve
tags:
  - nextcloud
  - mail-app
  - setup
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
created_at: '2024-01-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T04:39:09.886Z'
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
# Add-Mailbox-and-Navigate-to-Sieve-Settings

## Summary

This procedure sets up a mailbox in the Nextcloud Mail app and accesses the Sieve filter server settings, which triggers the vulnerable PUT request endpoint for SSRF exploitation.

## Description

In the context of exploiting the Blind SSRF in Nextcloud Mail app v2.0.1, this initial step establishes the necessary configuration interface. By adding a mailbox and navigating to Sieve settings, the application prepares to send a PUT request to /apps/mail/api/sieve/account/{id}, where the sieveHost parameter can later be manipulated. This requires an authenticated user session and assumes the Mail app is installed and enabled.

## Requirements

1. Authenticated access to Nextcloud instance with Mail app v2.0.1.
2. Browser with proxy capabilities (e.g., Burp Suite configured).
3. Valid email account details for mailbox addition.

## Defense

Defensive measures and detection strategies:

- Restrict Mail app to trusted users via role-based access control.
- Monitor for unusual Sieve configuration changes in application logs.

## Objectives

1. Gain access to the Sieve configuration interface.
2. Trigger the PUT request endpoint for interception.
3. Prepare for SSRF payload injection.

## Instructions

### Step 1: Log In and Access Mail App

**Context**: Authenticate to Nextcloud and open the Mail app to add a new mailbox.

No specific command; perform via web UI: Log in, click Mail app, add mailbox with IMAP/SMTP details.

> This creates an account ID (e.g., /account/5) for Sieve settings.

### Step 2: Navigate to Sieve Settings

**Context**: Enter the Sieve filter server configuration to initiate the update request.

No specific command; in Mail settings, go to "Sieve filter server" and attempt to save any changes.

> This sends the interceptable PUT request with default sieve parameters.

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

- nextcloud
- mail-app
- sieve-setup

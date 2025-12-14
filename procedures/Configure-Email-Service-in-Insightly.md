---
id: proc-insightly-email-config-001
tags:
  - configuration
  - email-integration
  - prerequisite-setup
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
  - '[[Valid Accounts]]'
updated_at: '2025-12-13T23:55:20.896Z'
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Valid Accounts]]'
---
# Configure-Email-Service-in-Insightly

## Summary

This procedure integrates an email service into Insightly, enabling the creation and sending of emails whose subjects can be exploited for stored XSS.

## Description

Insightly requires email configuration to handle inbound and outbound messages. This step connects an external email provider, allowing email subjects to be stored in the notification system where sanitization fails, leading to XSS execution upon viewing.

## Requirements

1. Access to an external email account (e.g., Gmail)
2. Insightly account with admin-like permissions for integrations
3. Knowledge of email server settings (IMAP/SMTP)

## Defense

Defensive measures and detection strategies:

- Validate all integrations against allowlisted providers
- Log and review new email service connections
- Use email gateways to scan for malicious content

## Objectives

1. Enable email functionality for payload injection
2. Ensure notifications include email subjects
3. Prepare platform for stored content exploitation

## Instructions

### Step 1: Access Settings

**Context**: Navigate to integration options.

Log in to Insightly, go to Admin > Email Settings.

### Step 2: Add Email Provider

**Context**: Configure connection to external service.

Select 'Add Email Service', choose provider (e.g., Gmail), and enter credentials (OAuth or SMTP/IMAP details).

### Step 3: Test Configuration

**Context**: Verify integration works.

Send a test email from Insightly and confirm receipt in the external account.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Valid Accounts]]

### Sub-Techniques


## Commands Used


## Tools Used


## Tags

- [[configuration]]
- [[email]]


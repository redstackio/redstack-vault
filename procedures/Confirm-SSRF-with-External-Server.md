---
id: proc-2
name: Confirm-SSRF-with-External-Server
tags:
  - ssrf
  - confirmation
  - external-callback
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
  - '[[tools/Burp-Collaborator]]'
tactics:
  - '[[Discovery]]'
commands:
  - '[[commands/post-mail-account-creation-request]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Network Service Scanning]]'
updated_at: '2025-12-14T04:39:09.963Z'
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
# Confirm-SSRF-with-External-Server

## Summary

This procedure confirms the blind SSRF vulnerability by modifying the imapHost parameter to an external server under attacker control, such as Burp Collaborator, and observing outbound connections from the Nextcloud server.

## Description

By altering the imapHost in the POST request to a domain like a Burp Collaborator URL, the server attempts an IMAP connection, resulting in detectable DNS resolutions or TCP connections. This validates that user-supplied inputs are not sanitized, allowing arbitrary outbound requests. Prerequisites include the intercepted request from the prior step and access to a collaboration tool.

## Requirements

1. Intercepted POST request from account setup
2. Burp Collaborator instance running
3. Authenticated Nextcloud session

## Defense

Defensive measures and detection strategies:

- Allowlist valid IMAP/SMTP hosts and ports
- Monitor outbound DNS and TCP connections from application servers
- Log and alert on connections to unknown external domains

## Objectives

1. Verify SSRF by detecting external outbound request
2. Confirm lack of input validation on imapHost
3. Establish proof for further internal exploitation

## Instructions

### Step 1: Modify Payload in Burp

**Context**: Change imapHost to Collaborator domain while keeping other parameters intact.

**Command** ([[commands/post-mail-account-creation-request]]):

In Burp Repeater, edit the JSON:

```bash
# Modified payload example (forward via Burp)
{"imapHost":"abc123.collaborator.burp.net","imapPort":993,"imapSslMode":"tls","imapUser":"user@example.com","imapPassword":"pass","smtpHost":"mysmtpserver.org","smtpPort":465,"smtpSslMode":"tls","smtpUser":"user@example.com","smtpPassword":"pass","accountName":"user@example.com","emailAddress":"user@example.com"}
```

> Forward the request. Expected output: Server response (may error), but check Collaborator for interaction.

### Step 2: Monitor Collaborator

**Context**: Observe evidence of SSRF in the collaboration tool.

No command; use Burp Collaborator poll.

> Look for DNS resolution to the Collaborator domain or attempted TCP connection on port 993. Success: Interaction logged, confirming SSRF.

## MITRE ATT&CK Mapping

### Tactics

- [[Discovery]] Discovery

### Techniques

- [[Network Service Scanning]] Network Service Scanning

### Sub-Techniques


## Commands Used

- [[commands/post-mail-account-creation-request]]

## Tools Used

- [[tools/Burp-Suite]]
- [[tools/Burp-Collaborator]]

## Tags

- ssrf
- confirmation
- external-callback

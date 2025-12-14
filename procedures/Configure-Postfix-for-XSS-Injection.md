---
id: proc-configure-postfix-xss
tags:
  - smtp
  - postfix
  - xss-injection
type: procedure
tools:
  - '[[tools/Postfix]]'
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/postmap-update-recipient-access]]'
  - '[[commands/systemctl-restart-postfix]]'
verified: false
platforms:
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[JavaScript]]'
updated_at: '2025-12-13T23:55:20.754Z'
skill_level: intermediate
impact_level: medium
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[JavaScript]]'
---
# Configure-Postfix-for-XSS-Injection

## Summary

This procedure sets up a Postfix SMTP server to reject emails for a controlled invalid address and inject a stored XSS payload into the rejection error message, enabling exploitation of web applications that unsafely render SMTP errors.

## Description

In the context of exploiting a stored XSS vulnerability on a web application like www.xvideos.com, this procedure configures Postfix (version 3.7.11) to handle incoming validation emails. By editing /etc/postfix/main.cf to include smtpd_recipient_restrictions with check_recipient_access and reject_unverified_recipient, and creating a /etc/postfix/recipient_access file with the entry 'invalid@example.org REJECT 5.1.1 <img src="" onerror="alert('hackerone!')" />', the server rejects emails and returns the payload in the error. This payload is then stored and rendered by the target site without sanitization via the html() method, leading to JavaScript execution after a processing delay.

## Requirements

1. Linux environment with root access for Postfix installation and configuration
2. Network accessibility for the SMTP server (ports 25/587 open)
3. Basic knowledge of SMTP and Postfix configuration files

## Defense

Defensive measures and detection strategies:

- Sanitize all user-controlled inputs, including SMTP error messages, before rendering with html() or similar methods
- Implement content security policy (CSP) to restrict inline JavaScript execution
- Monitor SMTP logs for unusual rejection patterns or custom error messages

## Objectives

1. Primary objective: Inject XSS payload into SMTP error responses for storage in the target application
2. Secondary objective: Simulate email bounce to trigger payload delivery
3. Expected outcome: Payload stored and ready for execution on the /account/email page

## Instructions

### Step 1: Edit Postfix Configuration

**Context**: Update /etc/postfix/main.cf to enable recipient access checks for rejection logic.

**Command** ([[commands/postmap-update-recipient-access]]):
```bash
# First, create /etc/postfix/recipient_access with: invalid@example.org REJECT 5.1.1 <img src="" onerror="alert('hackerone!')" />
postmap /etc/postfix/recipient_access
```

> This hashes the recipient_access file for efficient lookup. Expected output: No errors; creates /etc/postfix/recipient_access.db.

### Step 2: Restart Postfix Service

**Context**: Apply the configuration changes to activate the rejection rule with XSS payload.

**Command** ([[commands/systemctl-restart-postfix]]):
```bash
systemctl restart postfix
```

> Restarts the Postfix service. Expected output: Service restarts without errors; check with 'systemctl status postfix' for confirmation.

### Step 3: Test SMTP Rejection

**Context**: Verify the setup by sending a test email to invalid@example.org.

**Instructions**: Use a tool like telnet or swaks to send an email and confirm the rejection error includes the XSS payload.

**Expected Output**: SMTP response with 5.1.1 error containing the <img> tag payload.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[JavaScript]]

### Sub-Techniques


## Commands Used

- [[commands/postmap-update-recipient-access]]
- [[commands/systemctl-restart-postfix]]

## Tools Used

- [[tools/Postfix]]

## Tags

- smtp
- postfix
- xss-injection

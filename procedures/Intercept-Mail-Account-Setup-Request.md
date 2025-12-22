---
id: proc-1
name: Intercept-Mail-Account-Setup-Request
tags:
  - ssrf
  - intercept
  - nextcloud
type: procedure
tools:
  - '[[tools/Burp-Suite]]'
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
updated_at: '2025-12-14T04:39:09.967Z'
skill_level: intermediate
impact_level: low
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Discovery]]'
mitre_techniques:
  - '[[Network Service Scanning]]'
---
# Intercept-Mail-Account-Setup-Request

## Summary

This procedure intercepts the HTTP POST request sent during mail account creation in the Nextcloud Mail app to capture the JSON payload structure, enabling subsequent modifications for SSRF exploitation.

## Description

In the Nextcloud Mail application, adding a new mail account triggers a POST request to /apps/mail/api/accounts with parameters like imapHost, imapPort, and credentials. Intercepting this request allows inspection and alteration of the imapHost and imapPort to exploit the blind SSRF vulnerability. This step requires authenticated access and a proxy tool like Burp Suite. Expected outcome is visibility into the request format for targeted manipulation.

## Requirements

1. Authenticated session in Nextcloud Mail app
2. Proxy tool (Burp Suite) configured to intercept traffic
3. Valid mail credentials for initial setup attempt

## Defense

Defensive measures and detection strategies:

- Implement request logging for /apps/mail/api/accounts endpoints
- Use web application firewalls (WAF) to monitor unusual payload modifications
- Enforce client-side validation and server-side input sanitization for host/port parameters

## Objectives

1. Capture legitimate request payload for analysis
2. Identify modifiable parameters for SSRF
3. Prepare for vulnerability confirmation

## Instructions

### Step 1: Configure Proxy and Initiate Setup

**Context**: Set up Burp Suite as a proxy and start the mail account addition process to trigger the request.

**Command** ([[commands/post-mail-account-creation-request]]):

Use Burp Suite to intercept the browser traffic. Navigate to Nextcloud Mail, enter mail details, and submit.

```bash
# Simulated via curl for reference (actual use Burp for intercept)
curl -X POST https://nextcloud.example.com/apps/mail/api/accounts \
  -H "Content-Type: application/json" \
  -H "Cookie: your_session_cookie" \
  -d '{"imapHost":"myimapserver.org","imapPort":993,"imapSslMode":"tls","imapUser":"user@example.com","imapPassword":"pass","smtpHost":"mysmtpserver.org","smtpPort":465,"smtpSslMode":"tls","smtpUser":"user@example.com","smtpPassword":"pass","accountName":"user@example.com","emailAddress":"user@example.com"}'
```

> This command sends the POST request; in Burp, intercept before forwarding to view/modify the payload. Expected output: JSON response from server confirming account creation attempt.

### Step 2: Analyze Intercepted Payload

**Context**: Examine the JSON structure to note key parameters like imapHost and imapPort.

No specific command; manually inspect in Burp Repeater.

> Verify parameters such as imapHost (hostname), imapPort (port number), and ssl modes. Success: Payload captured without errors.

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

## Tags

- ssrf
- intercept
- nextcloud

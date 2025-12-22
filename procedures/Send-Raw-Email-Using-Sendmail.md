---
tags:
  - email-sending
  - raw-email
type: procedure
tools:
  - '[[tools/sendmail]]'
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/sendmail-send-raw-email]]'
platforms:
  - Web
  - Linux
techniques:
  - '[[Drive-by Compromise]]'
skill_level: beginner
impact_level: medium
detection_risk: low
sub_techniques: []
id: bd7aa7a8-d0dd-45e4-99c5-64cd73b6d66c
created_at: '2025-12-14T00:11:16.814Z'
updated_at: '2025-12-14T00:11:16.814Z'
verified: false
validated: true
submitted: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Drive-by Compromise]]'
---
# Send Raw Email Using Sendmail

## Summary

This procedure describes sending a raw HTML-formatted email using the sendmail tool to deliver malicious content to a target email service like HEY.com.

## Description

Sendmail allows sending emails directly from the command line by reading from a file containing headers and body. This is useful for delivering crafted payloads without relying on email clients that might alter the content. In the context of the HEY.com XSS, it ensures the encoded malicious HTML remains intact.

## Requirements

1. Access to a Linux system with sendmail installed
2. A prepared email file (e.g., email.txt)
3. Valid recipient email address

## Defense

Defensive measures and detection strategies:

- Monitor incoming emails for raw HTML content
- Block or flag emails sent via sendmail signatures if possible
- Use email gateways to sanitize incoming messages

## Objectives

1. Deliver the malicious email to the victim
2. Ensure the payload is not altered during transmission
3. Trigger the exploit upon viewing

## Instructions

### Step 1: Prepare the Email File

**Context**: Ensure the email.txt file is ready with headers and malicious body.

Verify the file contents before sending.

### Step 2: Execute Sendmail Command

**Context**: Send the email using the command line.

Execute [[commands/sendmail-send-raw-email]] to send the raw email file:

```bash
/usr/sbin/sendmail -t < email.txt
```

> This extracts recipients from headers and sends the email.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Drive-by Compromise]]

### Sub-Techniques



## Commands Used

- [[commands/sendmail-send-raw-email]]

## Tools Used

- [[tools/sendmail]]

## Tags

- [[email-sending]]
- [[raw-email]]

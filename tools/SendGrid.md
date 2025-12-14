---
url: 'https://sendgrid.com'
tags:
  - smtp
  - email
  - spoofing
type: tool
verified: false
platforms:
  - Linux
  - Windows
  - macOS
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:30:58.281Z'
id: c7c42f24-928f-4315-a217-c797c2051727
validated: true
submitted: true
---
# SendGrid

**Status**: Unverified

## Overview

SendGrid is a cloud-based SMTP service for sending transactional and marketing emails, commonly used in security testing for spoofing sender addresses in scenarios where email authentication is weak.

## Description

SendGrid provides an API and SMTP relay for high-volume email delivery with features like custom headers, allowing attackers to spoof From addresses in unauthenticated workflows. In this context, it's used to send GDPR requests to GitLab while impersonating the victim, bypassing basic email checks.

## Features

- Feature 1: API-driven email sending with JSON payloads for custom From/To
- Feature 2: Support for spoofed sender addresses via verified identities
- Feature 3: Delivery tracking and bounce handling

## Installation

### Requirements

- API key from SendGrid account
- curl or similar HTTP client

### Install Commands

No installation needed for API usage; sign up at sendgrid.com.

## Basic Usage

```bash
tool-name --help
```

Wait, SendGrid is API/SMTP, not CLI tool. Basic API call:

```bash
curl -X POST https://api.sendgrid.com/v3/mail/send -H "Authorization: Bearer API_KEY" -d '@email.json'
```

### Common Options

| Option | Description |
|--------|-------------|
| Authorization | Bearer token for API access |
| Content-Type | application/json for payloads |

## Examples

### Example 1: Basic Usage

```bash
curl -X POST https://api.sendgrid.com/v3/mail/send \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"personalizations":[{"to":[{"email":"target@example.com"}]}],"from":{"email":"spoofed@example.com"},"subject":"Test","content":[{"type":"text/plain","value":"Message"}]}'
```

### Example 2: Advanced Usage

```bash
curl -X POST https://api.sendgrid.com/v3/mail/send \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -d '{"personalizations":[{"to":[{"email":"gdpr-request@gitlab.com"}],"subject":"GDPR Request"}],"from":{"email":"victim@example.com"},"content":[{"type":"text/plain","value":"Erasure request under GDPR"}]}'
```

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[Phishing]]

### Tactics

- [[Initial Access]]

## Detection

Indicators and methods for detecting this tool's usage:

- API key logs in cloud environments
- Unusual outbound SMTP traffic to services like SendGrid
- High-volume spoofed emails in email gateways

## Related Procedures


## Related Tools

- [[Mailgun]]
- [[Amazon SES]]

## References

- Official documentation: https://docs.sendgrid.com
- Related resources: SMTP spoofing guides

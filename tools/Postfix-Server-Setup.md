---
id: 24f0e28f-bef3-48d8-af40-963d3e0cf20b
type: tool
verified: true
created_at: '2019-08-28T21:17:19.321730+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Linux
tags:
  - email
  - phishing
  - mail-server
  - mta
url: 'http://www.postfix.org/'
validated: true
---

# Postfix-Server-Setup

**Status**: Unverified

## Overview

Postfix is a free, open-source mail transfer agent (MTA) used for routing and delivering email. In offensive security, it's commonly set up as a phishing server to simulate email-based attacks, send spoofed messages, or test email infrastructure. Setup can be time-intensive but provides a reliable platform for red team phishing campaigns.

## Description

Postfix handles SMTP for sending emails and can be configured for relaying through external services to anonymize sends. It's secure by default, supports TLS, and integrates with tools like SASL for authentication. For phishing, configure it to send bulk emails or integrate with scripts for dynamic content. Note: Proper setup requires domain/DNS configuration to avoid blacklisting; it's easily compromised if not secured (e.g., open relay risks).

## Features

- Feature 1: High-performance email queuing and delivery
- Feature 2: Built-in support for TLS encryption and authentication
- Feature 3: Modular configuration for relays, virtual domains, and spam filtering
- Feature 4: Integration with external tools like Dovecot for IMAP/POP3

## Installation

### Requirements

- Root or sudo access
- Ubuntu/Debian-based system (Kali Linux recommended for pentesting)
- Network access for DNS resolution

### Install Commands

For Kali/Ubuntu:

```bash
[[commands/install-postfix-ubuntu]]
```

For CentOS/RHEL:

```bash
sudo yum install postfix
```

Post-install, edit /etc/postfix/main.cf for basic config.

## Basic Usage

```bash
postconf -n  # View active config
mailq        # Check email queue
```

### Common Options

| Option | Description |
|--------|-------------|
| `-n` | Show non-default config |
| `mailq` | List queued emails |
| `postsuper -d ALL` | Delete all queued emails |

## Examples

### Example 1: Basic Usage

View configuration:

```bash
postconf -n
```

### Example 2: Advanced Usage

Configure relay and test send:

1. Run [[commands/configure-postfix-relay]]
2. Create auth file: `echo '[smtp.gmail.com]:587 user:pass' > /etc/postfix/sasl_passwd && postmap /etc/postfix/sasl_passwd`
3. Reload: `sudo systemctl reload postfix`
4. Send test: [[commands/send-test-email-postfix]]

## MITRE ATT&CK Mapping

This tool is commonly associated with:

### Techniques

- [[T1566.001]] Phishing: Spearphishing Attachment
- [[Web Protocols]] Application Layer Protocol: Web Protocols (for SMTP)

### Tactics

- [[Initial Access]] Initial Access
- [[Reconnaissance]] Reconnaissance

## Detection

Indicators and methods for detecting this tool's usage:

- Detection method 1: Monitor for new MTA services (postfix process, port 25/587 open)
- Detection method 2: Log analysis for unusual SMTP traffic or relay attempts
- Detection method 3: DNS queries for MX records pointing to suspicious IPs

## Related Procedures

```dataview
TABLE name as "Procedure", verified as "Verified"
FROM "procedures"
WHERE contains(tools, this.file.link)
SORT name ASC
LIMIT 10
```

## Related Tools

- [[tools/Mailutils]]
- [[tools/Dovecot]]

## References

- Official documentation: http://www.postfix.org/documentation.html
- Related resources: Kali Linux tools integration guides

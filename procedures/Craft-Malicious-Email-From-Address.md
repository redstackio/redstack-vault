---
id: proc-swiftmailer-from-craft
tags:
  - command-injection
  - swiftmailer
  - rce
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/create-swiftmailer-message-with-injection]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
updated_at: '2025-12-14T17:23:23.887Z'
skill_level: intermediate
impact_level: high
detection_risk: low
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
---
# Craft-Malicious-Email-From-Address

## Summary

This procedure crafts a SwiftMailer message with a malicious 'From' address that injects sendmail command-line options, enabling arbitrary file writes and code execution when processed by the sendmail transport.

## Description

In vulnerable SwiftMailer setups, such as those in Nextcloud, the \OC\Mail\Message::setFrom method fails to sanitize email addresses, allowing attackers to embed sendmail flags like -X (to append content to a file) and -oQ (to control queue directory). This is exploitable if user-controlled input reaches setFrom, such as via public APIs or third-party apps. The attack writes PHP code to a server file, which can then be executed remotely.

## Requirements

1. Access to PHP code execution context in a SwiftMailer-enabled application (e.g., Nextcloud instance)
2. Sendmail transport configured on the server
3. User-controlled input path to the mailer (e.g., API endpoint)

## Defense

Defensive measures and detection strategies:

- Update SwiftMailer to patched versions that validate email formats
- Sanitize all inputs to setFrom, rejecting non-standard addresses
- Monitor sendmail logs for anomalous flags like -X or -oQ
- Use dedicated mail relays without direct command-line access

## Objectives

1. Inject sendmail options into the email transport command
2. Prepare for file write and code execution
3. Achieve initial payload delivery without alerting defenses

## Instructions

### Step 1: Initialize Mailer Message

**Context**: Create a new message object using the application's mailer service to start building the malicious email.

**Command** ([[commands/create-swiftmailer-message-with-injection]]):
```php
$message = \OC::$server->getMailer()->createMessage();
```

> This initializes an empty Swift_Message object. Expected output: A valid $message instance ready for configuration.

### Step 2: Set Crafted From Address

**Context**: Apply the malicious 'From' string to embed sendmail injection, using escaped quotes and flags to bypass parsing.

**Command** ([[commands/create-swiftmailer-message-with-injection]]):
```php
$message->setFrom(['"Attacker@test.com\" -X/var/www/test_swiftmailer/phpcode.php -oQ/tmp test"@test.com']);
```

> The string injects -X to write PHP code (e.g., a shell) to the specified file and -oQ to queue it for execution. Expected output: From header set with embedded commands; no validation errors.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]

### Sub-Techniques


## Commands Used

- [[commands/create-swiftmailer-message-with-injection]]

## Tools Used


## Tags

- command-injection
- swiftmailer
- rce

---
id: proc-swiftmailer-send-trigger
tags:
  - rce
  - sendmail
  - command-injection
type: procedure
tools: []
tactics:
  - '[[Execution]]'
commands:
  - '[[commands/send-swiftmailer-message]]'
verified: false
platforms:
  - Web
  - Linux
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
updated_at: '2025-12-14T17:23:23.882Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
mitre_techniques:
  - '[[Unix Shell]]'
  - '[[Exploit Public-Facing Application]]'
---
# Trigger-Sendmail-Injection-via-Mailer

## Summary

This procedure finalizes and sends the crafted SwiftMailer message, triggering the sendmail transport to execute the injected commands for remote code execution.

## Description

Once the malicious 'From' address is set, configuring the recipient and body ensures the message is processed normally, but the send operation invokes sendmail with the injected flags. This leads to arbitrary file writes (e.g., PHP shells) and potential execution in queue directories, exploiting the lack of validation in SwiftMailer's transport handling.

## Requirements

1. Pre-configured message object with injected 'From' address
2. Valid recipient email and body content
3. Mailer service using sendmail transport (not SMTP or others)

## Defense

Defensive measures and detection strategies:

- Restrict mailer transport to non-command-line options (e.g., SMTP)
- Implement WAF rules to block anomalous email headers
- Audit mailer calls for user-controlled inputs
- Log and alert on file creations in web directories

## Objectives

1. Execute the sendmail command with injected options
2. Write and stage malicious PHP code on the server
3. Achieve RCE by accessing the written file

## Instructions

### Step 1: Set Recipient and Body

**Context**: Add standard email fields to make the message appear legitimate and ensure processing continues.

**Command** ([[commands/send-swiftmailer-message]]):
```php
$message->setTo(['lukas@cloud.wtf']);
$message->setBody('foo', 'text/plain');
```

> Sets a recipient and plain-text body. Expected output: Message fully configured; no errors.

### Step 2: Send the Message

**Context**: Invoke the mailer's send method to trigger the transport, activating the injection.

**Command** ([[commands/send-swiftmailer-message]]):
```php
\OC::$server->getMailer()->send($message);
```

> This calls the underlying sendmail binary with the crafted headers, executing flags like -X to append code to /var/www/test_swiftmailer/phpcode.php and -oQ to /tmp. Expected output: "Message sent" status, with side-effect file write; check server logs/files for confirmation.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]]

### Techniques

- [[Unix Shell]]
- [[Exploit Public-Facing Application]]

### Sub-Techniques


## Commands Used

- [[commands/send-swiftmailer-message]]

## Tools Used


## Tags

- rce
- sendmail
- command-injection

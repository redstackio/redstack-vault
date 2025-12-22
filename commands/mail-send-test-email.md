---
id: e6f9701f-4405-42e2-bb7a-a4a7a96634df
name: mail-send-test-email
type: command
executor: bash
data: mail -s 'Test Subject' $_RECIPIENT_EMAIL < /dev/null
output: null
created_at: '2023-04-06T03:55:58.607182+00:00'
updated_at: '2023-10-10T20:22:15.234874+00:00'
platforms:
  - Linux
tags:
  - smtp
  - test
verified: true
validated: true
---

# mail-send-test-email

## Command

```bash
mail -s 'Test Subject' $_RECIPIENT_EMAIL < /dev/null
```

## Description

This command sends a simple test email via the local mail utility to an SMTP relay, confirming that emails are processed and logged on the target. Use it to verify log writing before injecting malicious payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -s 'Test Subject' | Email subject line | Yes |
| $_RECIPIENT_EMAIL | Target recipient (e.g., root@10.10.10.10) | Yes |
| < /dev/null | Provides empty body to avoid interactive input | Yes |

## Examples

### Basic Usage

```bash
mail -s 'Test Subject' root@10.10.10.10 < /dev/null
```

### With Body Content

```bash
echo "Test body" | mail -s 'Test Subject' root@10.10.10.10
```

## Expected Output

Console output like:

```
Subject: Test Subject
To: root@10.10.10.10

```
No errors indicate successful queuing; check target logs via LFI to confirm receipt.

## Related

- [[procedures/LFI-to-RCE-via-Mail-Log-File-Inclusion]]
- [[commands/telnet-smtp-php-injection]]

---
data: 'MAIL FROM: <aaaaaaaaaaa@tester.com>'
tags:
  - smtp
type: command
output: 'SMTP server acceptance of sender (e.g., 250 OK)'
executor: smtp
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.603Z'
id: d12c9359-e83a-4bfe-9e26-842f764573ef
verified: false
validated: true
submitted: true
---
# smtp-mail-from-tester

## Command

```smtp
MAIL FROM: <aaaaaaaaaaa@tester.com>
```

## Description

Specifies the sender email address in an SMTP session, part of the payload to define the email origin in the SSRF exploit.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| aaaaaaaaaaa@tester.com | Sender email address | Yes |

## Examples

### Basic Usage

```smtp
MAIL FROM: <aaaaaaaaaaa@tester.com>
```

## Expected Output

250 2.1.0 Sender OK.

## Related

- [[commands/smtp-helo-test-org]]
- [[procedures/Create-PHP-Gopher-Redirector-for-SMTP-Commands]]

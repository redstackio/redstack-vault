---
data: 'RCPT TO: <bit-bucket@test.smtp.org>'
tags:
  - smtp
type: command
output: 'SMTP server acceptance of recipient (e.g., 250 OK)'
executor: smtp
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.592Z'
id: f8454e3b-9d09-4852-8ae5-1c845ea4a99c
verified: false
validated: true
submitted: true
---
# smtp-rcpt-to-bitbucket

## Command

```smtp
RCPT TO: <bit-bucket@test.smtp.org>
```

## Description

Declares the recipient email in the SMTP transaction, directing the email to a test address in the exploit payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| bit-bucket@test.smtp.org | Recipient email address | Yes |

## Examples

### Basic Usage

```smtp
RCPT TO: <bit-bucket@test.smtp.org>
```

## Expected Output

250 2.1.5 Recipient OK.

## Related

- [[commands/smtp-mail-from-tester]]
- [[procedures/Create-PHP-Gopher-Redirector-for-SMTP-Commands]]

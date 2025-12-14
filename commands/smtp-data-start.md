---
data: DATA
tags:
  - smtp
type: command
output: 'SMTP server readiness for data (e.g., 354 Start mail input)'
executor: smtp
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.588Z'
id: d08f4b25-f4ce-49c6-8d77-138f806b925e
verified: false
validated: true
submitted: true
---
# smtp-data-start

## Command

```smtp
DATA
```

## Description

Signals the start of the email body transmission in SMTP, allowing the message content to follow in the payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```smtp
DATA
```

## Expected Output

354 End data with <CR><LF>.<CR><LF>.

## Related

- [[commands/smtp-rcpt-to-bitbucket]]
- [[procedures/Create-PHP-Gopher-Redirector-for-SMTP-Commands]]

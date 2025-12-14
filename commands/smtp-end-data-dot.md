---
data: .
tags:
  - smtp
type: command
output: 'SMTP server completion of message (e.g., 250 OK)'
executor: smtp
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.569Z'
id: 910c6ea6-9cc8-4c7a-90f6-455e6b4c2771
verified: false
validated: true
submitted: true
---
# smtp-end-data-dot

## Command

```smtp
.
```

## Description

Ends the SMTP DATA section, finalizing the email send in the Gopher payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```smtp
.
```

## Expected Output

250 2.0.0 OK: queued as...

## Related

- [[commands/smtp-email-body-test-mail]]
- [[procedures/Create-PHP-Gopher-Redirector-for-SMTP-Commands]]

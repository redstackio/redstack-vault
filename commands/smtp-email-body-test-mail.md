---
data: Test mail
tags:
  - smtp
type: command
output: Email body transmitted
executor: smtp
platforms:
  - Web
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:14.578Z'
id: 252b635a-2681-4a77-8996-b15bee3a3205
verified: false
validated: true
submitted: true
---
# smtp-email-body-test-mail

## Command

```smtp
Test mail
```

## Description

Provides the simple email body content in the SMTP DATA section of the exploit payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|

## Examples

### Basic Usage

```smtp
Test mail
```

## Expected Output

Body accepted as part of DATA.

## Related

- [[commands/smtp-data-start]]
- [[procedures/Create-PHP-Gopher-Redirector-for-SMTP-Commands]]

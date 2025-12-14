---
id: cmd-postmap-recipient
data: postmap /etc/postfix/recipient_access
tags:
  - postfix
  - smtp-config
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.747Z'
verified: false
validated: true
submitted: true
---
# postmap-update-recipient-access

## Command

```bash
postmap /etc/postfix/recipient_access
```

## Description

This command updates the Postfix database by hashing the specified recipient access file, enabling efficient lookups for rejection rules including custom error messages with XSS payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /etc/postfix/recipient_access | Path to the recipient access file containing rejection rules | Yes |

## Examples

### Basic Usage

```bash
postmap /etc/postfix/recipient_access
```

### Advanced Usage

```bash
postmap -q invalid@example.org hash:/etc/postfix/recipient_access
```

## Expected Output

No stdout output on success; creates .db file. Errors if file not found or permissions issue.

## Related

- [[commands/systemctl-restart-postfix]]
- [[procedures/Configure-Postfix-for-XSS-Injection]]

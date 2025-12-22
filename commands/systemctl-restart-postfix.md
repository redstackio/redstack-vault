---
id: cmd-systemctl-postfix
data: systemctl restart postfix
tags:
  - postfix
  - service-management
type: command
output: null
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-13T23:55:20.745Z'
verified: false
validated: true
submitted: true
---
# systemctl-restart-postfix

## Command

```bash
systemctl restart postfix
```

## Description

This command restarts the Postfix service to apply configuration changes, such as new recipient access rules for SMTP rejections with custom payloads.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| postfix | Name of the Postfix service | Yes |
| restart | Action to stop and start the service | Yes |

## Examples

### Basic Usage

```bash
systemctl restart postfix
```

### Advanced Usage

```bash
systemctl restart postfix --now
```

## Expected Output

Silent on success; use 'systemctl status postfix' to verify active state.

## Related

- [[commands/postmap-update-recipient-access]]
- [[procedures/Configure-Postfix-for-XSS-Injection]]

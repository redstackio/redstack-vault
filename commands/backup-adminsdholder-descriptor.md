---
id: a20b1b88-f8f1-4fae-9e2c-4f3b66f93f4c
type: command
executor: powershell
data: SDProp /backup /quiet
output: null
created_at: '2023-04-06T03:56:06.430083+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - adminsdholder
verified: true
validated: true
---

# backup-adminsdholder-descriptor

## Command

```powershell
SDProp /backup /quiet
```

## Description

Backs up the current AdminSDHolder security descriptor silently on a domain controller. This creates a snapshot for potential restoration before modifying ACLs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /backup | Initiates backup of the AdminSDHolder template | Yes |
| /quiet | Suppresses output for stealthy execution | No |

## Examples

### Basic Usage

```powershell
SDProp /backup /quiet
```

### With Output (Non-Quiet)

```powershell
SDProp /backup
```

## Expected Output

No output in quiet mode if successful. In non-quiet mode: "Backup completed successfully." Check for backup files in the system directory.

## Related

- [[procedures/Abuse-AdminSDHolder-for-Privilege-Escalation]]
- [[commands/restore-adminsdholder-descriptor]]

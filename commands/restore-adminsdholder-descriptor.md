---
id: f3b4525d-d82b-4f14-a769-3289eefb2a68
type: command
executor: powershell
data: SDProp /restore /quiet
output: null
created_at: '2023-04-06T03:56:06.430203+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - adminsdholder
verified: true
validated: true
---

# restore-adminsdholder-descriptor

## Command

```powershell
SDProp /restore /quiet
```

## Description

Restores the previously backed-up AdminSDHolder descriptor, reverting any custom ACL modifications.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /restore | Restores from backup | Yes |
| /quiet | Suppresses output | No |

## Examples

### Basic Usage

```powershell
SDProp /restore /quiet
```

### With Output

```powershell
SDProp /restore
```

## Expected Output

No output on success. Non-quiet: "Descriptor restored successfully."

## Related

- [[procedures/Abuse-AdminSDHolder-for-Privilege-Escalation]]
- [[commands/backup-adminsdholder-descriptor]]

---
id: 8b6eb249-c572-466a-88db-e578d58d1079
type: command
executor: powershell
data: SDProp /modify /quiet
output: null
created_at: '2023-04-06T03:56:06.430139+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - adminsdholder
verified: true
validated: true
---

# modify-adminsdholder-propagation

## Command

```powershell
SDProp /modify /quiet
```

## Description

Forces the application of the AdminSDHolder template to all protected objects, propagating any ACL changes made.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /modify | Applies the current AdminSDHolder descriptor | Yes |
| /quiet | Runs without console output | No |

## Examples

### Basic Usage

```powershell
SDProp /modify /quiet
```

### With Output

```powershell
SDProp /modify
```

## Expected Output

Silent success in quiet mode. Non-quiet: "Modification applied to X protected objects."

## Related

- [[procedures/Abuse-AdminSDHolder-for-Privilege-Escalation]]
- [[commands/backup-adminsdholder-descriptor]]

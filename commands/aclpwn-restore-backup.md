---
id: f0a03118-c6d1-4995-8604-fc34623b6c1d
name: aclpwn-restore-backup
type: command
executor: bash
data: python aclpwn.py --restore $_BACKUP_FILE_PATH
output: null
created_at: '2023-04-06T03:56:08.023060+00:00'
updated_at: '2023-04-10T20:26:32.381858+00:00'
platforms:
  - Linux
tags:
  - defense-evasion
  - active-directory
verified: true
validated: true
---

# aclpwn-restore-backup

## Command

```bash
python aclpwn.py --restore $_BACKUP_FILE_PATH
```

## Description

Restores Active Directory ACLs from a backup file created by ACLPwn, used to revert changes after privilege escalation to avoid detection.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --restore $_BACKUP_FILE_PATH | Path to backup file (e.g., ../aclpwn-backup.restore) | Yes |

## Examples

### Basic Usage

```bash
python aclpwn.py --restore ../aclpwn-20190319-125741.restore
```

## Expected Output

[*] Restoring ACLs from backup...
[*] ACLs restored successfully for targeted objects.

## Related

- [[procedures/PrivExchange-Attack-with-NTLM-Relay]]

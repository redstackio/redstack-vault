---
type: command
executor: cmd
data: 'vssadmin create shadow /for=C:'
output: null
created_at: '2023-04-06T03:56:03.847598+00:00'
updated_at: '2023-04-10T20:26:27.031869+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - active-directory
verified: true
validated: true
---

# create-volume-shadow-copy-vssadmin

## Command

```cmd
vssadmin create shadow /for=C:
```

## Description

Creates a new volume shadow copy (snapshot) of the specified drive, useful for accessing locked files like NTDS.DIT on Domain Controllers without downtime. Requires admin privileges and VSS service running.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /for=DRIVE | The drive letter to create shadow for (e.g., C:, D:) | Yes |
| /? | Display help | No |

## Examples

### Basic Usage

```cmd
vssadmin create shadow /for=C:
```

### Advanced Usage

```cmd
vssadmin create shadow /for=D:
```

## Expected Output

```
Successfully created shadow copy for 'C:\'
Shadow Copy ID: {xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx}
Shadow Copy Volume: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy2
```

Copy the Shadow Copy Volume path for file access. If failed: Check VSS service (`sc start vss`) or disk space.

## Related

- [[commands/copy-ntds-dit-from-shadow-copy]]
- [[procedures/Dump-AD-Domain-Credentials-Using-VSSAdmin]]

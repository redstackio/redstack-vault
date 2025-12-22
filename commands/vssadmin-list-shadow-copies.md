---
id: 40e474c9-a4ff-4414-b5ec-5aa1983fb910
name: vssadmin-list-shadow-copies
type: command
executor: cmd
data: vssadmin list shadows
output: null
created_at: '2023-04-06T03:56:30.010659+00:00'
updated_at: '2023-04-10T20:37:37.824369+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - shadow-copy
  - privilege-escalation
verified: true
validated: true
---

# vssadmin-list-shadow-copies

## Command

```cmd
vssadmin list shadows
```

## Description

This command uses the built-in vssadmin utility to list all Volume Shadow Copies on the system, displaying details like shadow copy ID, creation time, originating volume, and snapshot path. It is essential for identifying available snapshots in privilege escalation scenarios involving file access bypass.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| list | Subcommand to enumerate shadows | Yes |
| shadows | Specifies shadow copy listing | Yes |

## Examples

### Basic Usage

```cmd
vssadmin list shadows
```

### With Volume Filter (Advanced)

```cmd
vssadmin list shadows /for=C:
```

## Expected Output

```
Contents of shadow copy set ID: {guid}
  Shadow Copy ID: {guid}
  Shadow Copy Volume: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
  Originating Volume Name: (C:)\?
  Service Machine: \\%computername%
  Service Machine: %computername%
  Shadow Copy Provider: 'Microsoft Software Shadow Copy provider 1.0'
  Shadow Copy Provider ID: {guid}
  Shadow Copy Provider Type: System
  Shadow Copy Provider Version: 1.0.0.0
  Shadow Copy Provider Format: Auto format
  Shadow Copy Provider Configuration: Original
  Shadow Copy Storage Association ID: {guid}
  Shadow Copy Storage Association Device: \\?\GLOBALROOT\Device\HarddiskVolume1\Recoverypartition
  Shadow Copy Storage Association Volume: (R:)\?
  Shadow Copy Set Type: Auto
  Shadow Copy Set Attributes: Automatic (not user initiated)
  Shadow Copy Set Persistent: No
  Shadow Copy Set Client Name: 'default'
  Shadow Copy Set Count: 1
  Shadow Copy Creation Time: 4/10/2023 12:00:00 PM
```

## Related

- [[procedures/Abusing-Shadow-Copies-for-Privilege-Escalation]]
- [[commands/diskshadow-list-shadow-copies]]

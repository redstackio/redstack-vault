---
id: 83eb9731-5c98-4ba2-a873-dff26f6c2fd3
name: mimikatz-misc-shadowcopies
type: command
executor: cmd
data: 'mimikatz> misc::shadowcopies'
output: null
created_at: '2023-04-06T03:56:28.851508+00:00'
updated_at: '2023-04-10T20:37:52.895105+00:00'
platforms:
  - Windows
tags:
  - vss
  - shadow-copy
verified: true
validated: true
---

# mimikatz-misc-shadowcopies

## Command

```cmd
mimikatz> misc::shadowcopies
```

## Description

Lists all available Volume Shadow Copies on the system within Mimikatz. Essential for identifying accessible backup paths for registry hives in exploits like HiveNightmare.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| (none) | No parameters; lists all shadow copies | No |

## Examples

### Basic Usage

```cmd
mimikatz> misc::shadowcopies
```

## Expected Output

```
Volume Shadow Copy 1: \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1
Volume Shadow Copy 2: ...
```

Note the volume paths for use in subsequent dumps.

## Related

- [[procedures/HiveNightmare-SAM-Dump-via-Shadow-Copies]]

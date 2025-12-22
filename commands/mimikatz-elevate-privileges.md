---
type: command
executor: mimikatz
data: 'privilege::debug'
output: null
platforms:
  - Windows
tags:
  - privilege-escalation
  - mimikatz
verified: true
validated: true
---

# mimikatz-elevate-privileges

## Command

```mimikatz
privilege::debug
```

## Description

Enables debug privileges in Mimikatz, required for modules like LSADUMP to access protected memory and perform operations such as DCSync. Run this immediately after launching Mimikatz to ensure sufficient rights.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | No parameters; enables SeDebugPrivilege globally for the session | No |

## Examples

### Basic Usage

```mimikatz
mimikatz # privilege::debug
```

### Usage in Session

After launching Mimikatz.exe as administrator, execute this to confirm privileges before DCSync.

## Expected Output

Privilege '20' OK

This indicates successful elevation. If it fails, relaunch Mimikatz with higher privileges (e.g., SYSTEM via token manipulation).

## Related

- [[procedures/Mimikatz-DCSync-Password-Hash-Dumping]]
- [[tools/Mimikatz]]

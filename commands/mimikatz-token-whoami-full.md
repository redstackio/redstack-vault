---
id: a26a342f-40fd-4e67-84c1-d6220c6104cb
name: mimikatz-token-whoami-full
type: command
executor: cmd
data: 'mimikatz> token::whoami /full'
output: null
created_at: '2023-04-06T03:56:28.851450+00:00'
updated_at: '2023-04-10T20:37:52.895105+00:00'
platforms:
  - Windows
tags:
  - credentials
  - token
verified: true
validated: true
---

# mimikatz-token-whoami-full

## Command

```cmd
mimikatz> token::whoami /full
```

## Description

Within Mimikatz, displays detailed information about the current process token, including user SID, privileges, and impersonation level. Useful for verifying access before attempting credential dumps.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /full | Shows complete token details including groups and privileges | Yes |

## Examples

### Basic Usage

```cmd
mimikatz> token::whoami /full
```

## Expected Output

```
Token Id  : 0x123456
User      : lowpriv\user
SID       : S-1-5-21-...
Privileges: SeDebugPrivilege (disabled)
Groups    : ...
Impersonation level : Anonymous
```

Indicates current privileges; look for limited rights to confirm low-priv execution.

## Related

- [[procedures/HiveNightmare-SAM-Dump-via-Shadow-Copies]]

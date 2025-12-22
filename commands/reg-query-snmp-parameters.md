---
type: command
executor: cmd
data: reg query "HKLM\SYSTEM\CurrentControlSet\Services\SNMP"
output: null
created_at: '2023-10-01T00:00:00+00:00'
updated_at: '2023-10-01T00:00:00+00:00'
platforms:
  - Windows
tags:
  - credential-access
  - snmp
verified: true
validated: true
---

# reg-query-snmp-parameters

## Command

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Services\SNMP"
```

## Description

Queries SNMP service parameters for community strings.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Key path | SNMP registry path | Yes |

## Examples

### Basic Usage

```cmd
reg query "HKLM\SYSTEM\CurrentControlSet\Services\SNMP"
```

## Expected Output

```
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\SNMP\Parameters
    ValidCommunities    REG_SZ    public
```

## Related

- [[procedures/windows-password-and-credential-query-via-registry]]

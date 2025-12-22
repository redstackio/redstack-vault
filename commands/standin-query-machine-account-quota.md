---
id: 873c0d10-882e-4a9f-a6c9-7269a237d7e9
name: standin-query-machine-account-quota
type: command
executor: cmd
data: StandIn.exe --object ms-DS-MachineAccountQuota=*
output: null
created_at: '2023-04-06T03:56:03.034713+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - active-directory
verified: true
validated: true
---

# standin-query-machine-account-quota

## Command

```cmd
StandIn.exe --object ms-DS-MachineAccountQuota=*
```

## Description

This command uses StandIn.exe to query Active Directory for objects matching the ms-DS-MachineAccountQuota attribute, revealing quota configurations across the domain. It is typically run after initial enumeration to gather detailed object information.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --object | Specifies the LDAP filter (ms-DS-MachineAccountQuota=*) | Yes |

## Examples

### Basic Usage

```cmd
StandIn.exe --object ms-DS-MachineAccountQuota=*
```

### Advanced Usage

```cmd
StandIn.exe --object ms-DS-MachineAccountQuota=* -v
```

## Expected Output

Output lists matching objects:

[+] Found ms-DS-MachineAccountQuota=10 on CN=System,DC=domain,DC=local

If no matches: No objects found.

## Related

- [[procedures/Active-Directory-Machine-Account-Enumeration-using-CrackMapExec]]
- [[tools/StandIn]]

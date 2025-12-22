---
id: 081ee469-9b8b-4514-96c9-c3a3cd06ec72
type: command
executor: powershell
data: >-
  Execute-Command -OS Windows -VM $_VM_NAME -ResourceGroup $_RG_NAME -Command
  "$_COMMAND"
output: null
created_at: '2023-04-06T03:56:14.586660+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
tags:
  - execution
  - vm
verified: true
validated: true
---

# powerzure-execute-command-on-vm

## Command

```powershell
Execute-Command -OS Windows -VM $_VM_NAME -ResourceGroup $_RG_NAME -Command "$_COMMAND"
```

## Description

Executes a command on an Azure VM using Contributor privileges via Run Command feature.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -OS | OS type (Windows/Linux) | Yes |
| -VM, $_VM_NAME | Target VM name | Yes |
| -ResourceGroup, $_RG_NAME | Resource group name | Yes |
| -Command, $_COMMAND | Command to execute | Yes |

## Examples

### Basic Usage

```powershell
Execute-Command -OS Windows -VM Win10Test -ResourceGroup Test-RG -Command "whoami"
```

## Expected Output

Command output: e.g., "win10test\user".

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/PowerZure]]

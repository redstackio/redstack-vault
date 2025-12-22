---
id: be1f4ff2-9d50-4c62-b973-d80af48bd2b9
type: command
executor: powershell
data: Execute-MSBuild -VM $_VM_NAME -ResourceGroup $_RG_NAME -File "$_FILE"
output: null
created_at: '2023-04-06T03:56:14.586730+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Azure
tags:
  - execution
  - msbuild
verified: true
validated: true
---

# powerzure-execute-msbuild-on-vm

## Command

```powershell
Execute-MSBuild -VM $_VM_NAME -ResourceGroup $_RG_NAME -File "$_FILE"
```

## Description

Executes an MSBuild file on an Azure VM for code execution via Contributor role.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -VM, $_VM_NAME | Target VM name | Yes |
| -ResourceGroup, $_RG_NAME | Resource group | Yes |
| -File, $_FILE | Path to MSBuild XML file | Yes |

## Examples

### Basic Usage

```powershell
Execute-MSBuild -VM Win10Test -ResourceGroup Test-RG -File "build.xml"
```

## Expected Output

MSBuild execution logs and any payload output.

## Related

- [[procedures/Azure-Reconnaissance]]
- [[tools/PowerZure]]

---
id: 853f1528-9f82-4170-8964-182b340855dc
name: Create-New-PowerShell-Session-Configuration
type: command
executor: powershell
data: Register-PSSessionConfiguration -Name $_CONFIG_NAME -Path $_CONFIG_PATH -Force
output: null
created_at: '2023-04-06T03:56:26.428890+00:00'
updated_at: '2023-04-10T20:37:06.785363+00:00'
platforms:
  - Windows
tags:
  - powershell
  - jea
verified: true
validated: true
---

# Create-New-PowerShell-Session-Configuration

## Command

```powershell
Register-PSSessionConfiguration -Name $_CONFIG_NAME -Path $_CONFIG_PATH -Force
```

## Description

Registers a new PowerShell session configuration (e.g., for JEA endpoints), enabling constrained remote sessions with defined roles and capabilities.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -Name | Name of the configuration (e.g., 'MyJEAEndpoint') | Yes |
| -Path | Path to the .pssc file defining the configuration | Yes |
| -Force | Overwrite existing configuration without prompt | No |
| -TrustPipelineInput | Allow pipeline input for security | No |

## Examples

### Basic Usage

```powershell
Register-PSSessionConfiguration -Name 'MyJEA' -Path 'C:\MyJEA.pssc'
```

### Advanced Usage

```powershell
Register-PSSessionConfiguration -Name 'MyJEAEndpoint' -Path 'C:\Path\To\MyJEAConfiguration.pssc' -Force -TrustPipelineInput
```

## Expected Output

The configuration 'MyJEAEndpoint' was registered successfully.

## Related

- [[procedures/implement-jea-to-limit-powershell-cmdlet-usage]]

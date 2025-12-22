---
id: 57d93a38-63a9-4a46-8e07-46b929dbe0f7
name: powerup-find-dll-hijack
type: command
executor: powershell
data: Import-Module PowerUp.ps1; Find-PathDLLHijack
output: null
created_at: '2023-04-06T03:56:29.436640+00:00'
updated_at: '2023-04-10T20:37:36.999118+00:00'
platforms:
  - Windows
tags:
  - dll-hijacking
  - privesc
verified: true
validated: true
---

# powerup-find-dll-hijack

## Command

```powershell
Import-Module PowerUp.ps1; Find-PathDLLHijack
```

## Description

Uses PowerUp.ps1 to scan for potential DLL hijacking paths in environment variables and service contexts, identifying writable directories for malicious DLL placement.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Runs default scan | No |

## Examples

### Basic Usage

```powershell
. \PowerUp.ps1; Find-PathDLLHijack
```

## Expected Output

[+] C:\ProgramData\Service\ : Writable (DLL Hijack Point)

Lists exploitable paths.

## Related

- [[procedures/Windows-Local-Service-Permissions-Escalation]]

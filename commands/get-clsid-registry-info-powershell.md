---
id: 7703cebb-1c22-4684-a910-538dfda4bf57
name: get-clsid-registry-info-powershell
type: command
executor: powershell
data: >-
  Get-ChildItem -Path
  'HKLM:\SOFTWARE\Classes\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}'

  Name                           Property

  ----                           --------

  Hosts                          (default) : Scanned Hosting Applications

  InprocServer32                 (default) : "C:\ProgramData\Microsoft\Windows
  Defender\Platform\4.18.2210.4-0\MpOav.dll"
output: null
created_at: '2023-04-06T03:56:25.869094+00:00'
updated_at: '2023-04-10T20:36:15.840247+00:00'
platforms:
  - Windows
tags:
  - discovery
  - registry
  - amsi
verified: true
validated: true
---

# get-clsid-registry-info-powershell

## Command

```powershell
Get-ChildItem -Path 'HKLM:\SOFTWARE\Classes\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}'
```

## Description

This PowerShell command retrieves subkey information from the Windows registry for the CLSID {2781761E-28E0-4109-99FE-B9D127C57AFE}, which is associated with the Anti-Malware Scan Interface (AMSI) provider. It lists properties like 'Hosts' (scanned applications) and 'InprocServer32' (the DLL path for the scanning provider, such as Windows Defender's MpOav.dll). Use this during discovery to identify endpoint security software without executing scans.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-Path` | Registry path to query (fixed to AMSI CLSID for this use) | Yes |

## Examples

### Basic Usage

```powershell
Get-ChildItem -Path 'HKLM:\SOFTWARE\Classes\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}'
```

### Advanced Usage

To get more details on the InprocServer32 subkey:

```powershell
Get-ItemProperty -Path 'HKLM:\SOFTWARE\Classes\CLSID\{2781761E-28E0-4109-99FE-B9D127C57AFE}\InprocServer32'
```

## Expected Output

```
Name                           Property
----                           --------
Hosts                          (default) : Scanned Hosting Applications
InprocServer32                 (default) : "C:\ProgramData\Microsoft\Windows Defender\Platform\4.18.2210.4-0\MpOav.dll"
```

This output confirms the AMSI provider details. If the key is missing, AMSI may be disabled or the system is non-standard.

## Related

- [[procedures/Enumerate-AMSI-Providers-via-Registry]]
- [[techniques/Software Discovery|T1518]]

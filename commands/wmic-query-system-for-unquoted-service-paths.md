---
id: 859b352a-5601-473d-88d2-5a8febe2595e
type: command
executor: command_prompt
data: >-
  wmic.exe service get name,displayname,pathname,startmode |findstr /i "auto"
  |findstr /i /v "c:\windows\\" |findstr /i /v """"
output: >-
  C:\>wmic.exe service get name,displayname,pathname,startmode |findstr /i
  "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """

  Skype Service    Skype C:\Program Files (x86)\Microsoft\Skype.exe --service   
  Auto
created_at: '2020-01-27T20:41:03.448594+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - misconfiguration
  - enumeration
verified: true
validated: true
---

# wmic-query-system-for-unquoted-service-paths

## Command

```command_prompt
wmic.exe service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """"
```

## Description

This command enumerates Windows services using WMIC, retrieving the service name, display name, executable path, and start mode. It then pipes the output through findstr filters to identify auto-starting services outside the Windows directory that have unquoted paths, which are potential vectors for path interception attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `service get name,displayname,pathname,startmode` | WMIC query to fetch service properties: name (internal name), displayname (user-friendly name), pathname (executable path), startmode (startup type like Auto) | Built-in |
| `findstr /i "auto"` | Case-insensitive search for lines containing 'auto' to filter auto-starting services | Built-in |
| `findstr /i /v "c:\windows\\"` | Case-insensitive exclusion (/v) of lines containing 'c:\windows\' to ignore system services | Built-in |
| `findstr /i /v """"` | Case-insensitive exclusion of lines with double quotes to focus on unquoted paths | Built-in |

## Examples

### Basic Usage

Run directly in Command Prompt to query the local system:

```command_prompt
wmic.exe service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """"
```

### Advanced Usage

To run remotely on another host (requires admin creds and WMI access):

```command_prompt
wmic.exe /node:TARGET_HOST /user:DOMAIN\USER /password:PASS service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\" | findstr /i /v """"
```

### PowerShell Adaptation

If running in PowerShell (which may mishandle quotes), prefix with cmd:

```powershell
cmd.exe /C "wmic.exe service get name,displayname,pathname,startmode | findstr /i \"auto\" | findstr /i /v \"c:\\windows\\\\\" | findstr /i /v \\\"\\\""
```

## Expected Output

Description of what output to expect when the command runs successfully.

If vulnerable services are found, output resembles:

```
C:\>wmic.exe service get name,displayname,pathname,startmode |findstr /i "auto" |findstr /i /v "c:\windows\\" |findstr /i /v """
Skype Service    Skype C:\Program Files (x86)\Microsoft\Skype.exe --service    Auto
```

Each line shows a potential vulnerable service. Empty output indicates no unquoted auto-start services outside Windows paths. Review 'pathname' for spaces without quotes to confirm vulnerability.

## Related

- [[procedures/Query-Windows-for-Unquoted-Service-Paths]]

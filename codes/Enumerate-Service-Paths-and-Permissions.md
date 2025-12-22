---
id: 00e0d44d-6c49-4f11-b325-730be1c892d7
type: code
name: Enumerate-Service-Paths-and-Permissions
language: batch
verified: true
created_at: '2023-04-06T03:56:29.436806+00:00'
updated_at: '2023-04-10T20:37:37.001468+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - services
validated: true
---

# Enumerate-Service-Paths-and-Permissions

## Code

```batch
$ for /f "tokens=2 delims='='" %a in ('wmic service list full^|find /i "pathname"^|find /i /v "system32"') do @echo %a >> c:\windows\temp\permissions.txt
$ for /f eol=^"^ delims=^" %a in (c:\windows\temp\permissions.txt) do cmd.exe /c icacls "%a"

$ sc query state=all | findstr "SERVICE_NAME:" >> Servicenames.txt
FOR /F %i in (Servicenames.txt) DO echo %i
type Servicenames.txt
FOR /F "tokens=2 delims= " %i in (Servicenames.txt) DO @echo %i >> services.txt
FOR /F %i in (services.txt) DO @sc qc %i | findstr "BINARY_PATH_NAME" >> path.txt
```

## Description

Batch script to enumerate Windows services, extract non-system32 binary paths, audit their permissions with icacls, and generate lists of service names and paths for identifying escalation vectors.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| None | Uses default temp files; modify paths if needed | N/A |

## Usage

Save as .bat and execute on target via cmd. Review permissions.txt and path.txt for writable locations. Delete temps post-use.

## Detection

- Suspicious WMIC/SC queries in command logs (Event ID 4688).
- File creation in C:\\windows\\temp\\ by low-priv users.

## Related

- [[procedures/Windows-Local-Service-Permissions-Escalation]]

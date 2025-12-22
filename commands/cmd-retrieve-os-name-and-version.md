---
type: command
executor: cmd
data: 'systeminfo | findstr /B /C:"OS Name" /C:"OS Version"'
output: null
created_at: '2023-04-06T03:56:28.589156+00:00'
updated_at: '2023-04-10T20:37:36.292864+00:00'
platforms:
  - Windows
tags:
  - discovery
  - os-information
verified: true
validated: true
---

# cmd-retrieve-os-name-and-version

## Command

```cmd
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

## Description

This command queries the Windows system for the OS name and version using systeminfo, filtered via findstr. Use it during initial reconnaissance to identify the build for vulnerability research in privilege escalation.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| /B | Matches at the beginning of lines | Built-in |
| /C:"OS Name" | String to search for OS Name | Built-in |
| /C:"OS Version" | String to search for OS Version | Built-in |

No user-supplied parameters; the command is fixed.

## Examples

### Basic Usage

```cmd
systeminfo | findstr /B /C:"OS Name" /C:"OS Version"
```

### Advanced Usage

Pipe to file for logging: `systeminfo | findstr /B /C:"OS Name" /C:"OS Version" > os_info.txt`

## Expected Output

```
OS Name:                   Microsoft Windows 10 Pro
OS Version:                10.0.19041 N/A Build 19041
```

Success is indicated by the display of OS details without errors.

## Related

- [[procedures/windows-os-information-gathering-for-privilege-escalation]]

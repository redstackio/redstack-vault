---
id: fa48b57a-9708-4e9f-91f9-30784dcec9e9
name: winpeas-execute-enumeration
type: command
executor: command_prompt
data: winPEAS.exe $_OPTIONS
output: |-
  Creating Dynamic lists, this could take a while, please wait...
  - Checking if domain...
  - Getting Win32_UserAccount info...
  - Creating current user groups list...
  - Creating active users list...
  - Creating disabled users list...
  - Admin users list...
  [... detailed enumeration output ...]
  [+] File C:\Users\Public\winPEAS.log created
created_at: '2020-03-12T23:11:13.796632+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - enumeration
  - priv-esc
verified: true
validated: true
---

# winpeas-execute-enumeration

## Command

```command_prompt
winPEAS.exe $_OPTIONS
```

## Description

Executes the winPEAS tool to enumerate a Windows system for privilege escalation opportunities, generating a comprehensive report on potential vectors.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_OPTIONS | Optional flags (e.g., -h for help, quiet for silent mode, or specific checks like systeminfo) | No |

## Examples

### Basic Usage

```command_prompt
winPEAS.exe
```

### Advanced Usage

```command_prompt
winPEAS.exe quiet
```

Suppresses console output for stealth.

## Expected Output

Creating Dynamic lists, this could take a while, please wait...
- Checking if domain...
- Getting Win32_UserAccount info...
- Creating current user groups list...
- Creating active users list...
- Creating disabled users list...
- Admin users list...

Sections follow with checks for services, software, credentials, etc. A log file (winPEAS.log) is created with highlighted potential issues.

## Related

- [[procedures/Enumerate-Windows-for-Privilege-Escalation-with-winPEAS]]
- [[tools/winPEAS]]

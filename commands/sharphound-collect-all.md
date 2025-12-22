---
id: c7f78e78-40b6-4eb9-b292-a59d1329a88e
name: sharphound-collect-all
type: command
executor: command_prompt
data: >-
  SharpHound.exe -c All -d $_DOMAIN --ldapusername $_USER --ldappassword
  $_PASSWORD --outputdirectory C:\Temp
output: SharpHound Enumeration Completed! Happy Graphing!
created_at: '2020-03-15T23:15:05.164898+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - ad
  - enumeration
verified: true
validated: true
---

# sharphound-collect-all

## Command

```command_prompt
SharpHound.exe -c All -d $_DOMAIN --ldapusername $_USER --ldappassword $_PASSWORD --outputdirectory C:\Temp
```

## Description

Collects all AD data with credentials.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -c All | Collection methods | Yes |
| -d $_DOMAIN | Domain | Yes |
| --ldapusername $_USER | Username | Yes |
| --ldappassword $_PASSWORD | Password | Yes |
| --outputdirectory C:\Temp | Output dir | Yes |

## Examples

### Basic Usage

```command_prompt
SharpHound.exe -c All -d lab.local --ldapusername user --ldappassword pass --outputdirectory C:\Temp
```

## Expected Output

ZIP file in directory.

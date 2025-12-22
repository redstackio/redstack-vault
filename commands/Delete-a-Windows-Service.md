---
id: 5d94ecb7-83ca-4a13-bad3-e795b9838b84
name: Delete-a-Windows-Service
type: command
executor: command_prompt
data: sc.exe delete $_SERVICE_NAME
output: |-
  C:\Windows\system32>sc.exe delete pwnSVC
  [SC] DeleteService SUCCESS
created_at: '2020-04-28T21:10:21.095995+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - cleanup
  - persistence
verified: true
validated: true
---

# Delete-a-Windows-Service

## Command

```command_prompt
sc.exe delete $_SERVICE_NAME
```

## Description

This command removes a previously created Windows service using sc.exe. It is used for cleanup after testing or exploitation to erase traces of malicious services.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_SERVICE_NAME | Name of the service to delete (e.g., pwnSVC) | Yes |

## Examples

### Basic Usage

```command_prompt
sc.exe delete pwnSVC
```

## Expected Output

```
C:\Windows\system32>sc.exe delete pwnSVC
[SC] DeleteService SUCCESS
```

The service is immediately removed from the registry.

## Related

- [[commands/Create-a-Windows-Service]]
- [[commands/Start-a-Windows-Service]]
- [[procedures/Create-and-Run-Windows-Service-as-SYSTEM-Administrator]]

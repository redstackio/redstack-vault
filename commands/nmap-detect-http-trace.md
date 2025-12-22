---
id: b13d8add-e7d2-4c14-a8b9-26f59c2c76d0
name: nmap-detect-http-trace
type: command
executor: bash
data: nmap --script http-trace -p$_PORT $_TARGET
output: |-
  Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 15:14 IST
  Nmap scan report for 192.168.1.3
  Host is up (0.00048s latency).

  PORT   STATE SERVICE
  $_PORT/tcp open  http
  |_http-trace: TRACE is enabled
created_at: '2020-09-01T16:56:54.515251+00:00'
updated_at: '2023-05-29T16:48:52.884824+00:00'
platforms:
  - Linux
  - Web
tags:
  - reconnaissance
  - web-scanning
verified: true
validated: true
---

# nmap-detect-http-trace

## Command

```bash
nmap --script http-trace -p$_PORT $_TARGET
```

## Description

This command uses Nmap's built-in http-trace script to scan a target web server for support of the TRACE HTTP method. It sends a TRACE request to the specified port and reports if the server echoes the request, indicating the method is enabled. Use this during web reconnaissance to identify potential information disclosure risks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| --script http-trace | Loads the http-trace NSE script to test for TRACE method | Yes |
| -p$_PORT | Specifies the port to scan (e.g., 80 for HTTP, 443 for HTTPS) | Yes |
| $_TARGET | IP address or hostname of the target web server | Yes |

## Examples

### Basic Usage

```bash
nmap --script http-trace -p80 192.168.1.3
```

### Advanced Usage

```bash
nmap --script http-trace -p80,443 --script-args http-trace.path=/admin 10.0.0.1
```

This variation specifies a custom path for the TRACE request.

## Expected Output

When TRACE is enabled:

```
Starting Nmap 7.70 ( https://nmap.org ) at 2020-09-01 15:14 IST
Nmap scan report for 192.168.1.3
Host is up (0.00048s latency).

PORT   STATE SERVICE
80/tcp open  http
|_http-trace: TRACE is enabled
```

When disabled, the output may show:

```
|_http-trace: TRACE is not enabled
```

## Related

- [[procedures/Detect-TRACE-HTTP-Method-with-Nmap]]
- [[tools/Nmap]]

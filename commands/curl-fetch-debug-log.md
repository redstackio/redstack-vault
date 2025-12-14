---
id: cmd-uuid-001
data: 'curl -s https://exacthosting.example.com/debug.log -o debug.log'
tags:
  - recon
  - information-disclosure
  - web
type: command
output: null
executor: bash
platforms:
  - Linux
  - macOS
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:56.386Z'
verified: false
validated: true
submitted: true
---
# curl-fetch-debug-log

## Command

```bash
curl -s https://exacthosting.example.com/debug.log -o debug.log
```

## Description

This command uses curl to silently download a publicly accessible debug.log file from an ExactHosting web server, saving it locally for analysis. It is used in reconnaissance to disclose debugging information without alerting the server (silent mode).

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-s` | Silent mode: Suppress progress meter and error messages | Yes |
| `https://exacthosting.example.com/debug.log` | URL of the target debug log file | Yes |
| `-o debug.log` | Output file name for the downloaded content | Yes |

## Examples

### Basic Usage

```bash
curl -s https://exacthosting.example.com/debug.log -o debug.log
```

### Advanced Usage

```bash
curl -s -H "User-Agent: Mozilla/5.0" https://exacthosting.example.com/debug.log -o debug.log
```

> Adds a user-agent header to mimic browser traffic.

## Expected Output

A local file 'debug.log' containing the server's debug log entries, such as:

```
[2023-01-01 12:00:00] INFO: Request from IP 1.2.3.4
[2023-01-01 12:01:00] ERROR: Failed to connect to database
```

If the file is not accessible, curl returns an error (e.g., 404 or 403), but in vulnerable cases, it succeeds with HTTP 200.

## Related

- [[Related Procedure: Access-Public-Debug-Log-for-Information-Disclosure]]

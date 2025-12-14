---
data: nc -v -l 12346
tags:
  - ssrf
  - network
type: command
output: >-
  Connection from [54.82.61.224] port 12346 [tcp/*] accepted (family 2, sport
  44251)

  GET /BASICSSRF HTTP/1.1

  User-Agent: Lavf/55.48.100

  Accept: */*

  Connection: close

  Host: www.gradeco.ru:12346
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T04:39:09.579Z'
id: 53543ac0-c971-4ab2-9a93-a0134cbbacf2
verified: false
validated: true
submitted: true
---
# nc-listen-ssrf

## Command

```bash
nc -v -l 12346
```

## Description

This command uses netcat to listen on port 12346 in verbose mode, capturing incoming TCP connections and HTTP requests triggered by SSRF exploits, such as those from Imgur's ffmpeg.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-v` | Verbose output to show connection details | Yes |
| `-l` | Listen mode for incoming connections | Yes |
| `12346` | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
nc -v -l 12346
```

### Advanced Usage

For specific interface: ```bash
nc -v -l 0.0.0.0 12346
```

## Expected Output

Connection from Imgur IP with GET request details, including User-Agent indicating ffmpeg version.

## Related

- [[Related Procedure: Capture-SSRF-Request-with-Netcat]]

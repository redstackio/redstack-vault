---
type: command
executor: bash
data: nmap -sCV $_TARGET_IP -p 2376
output: null
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
platforms:
  - Linux
tags:
  - scanning
  - docker
verified: true
validated: true
---

# nmap-scan-docker-api-port

## Command

```bash
nmap -sCV $_TARGET_IP -p 2376
```

## Description

Scans a specific target IP for the unencrypted Docker API port (2376) using service version detection and default scripts to identify the Docker daemon and its version.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_TARGET_IP | IP address of the target host | Yes |
| -sCV | Service version scan with default scripts | Built-in |
| -p 2376 | Scan only port 2376 | Built-in |

## Examples

### Basic Usage

```bash
nmap -sCV 10.10.10.10 -p 2376
```

### Advanced Usage

```bash
nmap -sCV 10.10.10.0/24 -p 2375,2376
```

## Expected Output

```
2376/tcp open  docker  Docker 19.03.5
| docker-version:
|   Version: 19.03.5
|   MinAPIVersion: 1.12
```

## Related

- [[procedures/Exploit-Open-Docker-API-for-Container-Management]]
- [[tools/Nmap]]

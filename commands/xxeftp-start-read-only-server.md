---
id: acfb8c16-abfa-4998-8659-16d25601e135
name: xxeftp-start-read-only-server
type: command
executor: bash
data: sudo ./xxeftp -uno $_PORT
output: null
created_at: '2023-04-06T03:56:43.973059+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Linux
tags:
  - xxe
  - server
  - ftp
verified: true
validated: true
---

# xxeftp-start-read-only-server

## Command

```bash
sudo ./xxeftp -uno $_PORT
```

## Description

Starts XXEFTP in read-only mode on a specified port, providing a mini webserver with FTP support for hosting XXE payloads during file enumeration attacks.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | Port to bind the server (default: 443) | Yes |
| -uno | Read-only mode flag | Built-in |

## Examples

### Basic Usage

```bash
sudo ./xxeftp -uno 443
```

### Custom Port

```bash
sudo ./xxeftp -uno 8443
```

## Expected Output

Server started successfully on port 443 with read-only FTP access. Logs incoming connections and file requests.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEFTP]]

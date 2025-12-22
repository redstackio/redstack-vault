---
id: 593b6cae-954f-43e4-98af-b6fe9f98faa1
name: xxeftp-start-write-server
type: command
executor: bash
data: ./xxeftp -w -wps $_PORT
output: null
created_at: '2023-04-06T03:56:43.973117+00:00'
updated_at: '2023-04-10T20:24:45.357412+00:00'
platforms:
  - Linux
tags:
  - xxe
  - server
  - ftp
  - upload
verified: true
validated: true
---

# xxeftp-start-write-server

## Command

```bash
./xxeftp -w -wps $_PORT
```

## Description

Launches XXEFTP with write permissions, allowing file uploads via FTP in XXE exploitation scenarios.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_PORT | Write server port (default: 5555) | Yes |
| -w | Enable write access | Built-in |
| -wps | Write port specifier | Built-in |

## Examples

### Basic Usage

```bash
./xxeftp -w -wps 5555
```

## Expected Output

Write server initialized on port 5555, ready for FTP uploads.

## Related

- [[procedures/Exploit-XXE-Vulnerability-Using-Multiple-Tools]]
- [[tools/XXEFTP]]

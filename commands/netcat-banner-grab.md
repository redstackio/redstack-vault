---
id: cmd-uuid-001
data: nc target_host 22
tags:
  - reconnaissance
  - network
type: command
output: SSH-2.0-OpenSSH_5.5p1 Debian-6+squeeze5
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:55.797Z'
verified: false
validated: true
submitted: true
---
# netcat-banner-grab

## Command

```bash
nc target_host 22
```

## Description

This command uses Netcat to connect to an SSH service on port 22 and capture the initial banner, revealing the server version without authentication. Useful for quick reconnaissance of SSH implementations.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `target_host` | IP or hostname of the target | Yes |
| `22` | SSH port (default) | Yes |

## Examples

### Basic Usage

```bash
nc blog.greenhouse.io 22
```

### Advanced Usage

```bash
nc -v target_host 22  # Verbose output for connection details
```

## Expected Output

The server responds with the banner string, e.g., "SSH-2.0-OpenSSH_5.5p1 Debian-6+squeeze5", followed by a connection prompt. Disconnect immediately after capture.

## Related

- [[Related Procedure|Gather-SSH-Server-Version-via-Banner-Grabbing]]
- [[Related Command|grep-version-parse]]

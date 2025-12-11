---
data: nc -lvnp 8080
tags:
  - network
  - listen
type: command
executor: bash
platforms:
  - Linux
  - macOS
id: cc6b4c12-8d02-40cc-a3da-cf1991254621
created_at: '2025-12-11T06:10:28.368Z'
updated_at: '2025-12-11T06:10:28.368Z'
verified: false
validated: true
submitted: true
---
# netcat-listen

## Command

```bash
nc -lvnp 8080
```

## Description

Sets up a listener on a specified port to capture incoming connections, useful for exfiltration during exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-l` | Listen mode | Yes |
| `-v` | Verbose output | No |
| `-n` | No DNS resolution | No |
| `-p 8080` | Port to listen on | Yes |

## Examples

### Basic Usage

```bash
nc -lvnp 8080
```

### Advanced Usage

```bash
nc -lvnp 443
```

## Expected Output

Connection received on port 8080 with any data sent by the client.

## Related

- [[tools/netcat]]
- [[procedures/Exploit-for-Account-Takeover]]

